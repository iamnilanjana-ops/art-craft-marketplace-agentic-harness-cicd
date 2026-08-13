# Step Classification

This document is updated after every calibration cycle. Steps that cross the stability threshold are promoted to candidate status. A step that has been a candidate for more than two calibration cycles without meeting all four signals is reviewed for re-scoping.

## Step: JSON schema validation

- Status: Converted to deterministic (ADR-001, 2026-06-06).
- Stability: harness scores 14/16, 15/16, 14/16 across the last three calibration runs. Consistent.
- Repeatability: three runs on the same holdout input produced identical output.
- Specifiability: validate the output document against `schemas/handoff.json` and reject it if any required field is missing, null, or empty.
- Run rate: every workflow invocation.
- Preserved edge case: present-but-empty required fields are rejected by `scripts/validate_handoff_deterministic.py` and covered by `eval/test_deterministic_step.py`.
- Recommendation: converted.

## Step: Planner

- Recommendation: not a candidate. Needs judgment and synthesis to break a task into subtasks; output is not specifiable in advance.
- Next review: 2026-09-04.

## Step: Release note draft

- Recommendation: weak candidate. Output is prose that needs human review and is not yet repeatable across runs.
- Candidate since: 2026-06-04. Next review: 2026-07-04.

## Step: Path-based routing

- Recommendation: converted to deterministic sample (ADR-002). It uses explicit path rules with a default for unmatched paths.
- Preserved edge case: unmatched paths route to `implementer` instead of failing silently.
## Step: Tester acceptance-criteria verification

- Current behavior: The Tester receives the acceptance criteria, the list of implemented or modified files, and the implementation summary after the Reviewer passes. It runs the available test suite, interprets the results against each acceptance criterion, and returns a PASS or FAIL report to the Orchestrator.
- Stability: Partial. Iteration Log Run 2 (2026-08-10) shows that the Tester behaved as designed by identifying acceptance criteria that lacked automated test coverage, blocking completion, and later returning PASS after the Implementer added the missing tests. However, the available evidence does not yet show consistent behavior across at least two full calibration cycles.
- Repeatability: Not yet demonstrated. Run 2 records a correct FAIL followed by PASS after the implementation's test coverage changed, but there is no evidence of three repeated runs on the same unchanged input producing an identical decision and output.
- Specifiability: Partial. Running the available test suite and reporting passed/failed/skipped counts can be specified deterministically, but deciding whether test results adequately cover each natural-language acceptance criterion still requires interpretation.
- Run rate: High. The Tester is invoked after the Reviewer passes an implementation and before the workflow can continue to the Project Manager.
- Known agent judgment / edge-case input: A test suite can have no failing tests while still failing to cover one or more acceptance criteria. In Iteration Log Run 2, the Tester identified missing automated coverage for localStorage persistence, product-specific review rendering, and cascade deletion of reviews when a product is removed.
- Recommendation: weak candidate. The mechanical test-running and result-counting portions could potentially be deterministic, but the complete Tester acceptance-criteria verification step is not ready for conversion because stability and repeatability have not been demonstrated and acceptance-criteria coverage still requires interpretation. Additional calibration evidence and repeated identical-input runs would be required before considering full deterministic conversion.
- Next review: 2026-09-13.
### Planned Tests for a Future Deterministic Replacement

1. **Normal successful case**
   - Input: Acceptance criteria where every criterion has a corresponding automated test, and the test suite reports all tests passing.
   - Expected output: PASS, with the passed/failed/skipped counts and every acceptance criterion marked as covered.
   - Why it matters: Confirms that the deterministic portion can correctly recognize a clean, fully covered implementation without blocking the workflow.

2. **Invalid or failure case**
   - Input: Acceptance criteria with corresponding automated tests where at least one required test fails.
   - Expected output: FAIL, identifying the failing test and the acceptance criterion affected.
   - Why it matters: Prevents a failing implementation from being reported as safe to continue to the Project Manager.

3. **Known agent judgment / edge-case case**
   - Input: A test suite with no failing tests, but one or more acceptance criteria have no automated test coverage, such as the missing localStorage persistence, product-specific review rendering, or cascade-deletion coverage identified in Iteration Log Run 2.
   - Expected output: FAIL or an explicit uncovered-criterion result; it must not silently return PASS.
   - Why it matters: Protects the judgment the current Tester demonstrated in Run 2. A deterministic implementation that misses this case would repeat the same incorrect PASS every time.
### Measurement Plan

Before accepting any future conversion, collect the same evidence for the current agentic Tester and the proposed deterministic portion using the same inputs across repeated runs.

- **Latency:** Measure average wall-clock execution time across three runs before and after conversion.
- **Token cost:** Record the agent's input/output token cost per run and compare it with the deterministic portion's expected zero token cost.
- **Predictability:** Run the same unchanged input three times and compare the outputs. Record whether the PASS/FAIL decision, counts, and structured results are identical.
- **Audit clarity:** Compare how easily a reviewer can determine what the step did from the agent definition/transcript versus the deterministic code and structured result. Record approximate review time.
- **Quality / harness results:** Compare the same applicable deterministic harness checks before and after conversion. Every shared required check passed by the agent must continue to pass.
- **Potential N/A rubric dimensions:** Any rubric dimension that evaluates the quality of the agent's prose explanation may become not applicable if a future deterministic portion returns structured results instead. Such dimensions should be marked N/A rather than counted as quality regressions.
### Rollback Plan

Any future conversion should be made as one focused, revertible commit. That commit should contain only the changes required to replace the selected Tester operations with deterministic code.

If the deterministic replacement produces incorrect results after integration, revert that single conversion commit. The revert must restore the Orchestrator instructions that invoke the previous Tester behavior, the Tester's routing-map row and tool grants, the relevant governance-policy entry, any retired Tester agent or step-specific artifacts, and any CI step changed to invoke the deterministic replacement. This keeps rollback independent of unrelated project work.