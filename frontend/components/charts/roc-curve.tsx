export function RocCurve({ points }: { points: [number, number][] }) {
  const w = 300
  const h = 220
  const pad = { l: 32, r: 10, t: 10, b: 28 }
  const iw = w - pad.l - pad.r
  const ih = h - pad.t - pad.b
  const x = (v: number) => pad.l + v * iw
  const y = (v: number) => pad.t + (1 - v) * ih
  const line = points.map(([fx, ty], i) => `${i === 0 ? 'M' : 'L'} ${x(fx)} ${y(ty)}`).join(' ')
  const area = `${line} L ${x(1)} ${y(0)} L ${x(0)} ${y(0)} Z`
  const grid = [0, 0.25, 0.5, 0.75, 1]

  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="h-auto w-full" role="img" aria-label="ROC curve from recorded Experiment 3 exploratory holdout predictions">
      <defs>
        <linearGradient id="roc-fill" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="var(--positive)" stopOpacity={0.22} />
          <stop offset="100%" stopColor="var(--positive)" stopOpacity={0} />
        </linearGradient>
      </defs>
      {grid.map((g) => (
        <g key={g}>
          <line x1={x(g)} x2={x(g)} y1={y(0)} y2={y(1)} stroke="var(--border)" />
          <line x1={x(0)} x2={x(1)} y1={y(g)} y2={y(g)} stroke="var(--border)" />
          <text x={x(g)} y={h - 10} textAnchor="middle" className="fill-muted-foreground font-mono" fontSize={8}>
            {g}
          </text>
          <text x={pad.l - 6} y={y(g) + 3} textAnchor="end" className="fill-muted-foreground font-mono" fontSize={8}>
            {g}
          </text>
        </g>
      ))}
      <line x1={x(0)} y1={y(0)} x2={x(1)} y2={y(1)} stroke="var(--muted-foreground)" strokeOpacity={0.5} strokeDasharray="3 4" />
      <path d={area} fill="url(#roc-fill)" />
      <path d={line} fill="none" stroke="var(--positive)" strokeWidth={1.75} strokeLinejoin="round" />
      <text x={x(0.5)} y={h} textAnchor="middle" className="fill-muted-foreground font-mono" fontSize={8}>
        False positive rate
      </text>
    </svg>
  )
}
