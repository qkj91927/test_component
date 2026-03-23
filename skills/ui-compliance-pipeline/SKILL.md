---
name: ui-compliance-pipeline
description: "This skill should be used when generating or modifying any UI/page/component. Enforce a mandatory, gate-based compliance pipeline: full spec/style-token ingestion, component-library-only implementation, icons-first asset policy, token/state/accessibility validation, and evidence-based delivery verdict."
allowed-tools: 
disable: true
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
- `/test_component/component_specs/`

Execution requirements:
1. Discover all spec files in `component_specs`.
2. Read every spec file completely.
3. Build a normalized component constraints map (API, structure, variants, states, tokens, spacing/layout rules).
4. Record file coverage evidence (list of files read).

### Gate B: Component Matrix Style Reference (Optional but Recommended)
Use component style reference from:
- `/test_component/component-matrix.html`

Execution requirements:
1. Read relevant matrix sections as needed for style alignment.
2. Parse component-related style blocks and naming conventions when the target page/component needs them.
3. Use matrix-derived class/token/layout/state information as a reference source.
4. Record what matrix scope was referenced (targeted evidence).

### Gate C: Full Style-Token Ingestion (Required for page generation)
Read style-token source before UI generation:
- `/test_component/style_css/` (component style tokens)

Execution requirements:
1. Discover all files in `style_css` and read every file completely.
2. Build a normalized token map (token naming/value/usage constraints) from `style_css`.
3. Generate UI styles using `style_css` tokens only; do not use hard-coded visual values.
4. Record full file coverage evidence for `style_css`.
5. Block implementation if folder coverage is incomplete.

### Gate D: Icon Asset Priority Policy (Required)
When UI generation needs icon resources, apply icon priority strictly.

Execution requirements:
1. Resolve icons from `/test_component/icons/` first.
2. If no semantically suitable icon exists in `icons`, fallback to already approved project icon assets and record fallback reason.
3. Never import external/unofficial icons without explicit user confirmation.
4. Do not modify original icon SVG stroke/weight settings when generating UI.
5. Ensure icon stroke/weight is consistent across the same page.
6. Ensure icon color matches the corresponding component-spec-defined icon color and use icon color tokens from `style_css` tokens.
7. Record icon source decisions and icon consistency checks in delivery report.

### Gate E: Component-Library-Only Composition (Required for page generation)
Generate page UI using **100% component-library components only**.

Strict constraints:
1. Use only documented components and documented variants from `component_specs` + `component-matrix` + `style_css`.
2. Keep canonical component naming, class naming, and token naming unchanged.
3. Keep style/layout values aligned to library definitions; do not invent ad-hoc styles.
4. Keep page composition as legal combinations of library components only.
5. If one-to-one exact component/variant match is unavailable, select the nearest legal component/variant from the library first.
6. If no acceptable approximate component exists, pause generation and ask user whether to continue and which continuation strategy to use; continue only after explicit user response.
7. Never fabricate unofficial components or bypass library constraints.

### Gate F: Matching Fallback and User Confirmation (Required)
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

### Step 1: Clone Required Repository (Mandatory First Step)
- Clone this repository before any UI analysis or implementation:
  - `https://github.com/qkj91927/test_component`
- Default local target path:
  - `/test_component/`
- If the repository already exists locally, pull latest changes and continue.
- Do not skip this step.

### Step 2: Lock Scope and Acceptance Level
- Identify target page/components and required interaction scope.
- Set acceptance level (default L4 for page generation).
- Define verification radius (component-local or full-page regression).

### Step 3: Run Gate A (Full `component_specs` ingestion)
- Complete full-folder ingestion.
- Build the component constraints map.
- Block implementation if any spec file is unread.

### Step 4: Run Gate B (Targeted `component-matrix.html` reference)
- Read and parse relevant matrix sections as needed.
- Build class/token/layout/state mapping for the target scope.
- Record referenced matrix scope evidence.

### Step 5: Run Gate C (Full `style_css` ingestion)
- Complete full-folder ingestion for `style_css`.
- Build style-token map from `style_css`.
- Block implementation if any file in folder is unread.

### Step 6: Run Gate D (Icon source + consistency)
- Resolve icon needs from `icons` folder first.
- If fallback is used, keep evidence and reason.
- Block external icon usage unless user explicitly confirms.
- Do not alter original icon SVG stroke/weight.
- Keep icon stroke/weight consistent across the same page.
- Use component-spec-aligned icon colors via icon color tokens.

### Step 7: Build Acceptance Matrix
Create per-component checklist:
1. Component identity and legal variant
2. DOM/slot structure
3. Geometry (W/H/padding/gap/radius)
4. Typography (family/size/weight/line-height)
5. Token naming + value consistency
6. Asset source/semantics/size/color/stroke consistency
7. States and event-driven transitions
8. Accessibility (ARIA, keyboard, focus, labels)
9. Regression impact

Do not implement before acceptance matrix is complete.

### Step 8: Implement with Library Lock
- Implement only with approved library components/variants.
- Preserve canonical naming and tokens.
- Preserve matrix-aligned layout and spacing where referenced.
- Reject custom one-off CSS/structure that bypasses component library constraints.

### Step 9: Validate State Machine and Interaction
- Validate entry, intermediate, and exit/cancel/clear/back transitions.
- Validate edge cases (empty input, blur timing, rapid actions, disabled/error paths).

### Step 10: Validate Accessibility and Regression
- Validate keyboard navigation and visible focus.
- Validate semantic roles/labels.
- Validate no unintended global token/style side effects.

