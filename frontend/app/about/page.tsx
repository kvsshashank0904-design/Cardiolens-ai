import type { Metadata } from 'next'
import { PageHeader } from '@/components/lab/page-header'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { ResearchDisclaimer } from '@/components/lab/research-disclaimer'

export const metadata: Metadata = { title: 'About' }

const principles = [
  {
    title: 'Legibility over authority',
    body: 'Every output is paired with the attributions that produced it, so the model’s reasoning can be inspected rather than trusted.',
  },
  {
    title: 'Association, not causation',
    body: 'Attributions describe statistical patterns learned from training data. They do not identify the medical cause of any condition.',
  },
  {
    title: 'Explicit uncertainty',
    body: 'Probabilities are shown alongside the decision threshold and calibration status, and results are displayed only after a valid backend response.',
  },
]

const limitations = [
  'Based on 302 Cleveland-derived feature groups; patient independence and transformation/repetition history remain unresolved.',
  'Not externally validated and not calibrated for any clinical setting.',
  'Attribution methods have known failure modes with correlated features.',
  'Not a medical diagnosis; no clinical validity or patient-level generalization is established.',
]

export default function AboutPage() {
  return (
    <>
      <PageHeader
        index="06"
        section="About"
        title="About CardioLens AI"
        description="CardioLens AI is a research prototype exploring how interpretable machine learning can make cardiovascular classification models easier to inspect, question, and critique."
      />

      <div className="grid gap-5 md:grid-cols-3">
        {principles.map((p, i) => (
          <Panel key={p.title} className="p-5">
            <p className="font-mono text-[10px] text-primary">{String(i + 1).padStart(2, '0')}</p>
            <h2 className="mt-3 text-sm font-medium">{p.title}</h2>
            <p className="mt-2 text-xs leading-relaxed text-muted-foreground">{p.body}</p>
          </Panel>
        ))}
      </div>

      <div className="mt-5 grid gap-5 lg:grid-cols-2">
        <Panel aria-labelledby="lim-title">
          <PanelHeader titleId="lim-title" eyebrow="Scope" title="Known limitations" />
          <PanelBody>
            <ul className="flex flex-col gap-3">
              {limitations.map((l) => (
                <li key={l} className="flex gap-3 text-sm text-foreground/85">
                  <span aria-hidden className="mt-2 size-1 shrink-0 rounded-full bg-warning" />
                  {l}
                </li>
              ))}
            </ul>
          </PanelBody>
        </Panel>
        <ResearchDisclaimer className="self-start" />
      </div>
    </>
  )
}
