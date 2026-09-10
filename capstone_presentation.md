# Inbound Lead Triage

## Agentic Specialist Capstone

Automating first-pass lead qualification with Zapier, Slack, Gmail, and Python

**Presented by: Nilanjana Choudhury**
---

# Problem and Goal

## The Problem

Inbound sales leads require repetitive manual work:

- Reading incoming inquiries
- Extracting lead information
- Evaluating lead quality
- Deciding priority and routing
- Preparing follow-up actions

## The Goal

Build an agentic workflow that automates first-pass lead triage while keeping humans involved in review and external communication.
---

# Solution Architecture

The solution combines four main components:

- Orchestrator Zap — receives inbound Gmail messages, classifies the inquiry, posts structured lead information to Slack, and records workflow state.
- V2 Python Lead Qualification Agent — validates structured lead fields and applies deterministic scoring.
- Qualification and Routing Zap — routes results based on validation, ICP fit, and review requirements.
- Reply Sender Zap — sends an external Gmail response only after the required human-controlled reply step.

## Workflow and Routing

Gmail → Orchestrator Zap → Slack shared state

Slack NEW LEAD → V2 Python Agent → LEAD SCORED

Routing conditions:

- **Strong Fit / High Priority** → sales follow-up / routing recommendation
- **Moderate Fit / Medium Priority** → human review before external action
- **Low Fit / Low Priority** → no automatic sales follow-up; result remains logged
- **Invalid, missing, or ambiguous information** → human review instead of guessed qualification

Human-approved response → Reply Sender Zap → Gmail

## Why Slack Shared State?

Slack is used as shared operational state instead of relying only on direct Zap-to-Zap chaining because:

- Zapier and the Python worker can read the same workflow context.
- Humans can inspect lead information, scoring results, and handoffs.
- Components remain loosely coupled instead of depending on one long direct automation chain.
- Failures and exceptions remain visible for review and recovery.

# Python Lead Qualification Agent

The V2 Python agent applies deterministic scoring to structured lead information.

## What It Does

- Validates required lead fields
- Calculates a deterministic Lead Quality Score from 0–100
- Assesses ICP fit
- Suggests response priority
- Provides a scoring reason
- Returns structured results for the workflow

## V2 Scoring Model

- Company Size — maximum 35 points
- Use Case — maximum 25 points
- Industry — maximum 20 points
- Urgency Signals — maximum 20 points

## ICP Fit

- 70–100 → Strong Fit
- 40–69 → Moderate Fit
- 0–39 → Low Fit

## Suggested Response Priority

- 70–100 → High
- 40–69 → Medium
- 0–39 → Low

The deterministic design makes scoring consistent, explainable, and regression-testable.

---
# Prompt Engineering and Iteration

The Orchestrator prompt was improved from Version 1.0 to Version 1.1 using a structured meta-prompt review.

## Version 1.0

The initial prompt classified inbound inquiries into:

- DEMO REQUEST
- PRICING QUESTION
- PARTNERSHIP
- GENERAL INQUIRY

The first version provided useful classification guidance but did not enforce a sufficiently strict output structure or explicitly prevent unsupported inference.

## Meta-Prompt Critique

The review identified five improvements:

1. Enforce a predictable output format.
2. Prohibit inference of urgency, budget, or qualification.
3. Define a deterministic fallback for ambiguous messages.
4. Strengthen sensitive-information handling.
5. Use stable field names for downstream automation.

## Version 1.1 Improvements

Accepted:

- Fixed classification categories
- Exact `category` and `summary` fields
- GENERAL INQUIRY fallback for ambiguity
- No invented information
- Sensitive-information boundary
- Concise structured output

Rejected:

- Dynamic categories — would make routing unpredictable
- AI-generated qualification score — deterministic Python owns scoring
- Automatic external response — human oversight remains required

## Before / After Evidence

Ambiguous input:

“Hi, I saw your company online and wanted to learn more about what you offer. Please send me some information.”

V1.0 risk:
Output structure and ambiguous fallback were not strict enough.

V1.1 expected result:

`category: GENERAL INQUIRY`

`summary: Sender is requesting general information about the company's offerings.`

The revised prompt provides predictable downstream fields without inventing qualification information.
---
---
# Quality Specification

Quality is evaluated across seven dimensions:

- Correctness
- Validation
- Consistency
- Explainability
- Human Oversight
- Speed
- Cost

## Quality Scale

- **5 — Excellent:** Fully correct; no correction required
- **4 — Good:** Correct with only a minor issue
- **3 — Acceptable:** Usable with minor human review
- **2 — Weak:** Significant error or correction required
- **1 — Failed:** Unusable or incorrect

## Manual Baseline

Representative leads are manually reviewed for expected qualification and routing, then compared with the automated result.

## Passing Standard

