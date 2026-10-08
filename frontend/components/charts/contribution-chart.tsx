import type { FeatureContribution } from '@/lib/research-data'
import { cn } from '@/lib/utils'

function roundUpHalf(n: number) {
  return Math.max(0.5, Math.ceil(n * 2) / 2)
}

function formatSigned(n: number) {
  return `${n >= 0 ? '+' : '−'}${Math.abs(n).toFixed(2)}`
}

export function ContributionChart({ data }: { data: FeatureContribution[] }) {
  const sorted = [...data].sort((a, b) => Math.abs(b.value) - Math.abs(a.value))
  const posMax = roundUpHalf(Math.max(0, ...data.map((d) => d.value)))
  const negMax = roundUpHalf(Math.max(0, ...data.map((d) => -d.value)))
  const span = posMax + negMax
  const zeroPct = (negMax / span) * 100

  const ticks: number[] = []
  for (let t = -negMax; t <= posMax + 1e-9; t += 0.5) ticks.push(Number(t.toFixed(2)))

  return (
    <figure>
      <figcaption className="sr-only">
        Feature contributions toward the disease-present class, sorted by magnitude:{' '}
        {sorted.map((d) => `${d.feature} ${formatSigned(d.value)}`).join(', ')}.
      </figcaption>

      <div aria-hidden className="grid grid-cols-[minmax(0,1fr)] gap-y-1 md:grid-cols-[10rem_minmax(0,1fr)_4.5rem] md:gap-x-4">
        <div className="hidden md:block" />
        <div className="relative mb-2 flex justify-between font-mono text-[10px] text-muted-foreground">
          <span className="text-negative">← toward disease-absent</span>
          <span className="text-positive">toward disease-present →</span>
        </div>
        <div className="hidden md:block" />

        {sorted.map((d) => {
          const widthPct = (Math.abs(d.value) / span) * 100
          const positive = d.value >= 0
          return (
            <div key={d.key} className="group contents">
              <div className="flex items-baseline justify-between pt-3 md:block md:pt-0 md:self-center">
                <span className="text-sm text-foreground">{d.feature}</span>
                <span className="ml-2 font-mono text-[10px] text-muted-foreground md:ml-0 md:block">{d.key}</span>
                <span className={cn('font-mono text-xs tabular md:hidden', positive ? 'text-positive' : 'text-negative')}>
                  {formatSigned(d.value)}
                </span>
              </div>

              <div className="relative h-9 rounded-md transition-colors group-hover:bg-secondary/40">
                {ticks.map((t) => (
                  <span
                    key={t}
                    className={cn('absolute inset-y-0 w-px', t === 0 ? 'bg-foreground/30' : 'bg-border')}
                    style={{ left: `${((t + negMax) / span) * 100}%` }}
                  />
                ))}
                <span
                  className={cn(
                    'absolute top-1/2 h-4 -translate-y-1/2',
                    positive
                      ? 'rounded-r-sm bg-gradient-to-r from-positive/50 to-positive shadow-[0_0_14px_-2px] shadow-positive/50'
                      : 'rounded-l-sm bg-gradient-to-l from-negative/50 to-negative',
                  )}
                  style={
                    positive
                      ? { left: `${zeroPct}%`, width: `${widthPct}%` }
                      : { left: `${zeroPct - widthPct}%`, width: `${widthPct}%` }
                  }
                />
              </div>

              <div
                className={cn(
                  'hidden self-center text-right font-mono text-sm tabular md:block',
                  positive ? 'text-positive' : 'text-negative',
                )}
              >
                {formatSigned(d.value)}
              </div>
            </div>
          )
        })}

        <div className="hidden md:block" />
        <div className="relative mt-2 h-4 font-mono text-[10px] text-muted-foreground">
          {ticks.map((t) => (
            <span
              key={t}
              className="absolute -translate-x-1/2 tabular"
              style={{ left: `${((t + negMax) / span) * 100}%` }}
            >
              {t === 0 ? '0' : t.toFixed(1)}
            </span>
          ))}
        </div>
        <div className="hidden md:block" />
      </div>
    </figure>
  )
}
