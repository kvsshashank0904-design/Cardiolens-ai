import contract from './input-contract.json'

export type PredictionInput = Record<(typeof featureNames)[number], number>
export const featureNames = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'] as const
export type PredictionResponse = {
  prediction: 0 | 1; prediction_label: string; model_probability: number; probability_definition: string
  model: { name: string; experiment: string; preprocessing: string; threshold: number }
  explanation: { method: string; intercept: number; log_odds: number; feature_contributions: {feature:string;contribution:number}[]; interpretation: string }
  missing_features: string[]; disclaimer: string
}
export class ApiError extends Error {
  constructor(message:string, public kind:'backend'|'invalid'|'validation'='backend') { super(message) }
}
const offline = 'CardioLens backend is unavailable. Start the API and try again.'
const object = (v:unknown):v is Record<string,unknown> => !!v && typeof v==='object' && !Array.isArray(v)
const text = (v:unknown):v is string => typeof v==='string' && v.trim().length>0
const finite = (v:unknown):v is number => typeof v==='number' && Number.isFinite(v)

export function parsePrediction(v:unknown):PredictionResponse {
  const bad=()=>{throw new ApiError('Invalid response from CardioLens backend. No result was displayed.','invalid')}
  if(!object(v)) return bad()
  if(![0,1].includes(v.prediction as number) || !finite(v.model_probability) || v.model_probability<0 || v.model_probability>1) return bad()
  if(!text(v.prediction_label)||!text(v.probability_definition)||!text(v.disclaimer)) return bad()
  if(!object(v.model)||v.model.name!=='Logistic Regression'||v.model.experiment!=='Experiment 3'||v.model.preprocessing!=='primary_explicit_missing'||v.model.threshold!==contract.threshold) return bad()
  if(v.prediction!==Number(v.model_probability>=v.model.threshold)) return bad()
  const e=v.explanation
  if(!object(e)||!text(e.method)||!text(e.interpretation)||!finite(e.intercept)||!finite(e.log_odds)||!Array.isArray(e.feature_contributions)||!e.feature_contributions.length) return bad()
  const seen=new Set<string>();let sum=e.intercept
  for(const c of e.feature_contributions){
    if(!object(c)||!text(c.feature)||!finite(c.contribution)||seen.has(c.feature)) return bad()
    const match=/^(numeric|categorical)__([a-z]+)(?:_(-?\d+(?:\.\d+)?))?$/.exec(c.feature)
    if(!match||!(contract.features as string[]).includes(match[2]))return bad()
    seen.add(c.feature);sum+=c.contribution
  }
  // Completeness for the frozen 5-numeric / 8-one-hot feature representation.
  const expected=[...contract.numeric_features.map(f=>`numeric__${f}`),...contract.categorical_features.flatMap(f=>{
    const codes=contract.categorical_codes[f as keyof typeof contract.categorical_codes]
    return codes.map(code=>`categorical__${f}_${((f==='ca'&&code===4)||(f==='thal'&&code===0)?-1:code).toFixed(1)}`)
  })]
  if(seen.size!==expected.length || expected.some(f=>!seen.has(f)))return bad()
  if(Math.abs(sum-e.log_odds)>1e-8||Math.abs(1/(1+Math.exp(-e.log_odds))-v.model_probability)>1e-8)return bad()
  if(!Array.isArray(v.missing_features)||v.missing_features.some(f=>f!=='ca'&&f!=='thal')||new Set(v.missing_features).size!==v.missing_features.length)return bad()
  return v as unknown as PredictionResponse
}

export function inputFromForm(data:FormData):PredictionInput {
  const payload={} as PredictionInput
  for(const f of featureNames){
    const raw=data.get(f)
    if(typeof raw!=='string'||!raw.trim())throw new ApiError(`Enter ${f}.`,'validation')
    const value=Number(raw)
    if(!Number.isFinite(value))throw new ApiError(`Enter a finite number for ${f}.`,'validation')
    if(f in contract.categorical_codes){
      const codes:readonly number[]=contract.categorical_codes[f as keyof typeof contract.categorical_codes]
      if(!Number.isInteger(value)||!codes.includes(value))throw new ApiError(`Unsupported category for ${f}.`,'validation')
    }else{
      const [low,high]=contract.numeric_supported_ranges[f as keyof typeof contract.numeric_supported_ranges]
      if(value<low||value>high)throw new ApiError(`${f} must be within the prototype's supported range ${low}–${high}.`,'validation')
    }
    payload[f]=value
  }
  return payload
}

const base=(process.env.NEXT_PUBLIC_API_URL || '/api/cardiolens').replace(/\/$/,'')
async function request(path:string,payload?:PredictionInput):Promise<unknown>{
  let r:Response
  try{r=await fetch(`${base}/${path}`,{method:payload?'POST':'GET',headers:payload?{'Content-Type':'application/json'}:undefined,body:payload?JSON.stringify(payload):undefined,cache:'no-store',signal:AbortSignal.timeout(15000)})}
  catch{throw new ApiError(offline)}
  if(r.status===502||r.status===503||r.status===504)throw new ApiError(offline)
  let value:unknown
  try{value=await r.json()}catch{throw new ApiError('Invalid response from CardioLens backend. No result was displayed.','invalid')}
  if(!r.ok){
    if(r.status===422)throw new ApiError('The backend rejected these inputs. Check the supported ranges and category codes.','validation')
    throw new ApiError('The backend could not complete the request. Please try again.')
  }
  return value
}
export async function health(){const v=await request('health');if(!object(v)||v.status!=='ok'||v.model_loaded!==true)throw new ApiError(offline);return v}
export async function modelInfo(){const v=await request('model-info');if(!object(v)||v.experiment!=='Experiment 3'||v.threshold!==contract.threshold||JSON.stringify(v.features)!==JSON.stringify(featureNames))throw new ApiError('Backend model contract does not match the frozen frontend contract.','invalid');return v}
export async function predict(input:PredictionInput){return parsePrediction(await request('predict',input))}
