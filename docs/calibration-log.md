# Calibration Log

## Near-Miss Patterns for Module 4 Governance

### 1. Implementer Delete Permission

During governance calibration, the Implementer was identified as having an overly broad potential `delete_entry` capability.

**Risk:** An Implementer with delete access could remove project state required by downstream agents.

**Evidence status:** Historical calibration/design finding. No executed `delete_entry` denial event for the Implementer is present in the current audit log, so this is not claimed as runtime denial evidence.

**Resulting control:** The final governance policy does not grant `delete_entry` to the Implementer. The policy test verifies that the role is excluded from this permission.

### 2. Reviewer Test-Skill Activation

During calibration, Reviewer output exposed the risk of activating the `run-tests` skill even though the Reviewer is intended to remain read-only.

**Risk:** A review-only role should not execute a capability that may change workspace state.

**Evidence status:** Historical calibration/design finding. No `skill_activation_denied` runtime log for the Reviewer is present in the current evidence, so this is not claimed as an executed denial.

**Resulting control:** The final governance policy explicitly denies `run-tests` to the Reviewer.

### 3. Confidential Retrieval Above Classification Ceiling

The retrieval evaluation tested whether an internal-level workflow could retrieve the confidential `cost-breakdown.md` document.

**Risk:** Retrieval above a role's classification ceiling could expose sensitive information to an unauthorized workflow.

**Executed evidence:** `docs/retrieval-quality-report.md`, Q5 — Classification Ceiling Enforcement.

- Requested information matched confidential cost data.
- Classification ceiling: `internal`.
- Forbidden document: `cost-breakdown.md` (`confidential`).
- The confidential document was not returned.
- Result: **PASS**.

**Resulting control:** Retrieval enforces classification ceilings and prevents confidential material from being returned to internal-only workflows.

## Conversion measurements

### Before conversion — handoff validation agent

- Average cycle time: 45 seconds across three runs.
- Token cost: $0.003 per run.
- Deterministic harness checks: 7/7 passing.
- Review latency: about 30 seconds.

### After conversion — deterministic handoff validator in isolation

- Average cycle time: 0.2 seconds across three runs.
- Token cost: $0.
- Deterministic harness checks: 7/7 passing.
- Output variance: zero; `diff` reported no differences across three runs.
- Review latency: about 5 seconds.

### Integrated end-to-end regression check

- Date: 2026-06-06
- Result: 24/24 harness checks passing; no regressions.
- Policy suite: passing.
- Evidence: deterministic validator is wired into orchestration and governance artifacts are in sync.
