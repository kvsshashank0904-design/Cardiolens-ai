# CardioLens canonical frontend

Educational interface integrated with the existing frozen FastAPI model. Read [the integration report](INTEGRATION_REPORT.md) and [verification evidence](verification/integrity.json).

## Run locally

Use Node 22 and Python 3.12.10. From the repository root, in one terminal:

```powershell
python -m venv work/backend-env
work/backend-env/Scripts/python.exe -m pip install -r backend/requirements.txt
work/backend-env/Scripts/python.exe -B -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

In another terminal:

```powershell
cd frontend
npm ci
npm run dev
```

Open http://localhost:3000. For a production build use `npm run build` then `npm start`. The original Geist font build requires network access to Google Fonts. No model training is needed.

The browser defaults to `/api/cardiolens`. The Next.js proxy defaults to http://127.0.0.1:8000. Set server-only `CARDIOLENS_API_URL` in `.env.local` if your backend address differs; see `.env.example`. Optional `NEXT_PUBLIC_API_URL` bypasses the proxy and requires appropriate backend CORS. Never commit local environment secrets.

## Checks

From frontend: `npx tsc --noEmit` and `npm run build`.

From the repository root:

```powershell
work/backend-env/Scripts/python.exe -B -m pytest backend/tests -q -p no:cacheprovider -p no:tmpdir
```

Some frozen integrity checks reference the original local CSV path. Preserve that CSV and its documented hash; consult backend documentation before using another machine.

For browser tests, start the backend on 8007 and the production frontend on 3007 with `CARDIOLENS_API_URL=http://127.0.0.1:8007`. From frontend run `npx playwright test`. Microsoft Edge must be installed. Test reports/screenshots go to `../work/frontend-integration/`. The committed verification directory is the completed integration evidence; later test runs do not overwrite it.

`python scripts/export-research.py` refreshes the frontend aggregate research JSON and contract only from existing frozen files. It neither trains nor evaluates a model. This is not required for startup.

## Behavior

All six supplied routes are retained. Assessment sends the exact 13-feature contract to the real backend. Results exist only in memory and disappear on refresh. Offline/invalid responses show errors without substitute predictions. ca=4 and thal=0 retain their original API codes and are described as missing in the source dataset. Contributions are the model's transformed-feature terms, not causal explanations.

Recorded research uses corrected disease-presence labels, feature-group separation and a previously inspected holdout. It establishes neither clinical validity nor patient independence. This repository is an educational research prototype.
