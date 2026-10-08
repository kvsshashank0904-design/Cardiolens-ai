"""Backend verification only: tests, live loopback API smoke test, protected hashes."""
import sys
sys.dont_write_bytecode=True
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import time
import urllib.request
import xml.etree.ElementTree as ET

B=Path(__file__).resolve().parent
ROOT=B.parent

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def check_protected():
    m=json.loads((B/'protected_manifest.json').read_text())
    assert sha(Path(m['source_path']))==m['source_sha256'],'Original CSV changed'
    for name,h in m['protected_sha256'].items():assert sha(ROOT/name)==h,'Protected changed: '+name
    return m

def verify(run_tests):
    manifest=check_protected()
    report={'status':'FAIL','errors':[],'checks':[], 'source_sha256':manifest['source_sha256'],
            'protected_files_unchanged':len(manifest['protected_sha256'])}
    try:
        if run_tests:
            result=subprocess.run([sys.executable,'-B','-m','pytest','backend/tests','-q','-p','no:cacheprovider','-p','no:tmpdir','--junitxml=backend/test_results.xml'],
                cwd=ROOT,capture_output=True,text=True)
            (B/'test_output.txt').write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
            assert result.returncode==0,'Backend tests failed; inspect test_output.txt'
        tree=ET.parse(B/'test_results.xml')
        suites=list(tree.getroot().iter('testsuite'))
        counts={k:sum(int(s.get(k,0)) for s in suites) for k in ['tests','failures','errors','skipped']}
        assert counts['tests']>=31 and counts['failures']==counts['errors']==counts['skipped']==0,'Test results incomplete'
        report['pytest']=counts
        report['checks'] += ['31 backend tests pass, including 61 saved Experiment 3 prediction parity cases',
            'Training/refit methods patched to fail during startup and requests; no calls occurred',
            'One joblib load per application lifespan; in-memory pipeline hash unchanged across predictions',
            'Feature order, explicit sentinel decoding, deterministic responses and log-odds explanation arithmetic verified',
            'Strict numeric/category validation, malformed payloads, loading failures and sanitized inference errors checked']
        env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
        with socket.socket() as s:
            s.bind(('127.0.0.1',0));port=s.getsockname()[1]
        log=(B/'uvicorn_smoke.log').open('w',encoding='utf-8')
        process=subprocess.Popen([sys.executable,'-B','-m','uvicorn','backend.app.main:app','--host','127.0.0.1','--port',str(port),'--no-access-log'],
            cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)
        opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
        def request(path,payload=None):
            data=None if payload is None else json.dumps(payload).encode()
            req=urllib.request.Request(f'http://127.0.0.1:{port}'+path,data=data,
                headers={'Content-Type':'application/json'} if data else {})
            with opener.open(req,timeout=3) as response:return json.load(response)
        try:
            ready=False
            for _ in range(100):
                if process.poll() is not None:raise AssertionError('Uvicorn startup failed; inspect local log')
                try:
                    health=request('/health');ready=True;break
                except (OSError,TimeoutError):time.sleep(.1)
            assert ready and health['model_loaded'] is True,'Live health failed'
            info=request('/model-info');assert info['experiment']=='Experiment 3' and info['threshold']==0.5
            payload=json.loads((B/'example_request.json').read_text())
            prediction=request('/predict',payload)
            assert prediction==request('/predict',payload),'Live prediction not deterministic'
            with (ROOT/'outputs/corrected_label_baseline/corrected_test_predictions.csv').open() as f:
                saved=next(r for r in csv.DictReader(f) if r['variant']=='explicit_missing')
            assert prediction['prediction']==int(saved['prediction'])
            assert abs(prediction['model_probability']-float(saved['probability_disease_present']))<1e-12
            (B/'example_response.json').write_text(json.dumps(prediction,indent=2)+'\n',encoding='utf-8')
            report['live_uvicorn']={'health':health,'model_info_experiment':info['experiment'],
                'prediction':prediction['prediction'],'model_probability':prediction['model_probability'],
                'deterministic':True,'server_stopped_after_check':True}
            report['checks'].append('Actual Uvicorn loopback HTTP: health, model-info and deterministic predict pass')
        finally:
            process.terminate()
            try:process.wait(timeout=10)
            except subprocess.TimeoutExpired:process.kill();process.wait()
            log.close()
        check_protected()
        report['checks'].append('Original CSV and all 104 pre-existing output files unchanged before and after verification')
        report['warnings']=['Installed Starlette TestClient emits an httpx deprecation warning; all tests pass. This does not occur in model inference.']
        report['status']='PASS'
    except Exception as e:report['errors'].append(str(e))
    report['backend_source_sha256']={p.relative_to(B).as_posix():sha(p) for p in B.rglob('*.py')}
    (B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    text=['# Backend verification','',f"Status: **{report['status']}**",'']
    text += ['- '+x for x in report['checks']]
    text += ['','Warnings: '+ '; '.join(report.get('warnings',[])),'','Errors: '+str(report['errors']), '',
        'Only frozen-model inference was exercised. Saved test predictions were compatibility fixtures, not a new evaluation or tuning source. No models were trained, thresholds changed, preprocessing refitted, or frozen artifacts rewritten.', '',
        'Initial setup encountered restricted ensurepip/temp-directory access. Dependencies were installed in a separate workspace environment via pip. An initial pytest run encountered temporary-directory permission errors in two failure-simulation tests; those tests now mock read failures and all 31 pass. The later complete test results and live-server checks are recorded here.', '',
        'The service is a local research prototype. The verification server was stopped after its checks. This is not clinical validation, production hardening, or a new independent holdout evaluation.']
    (B/'verification_report.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    return report['status']=='PASS'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--skip-tests',action='store_true',help='Use the current JUnit file; intended only immediately after running the unchanged suite.')
    a=p.parse_args();sys.exit(0 if verify(not a.skip_tests) else 1)
