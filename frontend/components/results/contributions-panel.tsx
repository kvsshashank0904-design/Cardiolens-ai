import { ContributionChart } from '@/components/charts/contribution-chart'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { Tag } from '@/components/lab/tag'
import type { ResultView } from '@/lib/research-data'

export function ContributionsPanel({r}:{r:ResultView}) {
  const net = r.contributions.slice(0,6).reduce((s, c) => s + c.value, 0)

  return (
    <Panel aria-labelledby="contrib-title">
      <PanelHeader
        titleId="contrib-title"
        eyebrow="Feature attribution"
        title="Feature contribution profile"
        description="Actual additive contributions in log-odds units, sorted by magnitude. Positive values moved the output toward the disease-present class."
        action={
          <div className="flex flex-wrap gap-2">
            <Tag tone="primary">{r.explainer}</Tag>
            <Tag>Top 6 transformed terms</Tag>
          </div>
        }
      />
      <PanelBody>
        <ContributionChart data={r.contributions.slice(0,6)} />
      </PanelBody>
      <footer className="flex flex-wrap items-center gap-x-6 gap-y-2 border-t border-border px-5 py-3 font-mono text-[11px] text-muted-foreground">
        <span className="flex items-center gap-2">
          <span aria-hidden className="h-2 w-4 rounded-sm bg-positive" /> Toward disease-present
        </span>
        <span className="flex items-center gap-2">
          <span aria-hidden className="h-2 w-4 rounded-sm bg-negative" /> Toward disease-absent
        </span>
        <span className="ml-auto tabular">
          Net of shown features: <span className="text-foreground">{net >= 0 ? '+' : ''}{net.toFixed(2)}</span>
        </span>
      </footer>
    </Panel>
  )
}
