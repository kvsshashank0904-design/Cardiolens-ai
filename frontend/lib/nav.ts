import {
  Activity,
  FlaskConical,
  Info,
  LayoutGrid,
  ScanLine,
  ShieldCheck,
  type LucideIcon,
} from 'lucide-react'

export type NavItem = {
  href: string
  label: string
  icon: LucideIcon
  index: string
}

export const navItems: NavItem[] = [
  { href: '/', label: 'Dashboard', icon: LayoutGrid, index: '01' },
  { href: '/assessment', label: 'Assessment', icon: ScanLine, index: '02' },
  { href: '/results', label: 'Prediction Results', icon: Activity, index: '03' },
  { href: '/model-lab', label: 'Model Lab', icon: FlaskConical, index: '04' },
  { href: '/data-integrity', label: 'Data Integrity', icon: ShieldCheck, index: '05' },
  { href: '/about', label: 'About', icon: Info, index: '06' },
]
