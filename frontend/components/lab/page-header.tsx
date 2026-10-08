export function PageHeader({
  index,
  section,
  title,
  description,
  actions,
}: {
  index: string
  section: string
  title: string
  description?: string
  actions?: React.ReactNode
}) {
  return (
    <div className="mb-8 flex flex-col gap-5 md:flex-row md:items-end md:justify-between">
      <div className="max-w-2xl">
        <p className="flex items-center gap-2 font-mono text-[11px] uppercase tracking-[0.2em] text-muted-foreground">
          <span className="text-primary">{index}</span>
          <span aria-hidden className="h-px w-6 bg-border" />
          {section}
        </p>
        <h1 className="mt-3 text-3xl font-semibold tracking-tight text-balance md:text-4xl">{title}</h1>
        {description && <p className="mt-3 text-sm leading-relaxed text-muted-foreground text-pretty">{description}</p>}
      </div>
      {actions && <div className="flex flex-wrap gap-2">{actions}</div>}
    </div>
  )
}
