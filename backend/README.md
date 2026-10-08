# CardioLens AI backend

Local FastAPI research prototype using the **frozen Experiment 3 primary explicit-missing Logistic Regression pipeline**. No model training, refitting, model fallback, threshold selection or experiment mutation occurs in the API. No UI is included.

## Install and start

Use Python **3.12.10**. From the project root, create a separate environment and install the exact dependency pins:

```powershell
python -m venv work/backend-env
& work/backend-env/Scripts/python.exe -m pip install -r backend/requirements.txt
& work/backend-env/Scripts/python.exe -B -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

The current workspace already has the separate `work/backend-env` environment installed. In this environment ensurepip initially failed under filesystem restrictions; installation was completed with the existing pip using its `--python work/backend-env/Scripts/python.exe` option. Do not reinstall into the ML experiment environment.

API documentation: `http://127.0.0.1:8000/docs`. Stop with Ctrl+C. Bind remains loopback by default; authentication, internet deployment, CORS/frontend integration and production hardening are outside this phase. No input persistence or request-body logging is implemented.

## Frozen artifact and input contract

Exact artifact in this workspace:

`C:\Users\DELL\Documents\Codex\2026-09-27\we-are-building-cardiolens-ai-an\outputs\corrected_label_baseline\explicit_missing_model.joblib`

SHA-256: `d5cc8dede683857a725976f578f08f81740e9d975ecc38efa5826a15f93d7344`.

The path is resolved relative to this project, not the current working directory. `model_contract.json` records the identity, feature contract and exact ML runtime versions. The service checks the checksum before deserializing the same bytes and aborts startup on missing/corrupt/incompatible artifacts. There is no alternative model. Loading occurs once per application process through FastAPI lifespan. Multiple server workers would each load once.

Frozen reference: `outputs/corrected_label_baseline/corrected_label_report.md`, configuration, group manifest and prediction artifacts. The pipeline has StandardScaler numeric indices `[0,3,4,7,9]`; categorical indices `[1,2,5,6,8,10,11,12]`; constant missing fill `-1`; dense OneHotEncoder with unknown categories ignored and no category dropped; LogisticRegression L2/C=1/lbfgs/max_iter=2000/tol=0.0001/no class weights/seed=42. Its fitted state is reused unchanged.

Exact feature order:

`age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal`

All 13 fields are required. Request key order does not matter; the server builds the array in the above order. Extra fields, nulls, numeric strings, booleans, nonfinite numbers and unsupported codes are rejected with 422. Categorical fields require JSON integers (e.g. `1`, not `1.0`). Numeric fields accept JSON integers or finite decimal numbers.

| Field | Accepted input |
|---|---|
| age | number 29–77 |
| sex | integer 0 or 1 |
| cp | integer 0, 1, 2 or 3 |
| trestbps | number 94–200 |
| chol | number 126–564 |
| fbs | integer 0 or 1 |
| restecg | integer 0, 1 or 2 |
| thalach | number 71–202 |
| exang | integer 0 or 1 |
| oldpeak | number 0–6.2 |
| slope | integer 0, 1 or 2 |
| ca | integer 0–4; **4 means missing** |
| thal | integer 0–3; **0 means missing** |

These are the **local CSV codes**, not raw UCI codes. In particular cp=0 corresponds to the matched asymptomatic code; local thal=1 fixed defect, 2 normal, 3 reversible defect. Refer to `outputs/dataset_investigation/dataset_provenance_report.md` for the complete evidence-based dictionary and unresolved units. Do not substitute another dataset's mappings.

Numeric bounds are the original CSV's observed minimum/maximum values, explicitly adopted as this prototype's supported-input envelope. They are **not medically validated ranges**, nor a claim that values outside them are invalid measurements. Bounds do not alter accepted inputs or tune the model; the API rejects unsupported requests rather than extrapolating silently. Even an in-range combination may be unlike the training data.

Only ca=4 and thal=0 decode to NaN before the saved pipeline, exactly as in Experiment 3. The pipeline then maps missingness to its fitted explicit `-1` category. API callers must not send `-1`, null, NaN or ordinary-category substitutes. The response lists `missing_features` so this treatment is visible.

