import { KeyValueList } from '@/components/lab/tag'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import type { ResultView } from '@/lib/research-data'

export function TechnicalDetails({r}:{r:ResultView}) {
  return (
    <Panel aria-labelledby="tech-title">
      <PanelHeader titleId="tech-title" eyebrow="Provenance" title="Technical model details" />
      <PanelBody className="grid gap-x-10 gap-y-2 py-2 md:grid-cols-2">
        <KeyValueList
          items={[
            { label: 'View identifier', value: r.id },
            { label: 'Received (browser time)', value: r.timestamp },
            { label: 'Model version', value: r.modelVersion },
            { label: 'Model family', value: r.response.model.name },
            { label: 'Output', value: 'Binary class probability' },
          ]}
        />
        <KeyValueList
          items={[
            { label: 'Raw probability', value: r.probability.toFixed(3) },
            { label: 'Decision threshold', value: r.threshold.toFixed(2) },
            { label: 'Attribution method', value: r.explainer },
            { label: 'Attribution space', value: 'Model output (log-odds)' },
            { label: 'Preprocessing', value: r.response.model.preprocessing },
            { label: 'Intercept / log-odds', value: `${r.response.explanation.intercept.toFixed(4)} / ${r.response.explanation.log_odds.toFixed(4)}` },
            { label: 'Missing source values', value: r.response.missing_features.join(', ') || 'None' },
            { label: 'Contribution terms', value: String(r.contributions.length) },
          ]}
        />
      </PanelBody>
    </Panel>
  )
}
