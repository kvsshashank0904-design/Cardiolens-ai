# CardioLens AI

Educational ML research prototype with the canonical v0 dashboard, real FastAPI predictions, and a frozen corrected-label Logistic Regression model. This is not a diagnostic system or clinically validated tool.

- [Frontend setup and checks](frontend/README.md)
- [Integration report](frontend/INTEGRATION_REPORT.md)
- [Verification and integrity evidence](frontend/verification/integrity.json)
- [Backend contract and setup](backend/README.md)
- [Dataset provenance](outputs/dataset_investigation/dataset_provenance_report.md)
- [Frozen corrected-label experiment](outputs/corrected_label_baseline/corrected_label_report.md)

The frontend preserves the supplied dashboard design and calls `/health`, `/model-info`, and `/predict`. No mock prediction fallback is used. Results remain in temporary memory only.

The `outputs/` directory contains unchanged historical research evidence and frozen model artifacts. The original external CSV and local virtual environments are not bundled. Some historical reproduction records reference their original filesystem paths. Starting the application requires no experiment rerun.

Use the pinned backend requirements and frontend npm lockfile. The original ZIP's pnpm metadata is retained for traceability; npm is the tested installation workflow. Refer to frontend instructions for local startup and verification.
