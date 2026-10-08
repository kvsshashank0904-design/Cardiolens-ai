# Backend verification

Status: **PASS**

- 31 backend tests pass, including 61 saved Experiment 3 prediction parity cases
- Training/refit methods patched to fail during startup and requests; no calls occurred
- One joblib load per application lifespan; in-memory pipeline hash unchanged across predictions
- Feature order, explicit sentinel decoding, deterministic responses and log-odds explanation arithmetic verified
- Strict numeric/category validation, malformed payloads, loading failures and sanitized inference errors checked
- Actual Uvicorn loopback HTTP: health, model-info and deterministic predict pass
- Original CSV and all 104 pre-existing output files unchanged before and after verification

Warnings: Installed Starlette TestClient emits an httpx deprecation warning; all tests pass. This does not occur in model inference.

Errors: []

Only frozen-model inference was exercised. Saved test predictions were compatibility fixtures, not a new evaluation or tuning source. No models were trained, thresholds changed, preprocessing refitted, or frozen artifacts rewritten.

Initial setup encountered restricted ensurepip/temp-directory access. Dependencies were installed in a separate workspace environment via pip. An initial pytest run encountered temporary-directory permission errors in two failure-simulation tests; those tests now mock read failures and all 31 pass. The later complete test results and live-server checks are recorded here.

The service is a local research prototype. The verification server was stopped after its checks. This is not clinical validation, production hardening, or a new independent holdout evaluation.
