'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { navItems } from '@/lib/nav'
import { cn } from '@/lib/utils'
import { Logo } from './logo'
import { isActivePath } from './sidebar'

export function MobileNav() {
  const pathname = usePathname()

  return (
    <header className="sticky top-0 z-30 border-b border-border bg-background/85 backdrop-blur-md lg:hidden">
      <div className="flex items-center justify-between px-4 py-3">
        <Logo />
        <span className="rounded-full border border-warning/30 px-2 py-0.5 font-mono text-[10px] uppercase tracking-wider text-warning">
          Not for clinical use
        </span>
      </div>
      <nav aria-label="Primary" className="overflow-x-auto px-2 pb-2 [scrollbar-width:none]">
        <ul className="flex w-max gap-1">
          {navItems.map((item) => {
            const active = isActivePath(pathname, item.href)
            const Icon = item.icon
            return (
              <li key={item.href}>
                <Link
                  href={item.href}
                  aria-current={active ? 'page' : undefined}
                  className={cn(
                    'flex items-center gap-2 rounded-md px-3 py-1.5 text-xs whitespace-nowrap transition-colors',
                    active ? 'bg-secondary text-foreground' : 'text-muted-foreground hover:text-foreground',
                  )}
                >
                  <Icon className={cn('size-3.5', active && 'text-primary')} aria-hidden />
                  {item.label}
                </Link>
              </li>
            )
          })}
        </ul>
      </nav>
    </header>
  )
}
