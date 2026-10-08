import { cn } from '@/lib/utils'

const tones = {
  neutral: 'border-border text-muted-foreground',
  primary: 'border-primary/30 bg-primary/10 text-primary',
  negative: 'border-negative/30 bg-negative/10 text-negative',
  warning: 'border-warning/30 bg-warning/10 text-warning',
} as const

export function Tag({
  tone = 'neutral',
  dot = false,
  className,
  children,
}: {
  tone?: keyof typeof tones
  dot?: boolean
  className?: string
  children: React.ReactNode
}) {
  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 rounded-full border px-2 py-0.5 font-mono text-[10px] uppercase tracking-wider whitespace-nowrap',
        tones[tone],
        className,
      )}
    >
      {dot && <span aria-hidden className="size-1.5 rounded-full bg-current" />}
      {children}
    </span>
  )
}

export function Metric({
  label,
  value,
  hint,
  className,
}: {
  label: string
  value: React.ReactNode
  hint?: React.ReactNode
  className?: string
}) {
  return (
    <div className={cn('flex flex-col gap-1.5', className)}>
      <dt className="font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">{label}</dt>
      <dd className="text-2xl font-semibold tracking-tight tabular">{value}</dd>
      {hint && <dd className="text-xs text-muted-foreground">{hint}</dd>}
    </div>
  )
}

export function KeyValueList({ items }: { items: { label: string; value: React.ReactNode }[] }) {
  return (
    <dl className="divide-y divide-border">
      {items.map((item) => (
        <div key={item.label} className="flex items-baseline justify-between gap-4 py-2.5">
          <dt className="text-xs text-muted-foreground">{item.label}</dt>
          <dd className="text-right font-mono text-xs text-foreground/90">{item.value}</dd>
        </div>
      ))}
    </dl>
  )
}
