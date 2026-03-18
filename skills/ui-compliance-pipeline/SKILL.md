---
name: ui-compliance-pipeline
description: "This skill should be used when generating or modifying any UI/page/component. Enforce a mandatory, gate-based compliance pipeline: full spec ingestion, full component-matrix style parsing, component-library-only implementation, token/state/accessibility validation, and evidence-based delivery verdict."
---

# UI Compliance Pipeline Skill

## Purpose
Establish a strict UI delivery protocol that prevents partial alignment and enforces full consistency on:
- component source
- structure and naming
- token names and values
- style and layout
- interaction/state transitions
- accessibility and regression safety

## Mandatory Trigger
Run this skill before any of the following:
1. Generate a new page
2. Generate a new component
3. Modify existing UI styles, structure, naming, token usage, or interactions
4. Refactor UI/component implementation

## Hard Gating Rules (Non-Bypassable)
Apply these gates in order. Do not implement UI code before all required gates pass.

### Gate A: Full Component Spec Ingestion (Required for page generation)
Read **all** component docs under project `component_specs` folder (full files, not partial snippets).
Default project path:
- `/UXworkflow/component_specs/`

Execution requirements:
1. Discover all spec files in `component_specs`.
2. Read every spec file completely.
3. Build a normalized component constraints map (API, structure, variants, states, tokens, spacing/layout rules).
4. Record file coverage evidence (list of files read).

### Gate B: Full Component Matrix Style Ingestion (Required for page generation)
Read full component style source from:
- `/UXworkflow/component-matrix.html`

Execution requirements:
1. Read the full file.
2. Parse all component-related style blocks and naming conventions (class names, tokens, geometry, typography, spacing, states).
3. Build a style-token-layout mapping aligned to spec constraints.
4. Record coverage evidence that full matrix styles were ingested.

### Gate C: Component-Library-Only Composition (Required for page generation)
Generate page UI using **100% component-library components only**.

Strict constraints:
1. Use only documented components and documented variants from `component_specs` + `component-matrix`.
2. Keep canonical component naming, class naming, and token naming unchanged.
3. Keep style/layout values aligned to library definitions; do not invent ad-hoc styles.
4. Keep page composition as legal combinations of library components only.
5. If one-to-one exact component/variant match is unavailable, select the nearest legal component/variant from the library first.
6. If no acceptable approximate component exists, pause generation and ask user whether to continue and which continuation strategy to use; continue only after explicit user response.
7. Never fabricate unofficial components or bypass library constraints.

### Gate D: Matching Fallback and User Confirmation (Required)
Run fallback resolution before implementation when exact match is missing.

Execution requirements:
1. Evaluate exact match first.
2. If exact match fails, evaluate approximate candidates by structure, interaction, token compatibility, and layout deviation.
3. If approximate candidate exists, select best candidate and record rationale.
4. If no approximate candidate exists, stop output generation and ask user:
   - whether to continue
   - which strategy to continue with (for example: relax strictness, redesign requirement with existing components, or wait for new component definition)
5. Resume generation only after explicit user reply.
6. Record decision evidence in delivery report.

## Compliance Level
Default to **L4** for page generation unless user explicitly lowers it:
- L1: Visual approximation only
- L2: Visual + key structure
- L3: Visual + structure + token naming/value + state machine
- L4: L3 + accessibility + evidence report + regression checks (default for pages)

## Execution Workflow (Must Follow in Order)

### Step 1: Lock Scope and Acceptance Level
- Identify target page/components and required interaction scope.
- Set acceptance level (default L4 for page generation).
- Define verification radius (component-local or full-page regression).

### Step 2: Run Gate A (Full `component_specs` ingestion)
- Complete full-folder ingestion.
- Build the component constraints map.
- Block implementation if any spec file is unread.

### Step 3: Run Gate B (Full `component-matrix.html` ingestion)
- Complete full-file style parsing.
- Build class/token/layout/state mapping.
- Block implementation if matrix parsing is incomplete.

