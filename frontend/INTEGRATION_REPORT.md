# Canonical frontend integration report

Completed 2026-10-08. The supplied v0 ZIP remains the visual source of truth. The existing FastAPI service and frozen Experiment 3 explicit-missing Logistic Regression model power the interface. No training or experiment reruns were performed.

## Inspection and changes

Inspected the ZIP app routes, components, theme, layout, research fixtures, package/configuration files; backend API implementation, contract, example request, tests, model metadata and frozen experiment reports/metrics/predictions. The existing GitHub repository contained only its initial README and LICENSE.

The following canonical files changed (all other canonical files are byte-identical, as recorded in verification/integrity.json):

- `app/about/page.tsx`
- `app/data-integrity/page.tsx`
- `app/layout.tsx`
- `app/model-lab/page.tsx`
- `app/page.tsx`
- `app/results/page.tsx`
- `components/assessment/assessment-form.tsx`
- `components/charts/probability-dial.tsx`
- `components/charts/roc-curve.tsx`
- `components/results/contributions-panel.tsx`
- `components/results/explanation-panel.tsx`
- `components/results/result-summary.tsx`
- `components/results/technical-details.tsx`
- `components/shell/sidebar.tsx`
- `lib/research-data.ts`
- `next.config.mjs`
- `package.json`

New implementation files: `lib/api.ts`, `lib/prediction-state.tsx`, `lib/input-contract.json`, `lib/verified-research.json`, `scripts/export-research.py`, `app/api/cardiolens/[endpoint]/route.ts`, `.env.example`, `package-lock.json`, `playwright.config.ts`, `tests/integration.spec.ts`, this report, README and verification evidence. Next.js also generates its standard type declarations during builds.

## API and explanation

The centralized client calls health, model-info and predict through a same-origin Next.js proxy. The server-only upstream is configurable. Exactly 13 numeric fields are sent in the required order; dataset codes ca=4 and thal=0 pass through unchanged. Human labels identify these as not recorded in the source dataset. The backend retains all preprocessing.

The client validates returned model identity, threshold, probability/class consistency, all 30 finite named contribution terms, additive log-odds and sigmoid consistency. Results use the actual response, including probability, interpretation, missing features, metadata and contribution magnitudes. The chart shows the six strongest transformed terms; its displayed net refers only to those terms. Explanations describe model behavior, not medical causes. No fallback predictions exist.

React context holds one temporary result in memory. Reload clears it. Empty, loading, error and invalid-response states are explicit. No assessment is placed in URL parameters or persistent browser storage. The canonical analytics component was removed to avoid unsolicited telemetry; it had no visual output.

## Visual preservation

The original colors, Geist fonts, CSS, navigation, layout structure, cards, chart styling and responsive behavior remain recognizable. Global CSS, shell layout, mobile navigation, logo, form field components and contribution chart are unchanged. Necessary copy updates replace fixtures with verified results, corrected codes, truthful units and connection states. Real text may wrap differently from short fixtures. Screenshots in verification provide the original and integrated comparisons.

## Verification

- TypeScript check passed after integration and test additions.
- Production build passed for all six routes and the API proxy. An initial sandboxed attempt could not download the original Google fonts; the network-enabled build succeeded without replacing fonts.
- Existing backend suite: 31 passed; one existing Starlette/httpx deprecation warning.
- Browser suite: 8 passed, zero skipped/flaky/failed. Covers real API parity, exact request fields, displayed result, refresh clearing state, ca=4/thal=0, unsupported age, simulated network unavailability, malformed responses, missing/incomplete contributions, and all six routes at desktop/mobile widths.
- An initial browser run found overly broad test alert selectors (including the Next.js route announcer); selectors were scoped to page content, then all tests passed.
- No horizontal overflow or uncaught page errors in route checks. Offline behavior was tested through browser network failure simulation, not by terminating a user service.
- All 130 pre-existing protected backend/output files match their before-integration SHA-256 values. The source CSV remains unchanged. Full before/after hashes are in verification/integrity.json.
- Frozen model SHA-256: `d5cc8dede683857a725976f578f08f81740e9d975ecc38efa5826a15f93d7344`.

## Limits and remaining work

This is a local educational prototype, not a clinical diagnostic system. The shared holdout was previously inspected; feature groups are not verified independent patients. Dataset acquisition history and certain units remain unresolved. Corrected positive means disease presence according to the documented UCI record mapping. The Model Lab distinguishes development CV from exploratory shared-holdout results.

No public deployment, authentication or production security hardening is included. The original font setup needs Google font access when building. Browser tests currently require installed Microsoft Edge and backend/frontend test ports 8007/3007. The preserved pnpm metadata belongs to the supplied ZIP; use npm ci and package-lock.json for this verified integration. Frozen historical reports may contain original absolute workspace paths; see their reproduction instructions before trying to rerun experiments. No experiment needs rerunning to start the application.
