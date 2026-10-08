'use client'
import { usePrediction } from '@/lib/prediction-state'
import { Panel, PanelBody } from '@/components/lab/panel'
import Link from 'next/link'
import { ArrowLeft, Download } from 'lucide-react'
import { PageHeader } from '@/components/lab/page-header'
import { ResearchDisclaimer } from '@/components/lab/research-disclaimer'
import { ContributionsPanel } from '@/components/results/contributions-panel'
import { ExplanationPanel } from '@/components/results/explanation-panel'
import { ResultSummary } from '@/components/results/result-summary'
import { TechnicalDetails } from '@/components/results/technical-details'
import { Button } from '@/components/ui/button'



export default function ResultsPage() {
  const {result:r,status,error}=usePrediction()
  return (
    <>
      <PageHeader
        index="03"
        section="Prediction Results"
        title="Model output & attribution"
        description="Real backend result showing the model’s classification, its estimated probability, and the statistical contribution of each input feature."
        actions={
          <>
            <Button variant="outline" size="sm" render={<Link href="/assessment" />} nativeButton={false}>
              <ArrowLeft aria-hidden /> New assessment
            </Button>
            <Button variant="secondary" size="sm" disabled>
              <Download aria-hidden /> Export report
            </Button>
          </>
        }
      />

      {!r ? <Panel><PanelBody><p role={error ? 'alert' : 'status'}>{status==='loading'?'Running the frozen model…':error || 'No prediction yet. Complete an assessment to view a real model result.'}</p></PanelBody></Panel> : <>
      <div className="grid gap-5 lg:grid-cols-[22rem_minmax(0,1fr)]">
        <ResultSummary r={r} />
        <ExplanationPanel r={r} />
      </div>

      <div className="mt-5">
        <ContributionsPanel r={r} />
      </div>

      <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <TechnicalDetails r={r} />
        <ResearchDisclaimer className="self-start" />
      </div>
      </>}
    </>
  )
}
