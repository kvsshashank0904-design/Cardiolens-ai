import {test,expect,type Page} from '@playwright/test'
import {readFileSync,mkdirSync} from 'node:fs'
import {resolve} from 'node:path'
import {parsePrediction,inputFromForm,featureNames} from '../lib/api'

const fixture=JSON.parse(readFileSync(resolve('../backend/example_request.json'),'utf8'))
const shots=resolve('../work/frontend-integration/screenshots');mkdirSync(shots,{recursive:true})
async function fill(page:Page,values:Record<string,number>){
  for(const [key,value] of Object.entries(values)){
    const field=page.locator(`[name="${key}"]`)
    if(['sex','fbs','exang'].includes(key))await page.locator(`[name="${key}"][value="${value}"]`).check({force:true})
    else if(['cp','restecg','slope','ca','thal'].includes(key))await field.selectOption(String(value))
    else await field.fill(String(value))
  }
}
test('real prediction, exact payload, probability, contributions, refresh clears memory',async({page,request})=>{
  const direct=await request.post('http://127.0.0.1:8007/predict',{data:fixture});expect(direct.ok()).toBeTruthy()
  const reference=await direct.json();parsePrediction(reference)
  await page.goto('/assessment');await fill(page,fixture)
  const sent=page.waitForRequest(r=>r.url().endsWith('/predict')&&r.method()==='POST')
  await page.getByRole('button',{name:'Run assessment'}).click()
  const submitted=(await sent).postDataJSON();expect(Object.keys(submitted)).toEqual([...featureNames]);expect(submitted).toEqual(fixture)
  await expect(page).toHaveURL(/\/results$/)
  await expect(page.getByRole('heading',{name:reference.prediction_label,exact:true})).toBeVisible()
  await expect(page.getByRole('img',{name:new RegExp(`Estimated model probability ${(reference.model_probability*100).toFixed(1)}`)})).toBeVisible()
  await expect(page.getByText('Top 6 transformed terms')).toBeVisible()
  await expect(page.getByText('numeric__age',{exact:true})).toHaveCount(reference.explanation.feature_contributions.sort((a:any,b:any)=>Math.abs(b.contribution)-Math.abs(a.contribution)).slice(0,6).some((c:any)=>c.feature==='numeric__age')?1:0)
  await page.screenshot({path:resolve(shots,'integrated-results-desktop.png'),fullPage:true})
  await page.setViewportSize({width:390,height:844});await page.screenshot({path:resolve(shots,'integrated-results-mobile.png'),fullPage:true})
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBeTruthy()
  expect(await page.evaluate(()=>localStorage.length+sessionStorage.length)).toBe(0)
  await page.reload();await expect(page.getByText('No prediction yet. Complete an assessment to view a real model result.')).toBeVisible()
})
test('missing codes remain 4 and 0 and real backend reports both',async({page})=>{
  await page.goto('/assessment');await fill(page,{...fixture,ca:4,thal:0})
  const response=page.waitForResponse(r=>r.url().endsWith('/predict'))
  await page.getByRole('button',{name:'Run assessment'}).click()
  const r=await response;expect(r.request().postDataJSON().ca).toBe(4);expect(r.request().postDataJSON().thal).toBe(0)
  expect((await r.json()).missing_features).toEqual(['ca','thal'])
  await expect(page).toHaveURL(/\/results$/);await expect(page.getByText('ca, thal',{exact:true})).toBeVisible()
})
test('invalid age blocked before inference',async({page})=>{
  let calls=0;page.on('request',r=>{if(r.url().endsWith('/predict'))calls++})
  await page.goto('/assessment');await page.locator('#age').fill('10');await page.getByRole('button',{name:'Run assessment'}).click()
  expect(await page.locator('#age').evaluate((e:HTMLInputElement)=>e.validity.rangeUnderflow)).toBeTruthy();expect(calls).toBe(0)
  const form=new FormData();Object.entries({...fixture,age:10}).forEach(([k,v])=>form.set(k,String(v)));expect(()=>inputFromForm(form)).toThrow()
})
test('offline error no fallback and error visible in results',async({page})=>{
  await page.route('**/api/cardiolens/predict',r=>r.abort('connectionrefused'))
  await page.goto('/assessment');await page.getByRole('button',{name:'Run assessment'}).click()
  await expect(page.locator('main').getByRole('alert')).toHaveText('CardioLens backend is unavailable. Start the API and try again.')
  await page.getByRole('link',{name:'Prediction Results'}).first().click();await expect(page.locator('main').getByRole('alert')).toContainText('backend is unavailable')
  await expect(page.getByRole('img',{name:/Estimated model probability/})).toHaveCount(0)
})
for(const invalid of ['malformed','missing-contributions','incomplete-contributions'])test(`reject ${invalid} API response`,async({page,request})=>{
  const live=await(await request.post('http://127.0.0.1:8007/predict',{data:fixture})).json()
  if(invalid==='missing-contributions')delete live.explanation.feature_contributions
  if(invalid==='incomplete-contributions')live.explanation.feature_contributions.pop()
  await page.route('**/api/cardiolens/predict',r=>r.fulfill({status:200,contentType:'application/json',body:invalid==='malformed'?'{broken':JSON.stringify(live)}))
  await page.goto('/assessment');await page.getByRole('button',{name:'Run assessment'}).click()
  await expect(page.locator('main').getByRole('alert')).toContainText('Invalid response')
  await page.getByRole('link',{name:'Prediction Results'}).first().click();await expect(page.locator('main').getByRole('alert')).toContainText('Invalid response')
  await expect(page.getByRole('img',{name:/Estimated model probability/})).toHaveCount(0)
})
test('all routes render and desktop/mobile screenshots',async({page})=>{
  const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message))
  for(const width of [1440,390]){
    await page.setViewportSize({width,height:width===390?844:1000})
    for(const path of ['/','/assessment','/results','/model-lab','/data-integrity','/about']){
      await page.goto(path);await expect(page.locator('main h1')).toBeVisible()
      expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBeTruthy()
      await page.screenshot({path:resolve(shots,`integrated-${path.slice(1)||'dashboard'}-${width}.png`),fullPage:true})
    }
  }
  expect(errors).toEqual([])
})
