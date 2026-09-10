# Adoption Plan — Inbound Lead Triage

## 1. Adoption Goal

The goal is to introduce the Inbound Lead Triage workflow gradually so the sales team can reduce manual lead-review work while keeping human oversight.

## 2. Initial Users

The first users should be a small sales or operations team that currently reviews inbound demo requests, pricing questions, partnership inquiries, and general inquiries.

## 3. Rollout Approach

### Phase 1 — Pilot

- Run the workflow with representative or synthetic leads.
- Confirm Gmail, Zapier, Slack, and the Python worker operate correctly.
- Review every automated qualification result.
- Record errors and unexpected behavior.

### Phase 2 — Limited Use

- Process a small number of real or simulated inbound leads.
- Continue human review of qualification results.
- Track processing time, errors, and manual interventions.
- Compare results with the documented baseline.

### Phase 3 — Wider Adoption

Expand usage only after:

- Regression tests consistently pass.
- Lead scoring results meet acceptance thresholds.
- Human reviewers understand the escalation process.
- Monitoring and rollback procedures are available.

## 4. User Training

Users should understand:

- How a new lead appears in Slack
- How to read the Python lead score
- What Qualified, Needs Review, and Not Qualified mean
- When human review is required
- How to send an approved reply
- How to report an incorrect result or workflow failure

## 5. Human Review

Human reviewers remain responsible for judgment-based decisions.

They should review:

- Needs Review leads
- Invalid or incomplete leads
- Unexpected scoring results
- Sensitive or unusual inquiries
- External responses before they are sent when human approval is required

## 6. Feedback Process

Users should report:

- Incorrect qualification results
- Missing information
- Routing problems
- Failed Zap runs
- Slack worker failures
- Unclear scoring explanations

Feedback should be reviewed before scoring rules or workflow logic are changed.

## 7. Change Management

Any significant change to scoring or routing should follow this process:

1. Document the proposed change.
2. Update the workflow or Python logic.
3. Run the regression test suite.
4. Confirm all tests pass.
5. Test representative leads.
6. Deploy the change only after successful validation.

## 8. Adoption Success Measures

Adoption will be considered successful when:

- Users can operate the workflow without developer assistance.
- Lead processing time decreases.
- Manual repetitive triage work decreases.
- Qualification results remain consistent.
- Critical workflow failures are detected and handled.
- Human reviewers know when and how to intervene.

## 9. Rollback During Adoption

If the workflow becomes unreliable:

- Stop the Python worker.
- Disable the affected Zap.
- Return temporarily to manual Slack-based lead review.
- Diagnose and fix the issue.
- Run regression tests before restarting automation.

This ensures the sales team can continue working even if the automation is unavailable.