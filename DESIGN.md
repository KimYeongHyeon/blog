# CV Design System

## 1. Atmosphere & Identity

A quiet academic dossier: readable, restrained, and easy to scan. The signature is a right-side table-of-contents island that keeps long CV pages navigable without competing with the content.

## 2. Color

### Palette

| Role | Token | Light | Dark | Usage |
|------|-------|-------|------|-------|
| Surface/primary | `--theme` | PaperMod theme variable | PaperMod theme variable | Main page background |
| Surface/elevated | `--entry` | PaperMod theme variable | PaperMod theme variable | Floating ToC island |
| Surface/subtle | `--code-bg` | PaperMod theme variable | PaperMod theme variable | Inline panels and code surfaces |
| Text/primary | `--primary` | PaperMod theme variable | PaperMod theme variable | Headings and body text |
| Text/secondary | `--secondary` | PaperMod theme variable | PaperMod theme variable | Metadata and muted text |
| Border/default | `--border` | PaperMod theme variable | PaperMod theme variable | Dividers and ToC outline |

### Rules

- Use PaperMod theme variables rather than raw colors.
- Use borders and tonal shifts for hierarchy; avoid decorative color.

## 3. Typography

### Scale

| Level | Size | Weight | Line Height | Tracking | Usage |
|-------|------|--------|-------------|----------|-------|
| H1 | Theme default | 700 | Theme default | 0 | Page title |
| H2 | Theme default | 600 | Theme default | 0 | CV sections |
| H3 | Theme default | 600 | Theme default | 0 | Positions, awards, talks |
| Body | Theme default | 400 | 1.75 | 0 | CV content |
| Body/sm | 0.875rem | 400-500 | 1.45 | 0 | ToC and metadata |

### Font Stack

- Primary: PaperMod system font stack.
- Mono: PaperMod code font stack.

### Rules

- Keep the CV text compact but readable.
- Do not scale type with viewport width.

## 4. Spacing & Layout

### Base Unit

All spacing derives from a base of 4px.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight internal spacing |
| `--space-2` | 8px | Compact list spacing |
| `--space-3` | 12px | ToC inner padding |
| `--space-4` | 16px | Comfortable item spacing |
| `--space-6` | 24px | Page and panel spacing |
| `--space-8` | 32px | Section spacing |

### Grid

- Content width follows PaperMod `--main-width`.
- Floating ToC appears only when the viewport can provide a separate right rail.

### Rules

- Do not let navigation overlap the CV body.
- Keep mobile reading single-column.

## 5. Components

### Floating ToC Island

- **Structure**: PaperMod `.toc` rendered before `.post-content`.
- **Variants**: inline on narrow viewports, fixed right rail on desktop.
- **Spacing**: `--space-3`, `--space-4`, `--space-6`.
- **States**: hover, active, focus-visible.
- **Accessibility**: preserve semantic `<details>`, `<summary>`, and anchor links.
- **Motion**: color and transform transitions only.

## 6. Motion & Interaction

| Type | Duration | Easing | Usage |
|------|----------|--------|-------|
| Micro | 150ms | ease-out | ToC hover and active states |
| Standard | 220ms | ease-in-out | Surface transitions |

### Rules

- Animate `transform`, `opacity`, and color only.
- Respect `prefers-reduced-motion`.

## 7. Depth & Surface

### Strategy

Mixed, but restrained: borders for structure and a small shadow only for the desktop ToC island.

| Level | Value | Usage |
|-------|-------|-------|
| Subtle | `0 8px 28px rgb(0 0 0 / 0.08)` | Desktop ToC island |
