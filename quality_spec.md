# Quality Specification — Inbound Lead Triage

## 1. Purpose

This quality specification defines how the Inbound Lead Triage workflow will be evaluated for correctness, consistency, safety, speed, and cost.

## 2. Expected Python Agent Output

For every processed lead, the Python agent should return:

- company_name
- total_score
- qualification_status
- validation_status
- validation_issues
- scoring_reason

## 3. Lead Scoring

The total lead score ranges from 0 to 100.

Scoring dimensions:

- Budget: 0–30 points
- Business Need: 0–30 points
- Company Size: 0–20 points
- Purchase Timeline: 0–20 points

Qualification thresholds:

- 70–100 = Qualified
- 40–69 = Needs Review
- 0–39 = Not Qualified

## 4. Quality Evaluation Criteria

### Correctness

The calculated score must follow the documented deterministic scoring rules.

Acceptance threshold:
100% of regression tests must pass.

### Classification Accuracy

The qualification status must match the calculated score.

Acceptance threshold:

- Score 70–100 → Qualified
- Score 40–69 → Needs Review
- Score 0–39 → Not Qualified

### Validation

Required lead fields must be checked before scoring.

Acceptance threshold:
Missing or invalid required data must produce:

- validation_status = invalid
- total_score = 0
- qualification_status = Not Qualified
- a clear validation issue

### Explainability

Every scored lead must include a scoring reason showing how the score was calculated.

Acceptance threshold:
100% of valid scored leads include a readable scoring explanation.

### Consistency

The same structured input should produce the same result when processed repeatedly.

Acceptance threshold:
Deterministic scoring must not depend on randomness or an LLM.

### Human Oversight

Ambiguous, incomplete, or review-required cases must remain visible to a human in Slack.

Acceptance threshold:
Needs Review and invalid cases can be identified for human review before further action.

## 5. Speed Metric

Prototype goal:

Automated first-pass lead triage should reduce human processing effort compared with the estimated manual baseline of 10 minutes per lead.

Target human review effort:
2 minutes or less per lead on average during a future operational pilot.

## 6. Cost Metric

Baseline business-case assumption:

- 100 leads per month
- 10 minutes manual processing per lead
- $40/hour fully loaded labor cost

Target:

Reduce estimated first-pass human processing effort by approximately 80%.

## 7. Evaluation Cases

The evaluation suite includes:

1. Qualified lead
2. Needs Review lead
3. Not Qualified lead
4. Invalid lead with missing required information

## 8. Current Regression Result

Regression test result:

4 tests passed.

This confirms that the current scoring implementation correctly handles all four documented evaluation cases.

## 9. Minimum Passing Standard

The workflow is considered acceptable for capstone demonstration when:

- All regression tests pass.
- At least 3 representative workflow runs complete successfully.
- Valid leads receive the expected deterministic score and status.
- Invalid inputs are safely detected.
- Scoring decisions include an explanation.
- Human review remains available for uncertain cases.
- No secrets or credentials appear in submitted evidence.

## 10. Production Acceptance

The current results demonstrate prototype readiness, not production readiness.

Before production deployment, the organization should validate these thresholds using real operational lead data and measure actual processing time, review rate, failure rate, and qualification quality.