### Step 11: Reverse Regression Backtest + Auto-Repair Loop After Page Generation (Required)
- After page generation, run reverse regression checks.
- Verify all page styles and rendered units use repository-internal components, tokens, and icons only.
- Verify no external component/token/icon source is introduced.
- If any item fails component spec / token spec / icon spec compliance:
  1. self-fix the non-compliant parts,
  2. regenerate the page,
  3. rerun reverse regression backtest.
- Repeat the above loop until compliance reaches 100%.
- Only output the final page after 100% compliance is achieved.
- Record each iteration evidence and final pass verdict.

### Step 12: Delivery Contract (Required)
Output must include:
1. What changed
2. Full spec ingestion evidence (`component_specs` file list)
3. Matrix reference evidence (`component-matrix.html` referenced scope statement)
4. Full style-token ingestion evidence (`style_css` file list)
5. Icon source + stroke/weight consistency + icon token-color evidence
6. Acceptance matrix results (pass/fail per item)
7. Reverse regression backtest loop results (components/tokens/icons source audit + iteration history)
8. Remaining risks or "none"
9. Final verdict:
   - "Fully compliant at Lx (100%)"
   - or "Not fully compliant, gaps: ..."

Never claim completion without evidence.


### Step 13: Mandatory Compliance Output Template (Required)
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

### 3) Matrix Reference Checklist (`component-matrix.html` targeted reference)
- Source file: /test_component/component-matrix.html
- Reference mode: targeted/as-needed
- Referenced style domains (if used):
  - [ ] component class naming
  - [ ] token naming/value
  - [ ] geometry/spacing/radius
  - [ ] typography
  - [ ] states/interaction styles
- Coverage verdict: PASS | N/A | FAIL

### 4) Style Token Coverage Checklist (`style_css` full ingestion)
- Source folder: /test_component/style_css/
- [ ] All style token files read in full
- [ ] Token naming/value/usage map extracted
- Coverage verdict: PASS | FAIL

### 5) Icon Source Priority Checklist (`icons` first)
- Source folder: /test_component/icons/
- [ ] Icon demand resolved from `icons` first
- [ ] Fallback (if any) has explicit reason and approved source
- [ ] No external/unofficial icons without user confirmation
- [ ] Original icon SVG stroke/weight not modified
- [ ] Icon stroke/weight is consistent across the same page
- [ ] Icon color matches component spec and uses icon color token
- Coverage verdict: PASS | FAIL

### 6) Component Purity Checklist (100% library-only)
- [ ] All rendered units map to documented library components
- [ ] All variants are legal variants from specs/matrix/token sources
- [ ] No unofficial components introduced
- [ ] No ad-hoc token names
- [ ] No ad-hoc layout/style values that bypass library rules
- Purity verdict: PASS | FAIL

### 7) Matching Fallback Decision (when exact match missing)
- Exact match found: YES | NO
- Approximate candidate evaluated: YES | NO
- Selected approximate component/variant: <name> | none
- If none, user confirmation asked: YES | NO
- User decision summary: <reply> | pending

### 8) Acceptance Matrix Result
| Component | Structure | Geometry | Typography | Token Name/Value | State Machine | Accessibility | Result |
|-----------|-----------|----------|------------|------------------|---------------|---------------|--------|
| ...       | PASS/FAIL | PASS/FAIL| PASS/FAIL  | PASS/FAIL        | PASS/FAIL     | PASS/FAIL     | PASS/FAIL |

### 9) Reverse Regression Backtest + Auto-Repair Loop Result
- [ ] All page styles are from repository components/tokens/icons only
- [ ] No external component/token/icon source introduced
- [ ] If FAIL occurred, self-fix + regenerate + retest loop executed
- Iteration count: <n>
- Per-iteration summary:
  - Iteration 1: FAIL/PASS, fixes: <summary>
  - Iteration 2: FAIL/PASS, fixes: <summary>
  - ...
- Final backtest verdict: PASS (100%) | FAIL

### 10) Risks
- none | <explicit risks>

### 11) Final Verdict
- Fully compliant at Lx (100%)
- OR Not fully compliant, gaps: <explicit gap list>
```

Template enforcement rules:
1. If section 2 is missing, treat delivery as invalid.
2. If section 4 is missing, treat delivery as invalid.
3. If section 4 contains hard-coded visual values, delivery is non-compliant.
4. If section 5 is FAIL, icon usage is non-compliant.
5. If section 6 is FAIL, delivery must be marked non-compliant.
6. If section 9 final verdict is not PASS (100%), delivery must be marked non-compliant.
7. If any required checklist item is unknown/unverified, mark FAIL, not PASS.
8. If exact match is missing and no approximate candidate exists, user confirmation must be obtained before continuation.
9. Never output "Fully compliant" when any checklist or matrix row is FAIL.
10. If reverse regression finds component/token/icon non-compliance, repair+regenerate+retest loop is mandatory.

## Non-Negotiable Rules
1. Never generate page UI before full `component_specs` ingestion.
2. Never generate page UI before full `style_css` token ingestion.
3. Always resolve icon usage from `icons` folder first.
4. If no suitable icon exists in `icons`, use only approved fallback source with explicit reason.
5. Never modify original icon SVG stroke/weight.
6. Keep icon stroke/weight consistent across the same page.
7. Use component-spec-aligned icon colors via icon color tokens.
8. Never use components/styles/naming/tokens/layout outside the component library.
9. Never silently approximate token names/values when strict compliance is required.
10. If exact match and approximate match both fail, pause and ask user how to proceed; continue only after explicit reply.
11. Never skip state-machine or accessibility checks when interactions exist.
12. After page generation, reverse-regression-test component/token/icon source compliance.
13. If reverse regression finds non-compliance, self-fix + regenerate + retest until 100% compliance.
14. Only output final page when reverse regression final verdict is PASS (100%).
15. Never skip evidence-based compliance reporting.