## Endpoints

- `GET /health`: loaded model status and service name. Startup failure prevents normal serving.
- `GET /model-info`: model/experiment/label metadata, threshold, feature order, supported values and disclaimer; no filesystem paths.
- `POST /predict`: strict request validation, frozen pipeline probability, thresholded prediction and basic log-odds explanation.

Example request (copied from a saved Experiment 3 test group for integration parity only):

```json
{
  "age": 51,
  "sex": 1,
  "cp": 0,
  "trestbps": 140,
  "chol": 261,
  "fbs": 0,
  "restecg": 0,
  "thalach": 186,
  "exang": 1,
  "oldpeak": 0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
```

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/predict -ContentType 'application/json' -Body (Get-Content backend/example_request.json -Raw)
```

This fixture's recorded probability is approximately `0.2805778528953151`, prediction `0`. `example_response.json` contains the complete actual response from the verified live server.

## Output and explanation

Corrected convention: `disease_present = 1-original_target = int(matched UCI num>0)`. Class 0 means UCI-mapped absence; class 1 means UCI-mapped presence. Prediction is **1 when model_probability >= 0.5**, otherwise 0. `model_probability` is the pipeline's probability for class 1, **not medically validated risk or confidence**.

The response contains `prediction`, `prediction_label`, `model_probability`, `probability_definition`, `model`, `explanation`, `missing_features` and `disclaimer`. Labels begin “Model prediction”; the disclaimer is “This is a research prototype and is not a medical diagnosis.”

Each explanation contribution is the actual transformed feature value multiplied by its frozen logistic coefficient. Names come from `get_feature_names_out`. The intercept plus all contributions equals the log-odds; its sigmoid is checked against the pipeline probability for every request. Values are in **log-odds units**, not percentage points, medical causes, independent feature effects or patient-specific advice. One-hot inactive terms can be zero; standardized numeric terms refer to the training mean. Nothing is fitted to produce explanations.

Validation errors include field locations and messages without echoing raw input. Missing/corrupt model startup produces a clear local error without a fallback. Inference failures return a generic 500 JSON message; no filesystem paths or tracebacks are exposed in API responses.

## Tests and verification

```powershell
& work/backend-env/Scripts/python.exe -B -m pytest backend/tests -q -p no:cacheprovider -p no:tmpdir --junitxml=backend/test_results.xml
& work/backend-env/Scripts/python.exe -B backend/verify_backend.py
```

Verification reruns backend tests only, launches a short-lived loopback Uvicorn server for actual HTTP checks, stops it, and writes `verification.json` and `verification_report.md`. It does not run any ML experiment. Tests compare all 61 saved primary Experiment 3 test-group predictions for invocation parity; they do not calculate new performance estimates or select settings. Tests block estimator fitting, check one-time loading, unchanged in-memory state, deterministic output, feature order, missing-code handling, error behavior and explanation arithmetic.

`protected_manifest.json` contains the original source hash and all **104** pre-existing output-file hashes (including Experiments 3, 4 and 4B). Verification checks them before and after. Source data is never an API runtime dependency. `requirements.txt` locks installed dependencies including test tools; `environment.json` records the runtime. Current TestClient emits an httpx deprecation warning; this is documented in verification output and does not prevent the tests or server from working.

## Files and limits

New code: `app/config.py`, `schemas.py`, `model_service.py`, `main.py`, routes and package initializers. New supporting files: tests, requirements/environment records, contract/protected manifests, example request/response, verifier, JUnit results, live-server log and verification report. No pre-existing project file is edited.

Dataset acquisition/transformation/repetition history, patient identities, missingness mechanism, one omitted UCI record and some units remain unresolved. The holdout was previously inspected; source duplicates are not independent patients. Frozen model performance is educational evidence, not clinical validation. Inputs and model outputs must not be presented as diagnosis or patient-specific medical advice.

Implementation references: [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/) for startup loading; [Pydantic strict types](https://docs.pydantic.dev/2.0/usage/types/strict_types/) for strict/finite validation. Project artifacts, rather than generic examples, determine the model contract.
