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