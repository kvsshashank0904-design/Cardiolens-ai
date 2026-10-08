'use client'

import Link from 'next/link'
import { usePrediction } from '@/lib/prediction-state'
import { usePathname } from 'next/navigation'
import { navItems } from '@/lib/nav'
import { cn } from '@/lib/utils'
import { Logo } from './logo'

export function isActivePath(pathname: string, href: string) {
  return href === '/' ? pathname === '/' : pathname.startsWith(href)
}

export function Sidebar() {
  const {connection}=usePrediction()
  const pathname = usePathname()

  return (
    <aside className="sticky top-0 hidden h-dvh w-64 shrink-0 flex-col border-r border-sidebar-border bg-sidebar/80 backdrop-blur-sm lg:flex">
      <div className="px-5 pt-6 pb-8">
        <Logo />
      </div>

      <nav aria-label="Primary" className="flex-1 px-3">
        <p className="px-3 pb-3 font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground/70">
          Workspace
        </p>
        <ul className="flex flex-col gap-0.5">
          {navItems.map((item) => {
            const active = isActivePath(pathname, item.href)
            const Icon = item.icon
            return (
              <li key={item.href}>
                <Link
                  href={item.href}
                  aria-current={active ? 'page' : undefined}
                  className={cn(
                    'group relative flex items-center gap-3 rounded-md px-3 py-2 text-sm transition-colors outline-none focus-visible:ring-2 focus-visible:ring-ring',
                    active
                      ? 'bg-sidebar-accent text-foreground'
                      : 'text-muted-foreground hover:bg-sidebar-accent/60 hover:text-foreground',
                  )}
                >
                  {active && (
                    <span aria-hidden className="absolute inset-y-2 left-0 w-px bg-primary shadow-[0_0_8px] shadow-primary" />
                  )}
                  <Icon className={cn('size-4', active ? 'text-primary' : 'text-muted-foreground/80')} aria-hidden />
                  <span className="flex-1">{item.label}</span>
                  <span className="font-mono text-[10px] text-muted-foreground/50">{item.index}</span>
                </Link>
              </li>
            )
          })}
        </ul>
      </nav>

      <div className="m-3 rounded-lg border border-sidebar-border p-4">
        <div className="flex items-center gap-2">
          <span className="relative flex size-2">
            <span className="absolute inline-flex size-full animate-ping rounded-full bg-primary/50" />
            <span className="relative inline-flex size-2 rounded-full bg-primary" />
          </span>
          <span className="font-mono text-[11px] text-foreground/90">{connection === 'connected' ? 'Backend connected' : connection === 'checking' ? 'Checking backend' : 'Backend unavailable'}</span>
        </div>
        <p className="mt-2 text-xs leading-relaxed text-muted-foreground">
          Frozen Experiment 3 model. Predictions use the real API; research use only.
        </p>
      </div>
    </aside>
  )
}
