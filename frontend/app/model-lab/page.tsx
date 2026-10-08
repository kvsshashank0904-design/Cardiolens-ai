import type { Metadata } from 'next'
import research from '@/lib/verified-research.json'
import { RocCurve } from '@/components/charts/roc-curve'
import { PageHeader } from '@/components/lab/page-header'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { KeyValueList, Metric, Tag } from '@/components/lab/tag'

export const metadata: Metadata = { title: 'Model Lab' }

const rocPoints = research.roc_points as [number,number][]
const runs = research.runs.map(r=>({id:r.id,model:r.model,auc:`${r.cv.roc_auc.mean.toFixed(4)} ± ${r.cv.roc_auc.sd.toFixed(4)}`,status:r.status}))
const heldout=research.lr_test.distinct_group

export default function ModelLabPage() {
  return (
    <>
      <PageHeader
        index="04"
        section="Model Lab"
        title="Model configuration & evaluation"
        description="Frozen Experiment 3 results: held-out exploratory evaluation on 61 feature groups, previously inspected. Development cross-validation is shown separately in the run history. No clinical validation."
        actions={<Tag tone="warning">Recorded evidence</Tag>}
      />

      <Panel glass>
        <dl className="grid grid-cols-2 gap-6 p-5 md:grid-cols-5 md:p-6">
          <Metric label="ROC AUC" value={heldout.roc_auc.toFixed(4)} />
          <Metric label="Accuracy" value={heldout.accuracy.toFixed(4)} />
          <Metric label="Sensitivity" value={heldout.sensitivity.toFixed(4)} />
          <Metric label="Specificity" value={heldout.specificity.toFixed(4)} />
          <Metric label="F1" value={heldout.f1.toFixed(4)} />
        </dl>
      </Panel>

      <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <Panel aria-labelledby="roc-title">
          <PanelHeader
            titleId="roc-title"
            eyebrow="Evaluation"
            title="ROC curve — shared exploratory holdout"
            description="Derived from saved Experiment 3 predictions; 61 groups, counted once. Dashed line marks chance."
            action={<Tag tone="warning">Saved predictions</Tag>}
          />
          <PanelBody>
            <RocCurve points={rocPoints} />
          </PanelBody>
        </Panel>

        <Panel aria-labelledby="card-title">
          <PanelHeader titleId="card-title" eyebrow="Model card" title="Experiment 3 · frozen logistic" />
          <PanelBody className="py-2">
            <KeyValueList
              items={[
                { label: 'Family', value: 'Logistic Regression' },
                { label: 'Regularization', value: 'L2, C=1' },
                { label: 'Development / held-out', value: '241 / 61 groups' },
                { label: 'Decision threshold', value: '0.5' },
                { label: 'Validation', value: 'Five saved group-separated folds' },
                { label: 'Explainer', value: 'Logistic log-odds contributions' },
                { label: 'Intended use', value: 'Research only' },
              ]}
            />
          </PanelBody>
        </Panel>
      </div>

      <Panel aria-labelledby="runs-title" className="mt-5 overflow-hidden">
        <PanelHeader titleId="runs-title" eyebrow="Experiments" title="Development Cross-Validation — run history" action={<Tag tone="warning">Saved predictions</Tag>} />
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-border text-left font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">
                <th scope="col" className="px-5 py-3 font-normal">Run</th>
                <th scope="col" className="px-5 py-3 font-normal">Model</th>
                <th scope="col" className="px-5 py-3 text-right font-normal">CV AUC mean ± SD</th>
                <th scope="col" className="px-5 py-3 text-right font-normal">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border">
              {runs.map((run) => (
                <tr key={run.id} className="transition-colors hover:bg-secondary/30">
                  <td className="px-5 py-3 font-mono text-xs">{run.id}</td>
                  <td className="px-5 py-3">{run.model}</td>
                  <td className="px-5 py-3 text-right font-mono text-xs tabular">{run.auc}</td>
                  <td className="px-5 py-3 text-right">
                    <Tag tone={run.status === 'Frozen baseline' ? 'primary' : 'neutral'}>{run.status}</Tag>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Panel>
      <p className="mt-5 text-xs leading-relaxed text-muted-foreground">Development logistic sensitivity: {research.lr_cv.sensitivity.mean.toFixed(4)} ± {research.lr_cv.sensitivity.sd.toFixed(4)} (fold sample SD). Shared holdout confusion matrix: {JSON.stringify(heldout.confusion_matrix)} as [[TN, FP], [FN, TP]]; 28 positives and 33 negatives. Original-row-weighted view: 214 rows, sensitivity {research.lr_test.original_row_weighted.sensitivity.toFixed(4)}, AUC {research.lr_test.original_row_weighted.roc_auc.toFixed(4)}. Repetition is not independent evidence. Sources: frozen Experiment 3, 4 and 4B metrics; their checksums are recorded in the research export.</p>
    </>
  )
}
