const allowed=new Set(['health','model-info','predict'])
async function proxy(request:Request,context:{params:Promise<{endpoint:string}>}){
  const {endpoint}=await context.params
  if(!allowed.has(endpoint))return Response.json({detail:'Not found'},{status:404})
  if((endpoint==='predict')!==(request.method==='POST'))return Response.json({detail:'Method not allowed'},{status:405})
  const base=(process.env.CARDIOLENS_API_URL || 'http://127.0.0.1:8000').replace(/\/$/,'')
  try{
    const upstream=await fetch(`${base}/${endpoint}`,{method:request.method,headers:request.method==='POST'?{'Content-Type':'application/json'}:undefined,
      body:request.method==='POST'?await request.text():undefined,cache:'no-store',signal:AbortSignal.timeout(12000)})
    return new Response(await upstream.text(),{status:upstream.status,headers:{'Content-Type':'application/json','Cache-Control':'no-store'}})
  }catch{return Response.json({detail:'CardioLens backend is unavailable. Start the API and try again.'},{status:503,headers:{'Cache-Control':'no-store'}})}
}
export const GET=proxy
export const POST=proxy
