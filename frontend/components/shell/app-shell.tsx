import { Sidebar } from './sidebar'
import { MobileNav } from './mobile-nav'

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="relative min-h-dvh lg:flex">
      <div aria-hidden className="pointer-events-none fixed inset-0 lab-grid opacity-60" />
      <div
        aria-hidden
        className="pointer-events-none fixed -top-40 left-1/3 h-96 w-[40rem] rounded-full bg-primary/[0.06] blur-3xl"
      />
      <Sidebar />
      <MobileNav />
      <main className="relative flex-1 min-w-0">
        <div className="mx-auto w-full max-w-7xl px-4 py-6 sm:px-6 lg:px-10 lg:py-10">{children}</div>
      </main>
    </div>
  )
}
