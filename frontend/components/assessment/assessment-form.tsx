'use client'

import { useRouter } from 'next/navigation'
import { useState } from 'react'
import { inputFromForm } from '@/lib/api'
import { usePrediction } from '@/lib/prediction-state'
import { ArrowRight, RotateCcw } from 'lucide-react'
import { Panel, PanelBody, PanelHeader } from '@/components/lab/panel'
import { Tag } from '@/components/lab/tag'
import { Button } from '@/components/ui/button'
import { NumberField, SegmentedField, SelectField } from './fields'

export function AssessmentForm() {
  const router = useRouter()
  const {status, error, submit, clear} = usePrediction()
  const [inputError, setInputError] = useState<string|null>(null)
  const pending = status === 'loading'

  return (
    <form
      className="flex flex-col gap-5"
      onReset={() => {clear();setInputError(null)}}
      onSubmit={async (e) => {
        e.preventDefault()
        if(pending)return
        setInputError(null)
        try {
          const payload=inputFromForm(new FormData(e.currentTarget))
          if(await submit(payload))router.push('/results')
        } catch(err) {clear();setInputError(err instanceof Error?err.message:'Check the input fields.')}
      }}
    >
      <Panel aria-labelledby="demo-title">
        <PanelHeader titleId="demo-title" eyebrow="Section A" title="Demographics" />
        <PanelBody className="grid gap-5 sm:grid-cols-2">
          <NumberField id="age" label="Age" code="age" unit="years" min={29} max={77} defaultValue={54} required />
          <SegmentedField
            label="Sex"
            code="sex"
            defaultValue="1"
            options={[
              { value: '1', label: 'Male' },
              { value: '0', label: 'Female' },
            ]}
          />
        </PanelBody>
      </Panel>

      <Panel aria-labelledby="clin-title">
        <PanelHeader titleId="clin-title" eyebrow="Section B" title="Resting measurements" />
        <PanelBody className="grid gap-5 sm:grid-cols-2">
          <NumberField id="trestbps" label="Resting blood pressure" code="trestbps" unit="mm Hg" min={94} max={200} defaultValue={130} required />
          <NumberField id="chol" label="Serum cholesterol" code="chol" unit="mg/dl" min={126} max={564} defaultValue={246} required />
          <SegmentedField
            label="Fasting blood sugar > 120 mg/dl"
            code="fbs"
            defaultValue="0"
            options={[
              { value: '0', label: 'No' },
              { value: '1', label: 'Yes' },
            ]}
          />
          <SelectField
            id="restecg"
            label="Resting ECG"
            code="restecg"
            defaultValue="0"
            options={[
              { value: '0', label: 'Left ventricular hypertrophy' },
              { value: '1', label: 'Normal' },
              { value: '2', label: 'ST-T wave abnormality' },
            ]}
          />
        </PanelBody>
      </Panel>

      <Panel aria-labelledby="ex-title">
        <PanelHeader titleId="ex-title" eyebrow="Section C" title="Symptoms & exercise testing" />
        <PanelBody className="grid gap-5 sm:grid-cols-2">
          <SelectField
            id="cp"
            label="Chest pain type"
            code="cp"
            defaultValue="0"
            options={[
              { value: '0', label: 'Asymptomatic' },
              { value: '1', label: 'Atypical angina' },
              { value: '2', label: 'Non-anginal pain' },
              { value: '3', label: 'Typical angina' },
            ]}
          />
          <NumberField id="thalach" label="Maximum heart rate" code="thalach" hint="Unit not confirmed in source documentation" min={71} max={202} defaultValue={150} required />
          <SegmentedField
            label="Exercise-induced angina"
            code="exang"
            defaultValue="0"
            options={[
              { value: '0', label: 'No' },
              { value: '1', label: 'Yes' },
            ]}
          />
          <NumberField
            id="oldpeak"
            label="ST depression (Oldpeak)"
            code="oldpeak"
            unit=""
            step={0.1}
            min={0}
            max={6.2}
            defaultValue={1.0}
            hint="Relative to rest; unit not confirmed in source documentation"
            required
          />
          <SelectField
            id="slope"
            label="Peak exercise ST slope"
            code="slope"
            defaultValue="1"
            options={[
              { value: '0', label: 'Downsloping' },
              { value: '1', label: 'Flat' },
              { value: '2', label: 'Upsloping' },
            ]}
          />
          <SelectField
            id="ca"
            label="Major vessels (fluoroscopy)"
            code="ca"
            defaultValue="0"
            options={[...['0', '1', '2', '3'].map((v) => ({ value: v, label: v })), {value:'4',label:'Not recorded in source dataset'}]}
          />
          <SelectField
            id="thal"
            label="Thal defect status"
            code="thal"
            defaultValue="2"
            options={[
              { value: '0', label: 'Not recorded in source dataset' },
              { value: '1', label: 'Fixed defect' },
              { value: '2', label: 'Normal' },
              { value: '3', label: 'Reversible defect' },
            ]}
          />
        </PanelBody>
      </Panel>

      {(inputError || error) && <p role="alert" className="rounded-xl border border-warning/30 bg-panel p-4 text-sm text-warning">{inputError || error}</p>}
      <div className="flex flex-col-reverse items-stretch justify-between gap-3 rounded-xl border border-border bg-panel p-4 sm:flex-row sm:items-center">
        <div className="flex items-center gap-2 text-xs text-muted-foreground">
          <Tag tone="warning">Research only</Tag>
          Frozen Experiment 3. Supported ranges are not clinical validity ranges.
        </div>
        <div className="flex gap-2">
          <Button type="reset" variant="ghost" disabled={pending}>
            <RotateCcw aria-hidden /> Reset
          </Button>
          <Button type="submit" disabled={pending}>
            {pending ? 'Running…' : 'Run assessment'} <ArrowRight aria-hidden />
          </Button>
        </div>
      </div>
    </form>
  )
}
