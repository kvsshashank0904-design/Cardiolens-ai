import { cn } from '@/lib/utils'

const control =
  'h-10 w-full rounded-md border border-input bg-background/60 px-3 text-sm text-foreground outline-none transition-colors placeholder:text-muted-foreground/60 hover:border-foreground/20 focus-visible:border-primary/60 focus-visible:ring-2 focus-visible:ring-ring/40'

function FieldShell({
  id,
  label,
  code,
  hint,
  children,
}: {
  id: string
  label: string
  code: string
  hint?: string
  children: React.ReactNode
}) {
  return (
    <div className="flex flex-col gap-1.5">
      <div className="flex items-baseline justify-between gap-2">
        <label htmlFor={id} className="text-sm text-foreground/90">
          {label}
        </label>
        <span className="font-mono text-[10px] text-muted-foreground/70">{code}</span>
      </div>
      {children}
      {hint && (
        <p id={`${id}-hint`} className="text-[11px] text-muted-foreground">
          {hint}
        </p>
      )}
    </div>
  )
}

export function NumberField({
  id,
  label,
  code,
  unit,
  hint,
  ...props
}: {
  id: string
  label: string
  code: string
  unit?: string
  hint?: string
} & Omit<React.ComponentProps<'input'>, 'id' | 'type'>) {
  return (
    <FieldShell id={id} label={label} code={code} hint={hint}>
      <div className="relative">
        <input
          id={id}
          name={code}
          type="number"
          inputMode="decimal"
          aria-describedby={hint ? `${id}-hint` : undefined}
          className={cn(control, 'tabular', unit && 'pr-16')}
          {...props}
        />
        {unit && (
          <span className="pointer-events-none absolute inset-y-0 right-3 flex items-center font-mono text-[11px] text-muted-foreground">
            {unit}
          </span>
        )}
      </div>
    </FieldShell>
  )
}

export function SelectField({
  id,
  label,
  code,
  options,
  hint,
  ...props
}: {
  id: string
  label: string
  code: string
  hint?: string
  options: { value: string; label: string }[]
} & Omit<React.ComponentProps<'select'>, 'id'>) {
  return (
    <FieldShell id={id} label={label} code={code} hint={hint}>
      <select id={id} name={code} className={cn(control, 'appearance-none bg-[length:12px] pr-8')} {...props}>
        {options.map((o) => (
          <option key={o.value} value={o.value} className="bg-popover">
            {o.label}
          </option>
        ))}
      </select>
    </FieldShell>
  )
}

export function SegmentedField({
  label,
  code,
  options,
  defaultValue,
}: {
  label: string
  code: string
  options: { value: string; label: string }[]
  defaultValue: string
}) {
  return (
    <fieldset className="flex flex-col gap-1.5">
      <div className="flex items-baseline justify-between gap-2">
        <legend className="text-sm text-foreground/90">{label}</legend>
        <span className="font-mono text-[10px] text-muted-foreground/70">{code}</span>
      </div>
      <div className="grid h-10 grid-flow-col auto-cols-fr gap-1 rounded-md border border-input bg-background/60 p-1">
        {options.map((o) => (
          <label
            key={o.value}
            className="flex cursor-pointer items-center justify-center rounded-sm text-xs text-muted-foreground transition-colors hover:text-foreground has-[:checked]:bg-secondary has-[:checked]:text-foreground has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-ring/40"
          >
            <input type="radio" name={code} value={o.value} defaultChecked={o.value === defaultValue} className="sr-only" />
            {o.label}
          </label>
        ))}
      </div>
    </fieldset>
  )
}
