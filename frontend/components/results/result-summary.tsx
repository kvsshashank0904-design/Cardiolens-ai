import { ProbabilityDial } from '@/components/charts/probability-dial'
import { Panel } from '@/components/lab/panel'
import { Tag } from '@/components/lab/tag'
import type { ResultView } from '@/lib/research-data'

export function ResultSummary({r}:{r:ResultView}) {
  const margin = r.probability - r.threshold

  return (
    <Panel glass aria-labelledby="result-status" className="overflow-hidden">
      <div aria-hidden className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-primary/60 to-transparent" />
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-border px-5 py-4">
        <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground">Prediction status</p>
        <Tag tone="primary" dot>
          Inference complete
        </Tag>
      </div>

      <div className="flex flex-col items-center px-5 pt-6 pb-2">
        <ProbabilityDial value={r.probability} threshold={r.threshold} />
      </div>

      <div className="px-5 pb-5 text-center">
        <h2 id="result-status" className="text-lg font-semibold tracking-tight text-balance">
          {r.classification}
        </h2>
        <p className="mt-1.5 text-xs leading-relaxed text-muted-foreground text-pretty">
          The model output is {Math.abs(margin * 100).toFixed(1)} percentage points {margin >= 0 ? 'at or above' : 'below'} its {(r.threshold * 100).toFixed(0)}% threshold.
          {' '}{r.response.probability_definition}

        </p>
      </div>

      <dl className="grid grid-cols-3 divide-x divide-border border-t border-border">
        {[
          { label: 'Run', value: r.id },
          { label: 'Threshold', value: r.threshold.toFixed(2) },
          { label: 'Margin', value: `${margin >= 0 ? '+' : ''}${margin.toFixed(3)}` },
        ].map((item) => (
          <div key={item.label} className="px-3 py-3 text-center">
            <dt className="font-mono text-[9px] uppercase tracking-[0.18em] text-muted-foreground">{item.label}</dt>
            <dd className="mt-1 truncate font-mono text-xs text-foreground tabular">{item.value}</dd>
          </div>
        ))}
      </dl>
    </Panel>
  )
}