### Step 4: Build Acceptance Matrix
Create per-component checklist:
1. Component identity and legal variant
2. DOM/slot structure
3. Geometry (W/H/padding/gap/radius)
4. Typography (family/size/weight/line-height)
5. Token naming + value consistency
6. Asset source/semantics/size/color
7. States and event-driven transitions
8. Accessibility (ARIA, keyboard, focus, labels)
9. Regression impact

Do not implement before acceptance matrix is complete.

### Step 5: Implement with Library Lock
- Implement only with approved library components/variants.
- Preserve canonical naming and tokens.
- Preserve matrix-aligned layout and spacing.
- Reject custom one-off CSS/structure that bypasses component library constraints.

### Step 6: Validate State Machine and Interaction
- Validate entry, intermediate, and exit/cancel/clear/back transitions.
- Validate edge cases (empty input, blur timing, rapid actions, disabled/error paths).

### Step 7: Validate Accessibility and Regression
- Validate keyboard navigation and visible focus.
- Validate semantic roles/labels.
- Validate no unintended global token/style side effects.

### Step 8: Delivery Contract (Required)
Output must include:
1. What changed
2. Full spec ingestion evidence (`component_specs` file list)
3. Full matrix ingestion evidence (`component-matrix.html` coverage statement)
4. Acceptance matrix results (pass/fail per item)
5. Remaining risks or “none”
6. Final verdict:
   - “Fully compliant at Lx”
   - or “Not fully compliant, gaps: ...”

Never claim completion without evidence.

### Step 9: Mandatory Compliance Output Template (Required)
Use the following structure in every UI/page delivery. Do not omit sections.

```md
## Compliance Evidence Report

### 1) Scope
- Target page/component:
- Requested acceptance level:
- Effective acceptance level:

### 2) Spec Coverage Checklist (`component_specs` full ingestion)
- [ ] File 1: <path> (read: full)
- [ ] File 2: <path> (read: full)
- [ ] ...all files listed
- Coverage verdict: PASS | FAIL

### 3) Matrix Coverage Checklist (`component-matrix.html` full ingestion)
- Source file: /UXworkflow/component-matrix.html
- Read mode: full
- Parsed style domains:
  - [ ] component class naming
  - [ ] token naming/value
  - [ ] geometry/spacing/radius
  - [ ] typography
  - [ ] states/interaction styles
- Coverage verdict: PASS | FAIL

### 4) Component Purity Checklist (100% library-only)
- [ ] All rendered units map to documented library components
- [ ] All variants are legal variants from specs/matrix
- [ ] No unofficial components introduced
- [ ] No ad-hoc token names
- [ ] No ad-hoc layout/style values that bypass matrix rules
- Purity verdict: PASS | FAIL

### 5) Acceptance Matrix Result
| Component | Structure | Geometry | Typography | Token Name/Value | State Machine | Accessibility | Result |
|-----------|-----------|----------|------------|------------------|---------------|---------------|--------|
| ...       | PASS/FAIL | PASS/FAIL| PASS/FAIL  | PASS/FAIL        | PASS/FAIL     | PASS/FAIL     | PASS/FAIL |

### 6) Risks
- none | <explicit risks>

### 7) Final Verdict
- Fully compliant at Lx
- OR Not fully compliant, gaps: <explicit gap list>
```

Template enforcement rules:
1. If section 2 or 3 is missing, treat delivery as invalid.
2. If section 4 is FAIL, delivery must be marked non-compliant.
3. If any required checklist item is unknown/unverified, mark FAIL, not PASS.
4. If exact match is missing and no approximate candidate exists, user confirmation must be obtained before continuation.
5. Never output “Fully compliant” when any checklist or matrix row is FAIL.

## Non-Negotiable Rules
1. Never generate page UI before full `component_specs` ingestion.
2. Never generate page UI before full `component-matrix.html` style ingestion.
3. Never use components/styles/naming/tokens/layout outside the component library.
4. Never silently approximate token names/values when strict compliance is required.
5. Never skip state-machine or accessibility checks when interactions exist.
6. Never skip evidence-based compliance reporting.
