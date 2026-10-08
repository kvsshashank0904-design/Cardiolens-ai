import { cn } from '@/lib/utils'

export function Panel({
  className,
  glass = false,
  children,
  ...props
}: React.ComponentProps<'section'> & { glass?: boolean }) {
  return (
    <section
      className={cn(
        'relative rounded-xl border border-border',
        glass ? 'glass shadow-[0_0_0_1px_oklch(0.83_0.12_205/0.06),0_24px_60px_-30px_oklch(0.83_0.12_205/0.25)]' : 'bg-panel',
        className,
      )}
      {...props}
    >
      {children}
    </section>
  )
}

export function PanelHeader({
  eyebrow,
  title,
  description,
  action,
  className,
  titleId,
}: {
  eyebrow?: string
  title: string
  description?: React.ReactNode
  action?: React.ReactNode
  className?: string
  titleId?: string
}) {
  return (
    <header className={cn('flex flex-wrap items-start justify-between gap-3 border-b border-border px-5 py-4', className)}>
      <div className="min-w-0">
        {eyebrow && (
          <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground/80">{eyebrow}</p>
        )}
        <h2 id={titleId} className="mt-1 text-sm font-medium text-foreground text-pretty">
          {title}
        </h2>
        {description && <p className="mt-1 text-xs leading-relaxed text-muted-foreground">{description}</p>}
      </div>
      {action}
    </header>
  )
}

export function PanelBody({ className, ...props }: React.ComponentProps<'div'>) {
  return <div className={cn('p-5', className)} {...props} />
}
