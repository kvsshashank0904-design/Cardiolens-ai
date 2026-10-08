'use client'
import { createContext, useContext, useEffect, useRef, useState } from 'react'
import { ApiError, health, modelInfo, predict, type PredictionInput } from './api'
import { resultView, type ResultView } from './research-data'

type State={status:'idle'|'loading'|'success'|'error'|'invalid';result:ResultView|null;error:string|null}
type Context=State&{connection:'checking'|'connected'|'unavailable';submit:(input:PredictionInput)=>Promise<boolean>;clear:()=>void}
const PredictionContext=createContext<Context|null>(null)
export function PredictionProvider({children}:{children:React.ReactNode}){
  const [state,setState]=useState<State>({status:'idle',result:null,error:null})
  const [connection,setConnection]=useState<Context['connection']>('checking')
  const generation=useRef(0)
  useEffect(()=>{let mounted=true;const check=()=>Promise.all([health(),modelInfo()]).then(()=>{if(mounted)setConnection('connected')}).catch(()=>{if(mounted)setConnection('unavailable')});void check();const timer=setInterval(check,30000);return()=>{mounted=false;clearInterval(timer)}},[])
  const submit=async(input:PredictionInput)=>{
    const current=++generation.current
    setState({status:'loading',result:null,error:null})
    try{
      const response=await predict(input)
      if(current!==generation.current)return false
      setState({status:'success',result:resultView(response),error:null});setConnection('connected');return true
    }catch(e){
      if(current!==generation.current)return false
      const error=e instanceof Error?e.message:'Request failed.'
      setState({status:e instanceof ApiError&&e.kind==='invalid'?'invalid':'error',result:null,error})
      return false
    }
  }
  const clear=()=>{generation.current++;setState({status:'idle',result:null,error:null})}
  return <PredictionContext.Provider value={{...state,connection,submit,clear}}>{children}</PredictionContext.Provider>
}
export function usePrediction(){const c=useContext(PredictionContext);if(!c)throw new Error('PredictionProvider required');return c}
