import { defineConfig } from '@playwright/test'
export default defineConfig({testDir:'./tests',timeout:60000,workers:1,
  outputDir:'../work/frontend-integration/test-results',
  reporter:[['list'],['json',{outputFile:'../work/frontend-integration/browser-tests.json'}]],
  use:{baseURL:process.env.TEST_FRONTEND_URL || 'http://127.0.0.1:3007',channel:'msedge',headless:true,viewport:{width:1440,height:1000}}})
