'use client'

import Link from 'next/link'
import { ArrowRight, ArrowUpRight } from 'lucide-react'
import { PageHeader } from '@/components/lab/page-header'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { ResearchDisclaimer } from '@/components/lab/research-disclaimer'
import { Metric, Tag } from '@/components/lab/tag'
import { Button } from '@/components/ui/button'
import { usePrediction } from '@/lib/prediction-state'

const log = [
  { time: 'Exp 3', text: 'Frozen corrected-label logistic baseline; real API inference' },
  { time: 'Audit', text: '302 distinct feature groups; patient independence unresolved' },
  { time: 'Method', text: 'Additive frozen logistic contributions in log-odds units' },
  { time: 'Scope', text: 'Research prototype; not a medical diagnosis' },
]

const quickLinks = [
  { href: '/model-lab', title: 'Model Lab', body: 'Configuration, evaluation layout, experiment runs.' },
  { href: '/data-integrity', title: 'Data Integrity', body: 'Schema, completeness, and class balance checks.' },
  { href: '/about', title: 'About this project', body: 'Scope, limitations, and responsible-use notes.' },
]

export default function DashboardPage() {
  const {result:r,connection}=usePrediction()
  const top = r?.contributions.slice(0,3) || []
  const pipeline=[{label:'Dataset audit',status:'Recorded'},{label:'Integrity checks',status:'Recorded'},{label:'API model',status:connection},{label:'Explainer',status:'Frozen coefficients'},{label:'Reporting',status:r?'Real result':'Awaiting assessment'}]

  return (
    <>
      <PageHeader
        index="01"
        section="Dashboard"
        title="Interpretable cardiovascular ML workspace"
        description="A research interface for inspecting how a classification model weighs cardiovascular features — built to make model behaviour legible, not to make clinical decisions."
        actions={
          <Button render={<Link href="/assessment" />} nativeButton={false}>
            New assessment <ArrowRight aria-hidden />
          </Button>
        }
      />

      <Panel glass className="overflow-hidden">
        <div aria-hidden className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-primary/60 to-transparent" />
        <dl className="grid grid-cols-2 gap-6 p-5 md:grid-cols-4 md:p-6">
          <Metric label="Latest probability" value={r ? `${(r.probability * 100).toFixed(1)}%` : '—'} hint="Estimated model probability" />
          <Metric label="Decision threshold" value={r ? r.threshold.toFixed(2) : '0.50'} hint="Binary classifier" />
          <Metric label="Input attributes" value="13" hint="Cleveland schema" />
          <Metric label="Model version" value={<span className="font-mono text-lg">{r?.modelVersion || 'Experiment 3'}</span>} hint="Frozen logistic baseline" />
        </dl>
      </Panel>

      <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <Panel aria-labelledby="latest-title">
          <PanelHeader
            titleId="latest-title"
            eyebrow="Latest result"
            title={r?.classification || 'No prediction yet'}
            description={r ? `Received ${r.timestamp}` : 'Complete an assessment to see real model output.'}
            action={
              <Button variant="outline" size="sm" render={<Link href="/results" />} nativeButton={false}>
                Open <ArrowUpRight aria-hidden />
              </Button>
            }
          />
          <PanelBody>
            <p className="font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">
              Strongest attributions
            </p>
            <ul className="mt-4 flex flex-col gap-4">
              {top.map((c) => {
                const pct = (Math.abs(c.value) / (Math.abs(top[0].value) || 1)) * 100
                return (
                  <li key={c.key}>
                    <div className="flex items-baseline justify-between text-sm">
                      <span>{c.feature}</span>
                      <span className={`font-mono text-xs tabular ${c.value >= 0 ? 'text-positive' : 'text-negative'}`}>{c.value >= 0 ? '+' : ''}{c.value.toFixed(2)}</span>
                    </div>
                    <div className="mt-2 h-1.5 rounded-full bg-secondary">
                      <div className={`h-full rounded-full bg-gradient-to-r ${c.value >= 0 ? 'from-positive/40 to-positive' : 'from-negative/40 to-negative'}`} style={{ width: `${pct}%` }} />
                    </div>
                  </li>
                )
              })}
            </ul>
          </PanelBody>
        </Panel>

        <Panel aria-labelledby="pipeline-title">
          <PanelHeader titleId="pipeline-title" eyebrow="System" title="Pipeline status" />
          <PanelBody className="py-2">
            <ul className="divide-y divide-border">
              {pipeline.map((p) => (
                <li key={p.label} className="flex items-center justify-between py-3 text-sm">
                  <span className="text-foreground/90">{p.label}</span>
                  <Tag tone={p.status === 'unavailable' || p.status === 'checking' ? 'warning' : 'primary'} dot>
                    {p.status}
                  </Tag>
                </li>
              ))}
            </ul>
          </PanelBody>
        </Panel>
      </div>

      <div className="mt-5 grid gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
        <div className="grid gap-5 sm:grid-cols-3">
          {quickLinks.map((q) => (
            <Link
              key={q.href}
              href={q.href}
              className="group rounded-xl border border-border bg-panel p-5 transition-colors outline-none hover:border-primary/30 focus-visible:ring-2 focus-visible:ring-ring"
            >
              <div className="flex items-center justify-between">
                <h2 className="text-sm font-medium">{q.title}</h2>
                <ArrowUpRight className="size-4 text-muted-foreground transition-colors group-hover:text-primary" aria-hidden />
              </div>
              <p className="mt-2 text-xs leading-relaxed text-muted-foreground">{q.body}</p>
            </Link>
          ))}
        </div>

        <Panel aria-labelledby="log-title">
          <PanelHeader titleId="log-title" eyebrow="Activity" title="Research log" />
          <PanelBody className="py-3">
            <ol className="flex flex-col gap-3">
              {log.map((l) => (
                <li key={l.time} className="flex gap-3 text-xs">
                  <span className="font-mono text-muted-foreground tabular">{l.time}</span>
                  <span className="text-foreground/85">{l.text}</span>
                </li>
              ))}
            </ol>
          </PanelBody>
        </Panel>
      </div>

      <ResearchDisclaimer className="mt-5" />
    </>
  )
}
