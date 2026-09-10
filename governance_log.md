# Governance Log — Inbound Lead Triage

## 1. Purpose

This governance log documents the controls used to keep the Inbound Lead Triage workflow safe, reviewable, and easy to monitor.

The workflow uses Gmail, Zapier, Slack, and a Python lead qualification agent.

## 2. Permissions and Access Control

Access follows least-privilege principles. Only people responsible for maintaining the workflow should be able to modify automation logic or scoring rules.

| Component | Who Can View | Who Can Edit | Control |
|---|---|---|---|
| Gmail lead inbox | Authorized sales/operations users | Authorized account owners | Gmail account permissions |
| Zapier workflows | Authorized workflow users | Workflow owner/admin | Zapier workspace permissions |
| Slack lead channel | Approved team members | Workspace/channel admins manage access | Slack permissions |
| Python scoring code | Project/repository collaborators | Authorized code maintainer | Repository access and code review |
| V2 scoring weights | Project/repository collaborators | Authorized code maintainer | Changes require regression testing before release |
| Environment variables/tokens | Authorized system owner | Authorized system owner | Secrets are not stored in source code |

API keys and Slack tokens must never be hardcoded in Python source code or included in screenshots or submitted project files.

Any change to Zap routing logic or V2 scoring weights must be reviewed and regression-tested before the updated automation is used.

## 3. Data Handling

The workflow processes only the information needed for lead triage, such as:

- Sender email
- Company name
- Contact name
- Company size
- Budget
- Business need
- Purchase timeline

Synthetic test data is used for capstone testing and screenshots.

## 4. Human-in-the-Loop Gates

The system does not automatically make final sales decisions.

The V2 Python agent produces deterministic lead-scoring recommendations based on structured lead information.

V2 ICP fit thresholds:

- 70–100: Strong Fit
- 40–69: Moderate Fit
- 0–39: Low Fit

Suggested response priority:

- 70–100: High
- 40–69: Medium
- 0–39: Low

A human can review the Slack thread before taking an external action.

Ambiguous, invalid, or missing information is routed for human review rather than guessed by the automation.

The Reply Sender requires an explicit human reply marker before an external email response is sent.

## 5. Output Validation

Before scoring a lead, the V2 Python agent validates these required fields:

- Company name
- Company size
- Use case
- Industry
- Urgency signals

If required information is missing or invalid:

- `validation_status` becomes `invalid`.
- The lead quality score becomes 0.
- The validation issue is clearly reported.
- The workflow does not guess missing information.
- The lead is sent for human review instead of normal automated qualification.

This provides a safe fallback for incomplete or unreliable input.

## 6. Decision Logging

The workflow keeps processing visible in Slack.

The Python agent posts a structured thread reply containing:

- Company name
- Total score
- Qualification status
- Validation status
- Validation issues
- Scoring reason

This makes the scoring decision understandable and reviewable.

## 7. Monitoring

The workflow should be monitored for:

- Slack worker connection failures
- Missing required lead fields
- Invalid lead data
- Unexpected qualification scores
- Zap failures
- Gmail delivery failures
- Slack messages that do not receive expected processing

Representative test runs and regression tests are used to confirm expected behavior.

## 8. Escalation

Human review is required when:

- A lead receives `Needs Review`.
- Required information is missing.
- Input data is invalid.
- The result appears inconsistent with the original lead.
- A workflow component fails.
- An external response requires human judgment.

## 9. Rollback

The automation must be paused and the workflow returned to manual review if:

- Two consecutive invalid or clearly incorrect scoring results occur on otherwise valid inputs, or
- Any required V2 regression test fails.

Rollback procedure:

1. Stop the Python Slack worker.
2. Turn off the affected Zap.
3. Continue lead review manually in Slack.
4. Record and investigate the failure.
5. Correct the scoring or workflow issue.
6. Run the complete V2 regression test suite.
7. Restart automation only after all regression tests pass and the issue has been verified as resolved.

This numeric trigger provides a clear rule for when automation should be stopped instead of relying only on subjective judgment.

## 10. Regression Protection

The V2 Python evaluation suite checks five cases:

1. Strong Fit / High Priority lead
2. Moderate Fit / Medium Priority lead
3. Low Fit / Low Priority lead
4. Invalid lead with missing required information
5. Adversarial input attempting to override the deterministic scoring rules

Latest verified regression result:

`5 passed in 0.06s`

All five regression tests must pass before a scoring-rule or scoring-weight change is considered ready for use.

The adversarial test also confirms that instructions embedded inside lead data do not override the deterministic Python scoring logic.

## 11. Privacy and Security

- No API keys or tokens are stored in submitted source code.
- No credentials are included in screenshots.
- Synthetic lead information is used for demonstration.
- Access should follow least-privilege principles.
- Human review remains available for uncertain or sensitive decisions.