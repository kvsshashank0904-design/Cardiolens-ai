const SWEEP = 270
const START = 135

function polar(cx: number, cy: number, r: number, deg: number) {
  const rad = (deg * Math.PI) / 180
  return { x: cx + r * Math.cos(rad), y: cy + r * Math.sin(rad) }
}

function arcPath(cx: number, cy: number, r: number, from: number, to: number) {
  const a = polar(cx, cy, r, from)
  const b = polar(cx, cy, r, to)
  const large = to - from > 180 ? 1 : 0
  return `M ${a.x} ${a.y} A ${r} ${r} 0 ${large} 1 ${b.x} ${b.y}`
}

export function ProbabilityDial({
  value,
  threshold,
  size = 220,
}: {
  value: number
  threshold: number
  size?: number
}) {
  const c = 100
  const r = 82
  const end = START + SWEEP * value
  const thresholdDeg = START + SWEEP * threshold
  const tIn = polar(c, c, r - 10, thresholdDeg)
  const tOut = polar(c, c, r + 10, thresholdDeg)
  const ticks = Array.from({ length: 28 }, (_, i) => START + (SWEEP / 27) * i)

  return (
    <div className="relative" style={{ width: size, height: size }}>
      <svg
        viewBox="0 0 200 200"
        className="size-full"
        role="img"
        aria-label={`Estimated model probability ${(value * 100).toFixed(1)} percent; decision threshold ${(threshold * 100).toFixed(0)} percent`}
      >
        <defs>
          <linearGradient id="dial-grad" x1="0" y1="1" x2="1" y2="0">
            <stop offset="0%" stopColor="var(--negative)" />
            <stop offset="100%" stopColor="var(--positive)" />
          </linearGradient>
          <filter id="dial-glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" />
          </filter>
        </defs>

        {ticks.map((deg) => {
          const a = polar(c, c, 96, deg)
          const b = polar(c, c, 99, deg)
          return (
            <line key={deg} x1={a.x} y1={a.y} x2={b.x} y2={b.y} stroke="var(--muted-foreground)" strokeOpacity={0.35} strokeWidth={1} />
          )
        })}

        <path d={arcPath(c, c, r, START, START + SWEEP)} stroke="var(--border)" strokeWidth={10} fill="none" strokeLinecap="round" />
        <path d={arcPath(c, c, r, START, end)} stroke="url(#dial-grad)" strokeWidth={10} fill="none" strokeLinecap="round" opacity={0.45} filter="url(#dial-glow)" />
        <path d={arcPath(c, c, r, START, end)} stroke="url(#dial-grad)" strokeWidth={10} fill="none" strokeLinecap="round" />

        <line x1={tIn.x} y1={tIn.y} x2={tOut.x} y2={tOut.y} stroke="var(--foreground)" strokeWidth={1.5} />
      </svg>

      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground">Estimated model probability</span>
        <span className="mt-1 text-5xl font-semibold tracking-tight tabular">
          {(value * 100).toFixed(1)}
          <span className="text-2xl text-muted-foreground">%</span>
        </span>
        <span className="mt-1 font-mono text-[10px] text-muted-foreground">
          threshold {threshold.toFixed(2)}
        </span>
      </div>
    </div>
  )
}
