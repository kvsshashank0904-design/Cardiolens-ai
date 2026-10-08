import type { PredictionResponse } from './api'
export type FeatureContribution = {feature:string;key:string;value:number;note:string}
const labels:Record<string,string>={age:'Age',sex:'Sex',cp:'Chest Pain Type',trestbps:'Resting Blood Pressure',chol:'Cholesterol',fbs:'Fasting Blood Sugar',restecg:'Resting ECG',thalach:'Maximum Heart Rate',exang:'Exercise Angina',oldpeak:'Oldpeak',slope:'ST Slope',ca:'CA',thal:'Thal'}
export function humanize(name:string){
 const match=/^(numeric|categorical)__([a-z]+)(?:_(-?\d+(?:\.\d+)?))?$/.exec(name)
 if(!match)return name
 const label=labels[match[2]]||match[2]
 if(match[1]==='numeric')return label
 return `${label}: ${Number(match[3])===-1?'Not recorded in source dataset':`category ${Number(match[3])}`}`
}
export function resultView(response:PredictionResponse){return {
 id:'Local view', timestamp:new Date().toISOString(), classification:response.prediction_label,
 probability:response.model_probability, threshold:response.model.threshold,
 modelVersion:response.model.experiment, explainer:'Logistic contributions', response,
 contributions:response.explanation.feature_contributions.map(c=>({feature:humanize(c.feature),key:c.feature,value:c.contribution,note:'Contribution in log-odds units.'})).sort((a,b)=>Math.abs(b.value)-Math.abs(a.value))
}}
export type ResultView=ReturnType<typeof resultView>
export const ATTRIBUTION_CAVEAT='Contributions describe statistical model behavior, not medical causes. This is a research prototype and is not a medical diagnosis.'
