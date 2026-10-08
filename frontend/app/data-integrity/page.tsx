import type { Metadata } from 'next'
import { Check, Minus } from 'lucide-react'
import { PageHeader } from '@/components/lab/page-header'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { Metric, Tag } from '@/components/lab/tag'

export const metadata: Metadata = { title: 'Data Integrity' }

const TOTAL = 302

const features = [
  { key: 'age', type: 'numeric', missing: 0 },
  { key: 'sex', type: 'binary', missing: 0 },
  { key: 'cp', type: 'categorical', missing: 0 },
  { key: 'trestbps', type: 'numeric', missing: 0 },
  { key: 'chol', type: 'numeric', missing: 0 },
  { key: 'fbs', type: 'binary', missing: 0 },
  { key: 'restecg', type: 'categorical', missing: 0 },
  { key: 'thalach', type: 'numeric', missing: 0 },
  { key: 'exang', type: 'binary', missing: 0 },
  { key: 'oldpeak', type: 'numeric', missing: 0 },
  { key: 'slope', type: 'categorical', missing: 0 },
  { key: 'ca', type: 'categorical', missing: 4 },
  { key: 'thal', type: 'categorical', missing: 2 },
]

const checks = [
  { label: 'Schema matches 13-attribute specification', pass: true },
  { label: 'API uses observed ranges, not clinical validity ranges', pass: true },
  { label: '723 repeated copies linked to 302 feature groups', pass: true },
  { label: 'Target column excluded from feature set', pass: true },
  { label: 'ca=4 / thal=0 decoded to explicit missing categories', pass: true },
  { label: 'External validation cohort', pass: false },
]

export default function DataIntegrityPage() {
  const absent = 164
  const present = TOTAL - absent

  return (
    <>
      <PageHeader
        index="05"
        section="Data Integrity"
        title="Dataset quality & validation"
        description="1,025 original rows, 302 distinct feature groups and 723 repeated copies. Same-group records stay together: 241 development groups and 61 held-out groups. Distinct groups are not established independent patients."
        actions={<Tag>Cleveland-derived · 302 groups</Tag>}
      />

      <Panel glass>
        <dl className="grid grid-cols-2 gap-6 p-5 md:grid-cols-4 md:p-6">
          <Metric label="Original rows" value="1,025" />
          <Metric label="Distinct groups" value={TOTAL} />
          <Metric label="Missing group cells" value="6" hint="ca: 4 · thal: 2" />
          <Metric label="Completeness" value={`${(100 - (6 / (TOTAL * 13)) * 100).toFixed(2)}%`} />
        </dl>
      </Panel>

      <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <Panel aria-labelledby="feat-title" className="overflow-hidden">
          <PanelHeader titleId="feat-title" eyebrow="Completeness" title="Per-feature coverage — distinct groups" />
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border text-left font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">
                  <th scope="col" className="px-5 py-3 font-normal">Feature</th>
                  <th scope="col" className="px-5 py-3 font-normal">Type</th>
                  <th scope="col" className="w-2/5 px-5 py-3 font-normal">Coverage</th>
                  <th scope="col" className="px-5 py-3 text-right font-normal">Missing</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {features.map((f) => {
                  const pct = ((TOTAL - f.missing) / TOTAL) * 100
                  return (
                    <tr key={f.key} className="transition-colors hover:bg-secondary/30">
                      <td className="px-5 py-2.5 font-mono text-xs">{f.key}</td>
                      <td className="px-5 py-2.5 text-xs text-muted-foreground">{f.type}</td>
                      <td className="px-5 py-2.5">
                        <div className="h-1.5 rounded-full bg-secondary" aria-label={`${pct.toFixed(1)}% complete`} role="img">
                          <div
                            className={f.missing ? 'h-full rounded-full bg-warning' : 'h-full rounded-full bg-primary/70'}
                            style={{ width: `${pct}%` }}
                          />
                        </div>
                      </td>
                      <td className="px-5 py-2.5 text-right font-mono text-xs tabular">
                        <span className={f.missing ? 'text-warning' : 'text-muted-foreground'}>{f.missing}</span>
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </Panel>

        <div className="flex flex-col gap-5">
          <Panel aria-labelledby="bal-title">
            <PanelHeader titleId="bal-title" eyebrow="Target" title="Class balance" />
            <PanelBody>
              <div className="flex h-3 overflow-hidden rounded-full" role="img" aria-label={`Disease absent ${absent}, disease present ${present}`}>
                <div className="bg-negative" style={{ width: `${(absent / TOTAL) * 100}%` }} />
                <div className="bg-positive" style={{ width: `${(present / TOTAL) * 100}%` }} />
              </div>
              <dl className="mt-4 grid grid-cols-2 gap-4 text-xs">
                <div>
                  <dt className="text-negative">Disease absent</dt>
                  <dd className="mt-1 font-mono text-lg text-foreground tabular">
                    {absent} <span className="text-xs text-muted-foreground">{((absent / TOTAL) * 100).toFixed(1)}%</span>
                  </dd>
                </div>
                <div>
                  <dt className="text-positive">Disease present</dt>
                  <dd className="mt-1 font-mono text-lg text-foreground tabular">
                    {present} <span className="text-xs text-muted-foreground">{((present / TOTAL) * 100).toFixed(1)}%</span>
                  </dd>
                </div>
              </dl>
            </PanelBody>
          </Panel>

          <Panel aria-labelledby="checks-title">
            <PanelHeader titleId="checks-title" eyebrow="Safeguards" title="Validation checks" />
            <PanelBody className="py-3">
              <ul className="flex flex-col gap-3">
                {checks.map((c) => (
                  <li key={c.label} className="flex gap-3 text-xs">
                    <span
                      className={
                        c.pass
                          ? 'flex size-4 shrink-0 items-center justify-center rounded-full bg-primary/15 text-primary'
                          : 'flex size-4 shrink-0 items-center justify-center rounded-full bg-warning/15 text-warning'
                      }
                    >
                      {c.pass ? <Check className="size-3" aria-hidden /> : <Minus className="size-3" aria-hidden />}
                    </span>
                    <span className={c.pass ? 'text-foreground/85' : 'text-muted-foreground'}>
                      {c.label}
                      <span className="sr-only">{c.pass ? ' — passed' : ' — not yet available'}</span>
                    </span>
                  </li>
                ))}
              </ul>
            </PanelBody>
          </Panel>
        </div>
      </div>
      <p className="mt-5 text-xs leading-relaxed text-muted-foreground">Corrected disease_present = 1 − original_target: local target=1 matches UCI absence; target=0 matches UCI presence. ca=4 and thal=0 mean “Not recorded in source dataset,” affecting 4 and 2 groups (18 and 7 original rows). The source CSV is unchanged. File/version match and record correspondence are verified; acquisition route, transformation/repetition rationale and patient independence remain unresolved.</p>
    </>
  )
}
