import Link from 'next/link'

export function Logo() {
  return (
    <Link href="/" className="flex items-center gap-3 rounded-md outline-none focus-visible:ring-2 focus-visible:ring-ring">
      <span className="relative flex size-8 items-center justify-center rounded-md border border-primary/30 bg-primary/10">
        <svg viewBox="0 0 24 24" className="size-4 text-primary" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden>
          <circle cx="12" cy="12" r="8.5" opacity="0.45" />
          <path d="M3.5 12h4l2-4 3 8 2-4h6" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </span>
      <span className="flex flex-col leading-none">
        <span className="text-sm font-semibold tracking-tight">CardioLens AI</span>
        <span className="mt-1 font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">
          Research Prototype
        </span>
      </span>
    </Link>
  )
}