The prototype passes when:

- Average quality score is **4/5 or higher**
- No quality dimension is below **3/5**
- Qualification and routing match the expected outcome
- Required regression tests achieve **100% pass rate**

This specification provides a consistent basis for comparing manual and automated lead-triage quality.
---

# Testing and Results

The V2 scoring agent was tested with five regression cases.

## Verified Results

- Strong Fit / High Priority → PASS
- Moderate Fit / Medium Priority → PASS
- Low Fit / Low Priority → PASS
- Invalid / Missing Required Information → PASS
- Adversarial Instruction Input → PASS

## Regression Testing

Automated pytest regression suite:

**5 tests passed in 0.06s**

Regression pass rate: **100%**

The adversarial test confirmed that instructions embedded in lead data do not override the deterministic Python scoring rules.

## Measured Performance

The standalone V2 Python scoring execution was measured across 10 runs:

- Average execution time: **63.68 ms (0.0637 seconds)**
- Observed range: **59.06–75.40 ms**

This measurement represents standalone Python V2 execution only. End-to-end Gmail, Zapier, Slack, and worker latency has not yet been measured.

# Business Value

## Planning Assumptions

- Estimated lead volume: 100 leads/month
- Manual processing baseline: 10 minutes/lead
- Target human review after automation: 2 minutes/lead
- Assumed fully loaded labor cost: $40/hour

The 10-minute manual baseline is estimated as:

- Read inbound email: 2 minutes
- Identify inquiry and extract information: 2 minutes
- Evaluate lead-quality factors: 3 minutes
- Assess priority and routing: 1 minute
- Record decision / prepare follow-up: 2 minutes

These values are capstone planning assumptions, not measured production data.

## Projected Impact

- Human time saved: approximately 13.34 hours/month
- Projected labor savings: approximately $534/month
- Projected annual labor savings: approximately $6,408
- Projected first-pass human processing reduction: approximately 80%

## Automation Cost

The deterministic V2 Python scoring component does not use a paid AI model or token-based inference API.

End-to-end automation cost has **not yet been measured** because actual cost depends on Zapier, Slack, Gmail / Google Workspace, worker hosting, and usage volume.

Production cost and projected savings should be validated during a controlled pilot.

# Governance and Human Oversight

The workflow keeps humans involved in judgment-based and external actions.

## Access and Change Control

- Zapier workflow changes are limited to authorized workflow owners/admins.
- V2 Python scoring weights are changed only by authorized code maintainers.
- Scoring or routing changes require regression testing before release.
- Credentials and tokens remain outside submitted source code.

## Human Review Controls

- Ambiguous, invalid, or incomplete lead information is sent for human review rather than guessed.
- Humans can review scoring results and workflow context in Slack.
- External responses remain controlled through the Reply Sender workflow.
- Automation provides recommendations; it does not replace final human judgment.

## Rollback Trigger

Automation must be paused if:

- **Two consecutive invalid or clearly incorrect scoring results occur on otherwise valid inputs**, or
- **Any required V2 regression test fails.**

Rollback process:

Stop worker / affected Zap → Return to manual Slack review → Investigate and fix → Run all 5 V2 regression tests → Restart only after verification.

## Launch Readiness

**VERIFIED**
- 5/5 V2 regression tests passed
- Adversarial-input protection tested
- Invalid-input handling tested
- Human-review path available
- Numeric rollback trigger documented

**NOT YET TESTED**
- End-to-end workflow latency under controlled measurement
- Production-volume reliability and performance

# Deployment and Adoption

## Controlled Rollout

1. Pilot with representative or synthetic leads
2. Review automated qualification results
3. Move to limited use with human oversight
4. Expand only after acceptance criteria continue to pass

## Production Improvements

Before production deployment:

- Production-grade monitoring and logging
- Centralized secret management
- Retry and failure handling
- Improved alerting
- Production sales-system integrations
- Real operational performance measurement

The current solution is designed for capstone demonstration and controlled pilot evaluation, not full production deployment.
---

# Conclusion

## What the Prototype Demonstrates

- End-to-end agentic lead triage workflow
- Zapier, Gmail, Slack, and Python integration
- Deterministic V2 lead scoring
- Explainable ICP fit and response priority
- Safe invalid-input handling
- Human-in-the-loop oversight
- Five V2 regression tests with 100% pass rate
- Adversarial-input protection
- Measured standalone V2 Python execution performance
- Governance, access control, rollback, scale, and adoption planning
- Clearly separated measured evidence and projected business value

## Current Status

**READY FOR CAPSTONE DEMONSTRATION**

The prototype is ready for capstone demonstration based on the verified test evidence.

A controlled pilot would be the next step to measure end-to-end workflow latency, production reliability, actual operating cost, qualification quality with real protected data, and realized business impact.

# Thank You
