import type { Metadata } from 'next'
import { AssessmentForm } from '@/components/assessment/assessment-form'
import { PageHeader } from '@/components/lab/page-header'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { ResearchDisclaimer } from '@/components/lab/research-disclaimer'

export const metadata: Metadata = { title: 'Cardiovascular Assessment' }

const steps = [
  { label: 'Schema validation', detail: 'Types, ranges, required fields' },
  { label: 'Preprocessing', detail: 'Encoding & scaling (training-fit)' },
  { label: 'Inference', detail: 'Binary class probability' },
  { label: 'Attribution', detail: 'Per-feature contribution scores' },
  { label: 'Report', detail: 'Explanation & provenance' },
]

export default function AssessmentPage() {
  return (
    <>
      <PageHeader
        index="02"
        section="Cardiovascular Assessment"
        title="Input feature record"
        description="Enter a de-identified feature record using the 13-attribute schema. Values are passed to the model exactly as entered — no clinical interpretation is performed."
      />

      <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_20rem]">
        <AssessmentForm />

        <div className="flex flex-col gap-5 lg:sticky lg:top-10 lg:self-start">
          <Panel aria-labelledby="pipe-title">
            <PanelHeader titleId="pipe-title" eyebrow="Pipeline" title="What happens on submit" />
            <PanelBody>
              <ol className="relative flex flex-col gap-5 border-l border-border pl-5">
                {steps.map((s, i) => (
                  <li key={s.label} className="relative">
                    <span
                      aria-hidden
                      className="absolute top-1 -left-[25px] flex size-2 rounded-full border border-primary/60 bg-background"
                    />
                    <p className="font-mono text-[10px] text-muted-foreground">{String(i + 1).padStart(2, '0')}</p>
                    <p className="text-sm text-foreground">{s.label}</p>
                    <p className="text-xs text-muted-foreground">{s.detail}</p>
                  </li>
                ))}
              </ol>
            </PanelBody>
          </Panel>
          <ResearchDisclaimer compact />
        </div>
      </div>
    </>
  )
}
