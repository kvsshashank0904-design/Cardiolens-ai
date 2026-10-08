import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { Tag } from '@/components/lab/tag'
import { ATTRIBUTION_CAVEAT, type ResultView } from '@/lib/research-data'

const fmt = (n: number) => `${n >= 0 ? '+' : '−'}${Math.abs(n).toFixed(2)}`

export function ExplanationPanel({r}:{r:ResultView}) {
  const sorted = [...r.contributions].sort((a, b) => Math.abs(b.value) - Math.abs(a.value))
  const toward = sorted.filter((c) => c.value > 0)
  const away = sorted.filter((c) => c.value < 0)
  const strongest = sorted.slice(0, 2)

  return (
    <Panel aria-labelledby="why-title" className="flex flex-col">
      <PanelHeader
        titleId="why-title"
        eyebrow="Interpretation"
        title="Why did the model reach this result?"
        action={<Tag>Plain-language summary</Tag>}
      />
      <PanelBody className="flex flex-1 flex-col gap-6">
        <p className="text-base leading-relaxed text-foreground/90 text-pretty">
          {r.classification}, with an estimated model probability of {(r.probability * 100).toFixed(1)}% for the disease-present class.
          {' '}The largest absolute contributions were {strongest.map(c => `${c.feature} (${fmt(c.value)} log-odds)`).join(' and ')}.
          {' '}{r.response.explanation.interpretation}

        </p>

        <div className="grid gap-3 sm:grid-cols-2">
          <div className="rounded-lg border border-positive/20 bg-positive/[0.04] p-4">
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-positive">Largest positive terms</p>
            <ul className="mt-3 flex flex-col gap-2">
              {toward.slice(0,3).map((c) => (
                <li key={c.key} className="flex items-center justify-between text-sm">
                  <span>{c.feature}</span>
                  <span className="font-mono text-xs text-positive tabular">{fmt(c.value)}</span>
                </li>
              ))}
            </ul>
          </div>
          <div className="rounded-lg border border-negative/20 bg-negative/[0.04] p-4">
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-negative">Largest negative terms</p>
            <ul className="mt-3 flex flex-col gap-2">
              {away.slice(0,3).map((c) => (
                <li key={c.key} className="flex items-center justify-between text-sm">
                  <span>{c.feature}</span>
                  <span className="font-mono text-xs text-negative tabular">{fmt(c.value)}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <p className="mt-auto border-l-2 border-warning/50 pl-3 text-xs leading-relaxed text-muted-foreground">
          {r.response.disclaimer} {ATTRIBUTION_CAVEAT}
        </p>
      </PanelBody>
    </Panel>
  )
}
