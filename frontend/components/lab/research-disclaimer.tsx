import { TriangleAlert } from 'lucide-react'
import { cn } from '@/lib/utils'

export function ResearchDisclaimer({ compact = false, className }: { compact?: boolean; className?: string }) {
  return (
    <aside
      aria-label="Research disclaimer"
      className={cn('flex gap-3 rounded-xl border border-warning/25 bg-warning/[0.05] p-4', className)}
    >
      <TriangleAlert className="mt-0.5 size-4 shrink-0 text-warning" aria-hidden />
      <div className="text-xs leading-relaxed text-muted-foreground">
        <p className="font-medium text-warning">Research prototype — not a medical device</p>
        <p className="mt-1">
          CardioLens AI is an interpretability research interface. Outputs are statistical model estimates and are not a
          diagnosis, clinical recommendation, or substitute for evaluation by a qualified clinician.
          {!compact &&
            ' Feature contributions describe how the model weighted its inputs; they do not identify medical causes. Do not use this interface to make decisions about any individual’s care.'}
        </p>
      </div>
    </aside>
  )
}
