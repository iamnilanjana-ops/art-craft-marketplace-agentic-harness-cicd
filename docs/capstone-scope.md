\# Agentic Engineer Capstone Scope



\## 1. Selected Workflow



\*\*Workflow:\*\* AI-Assisted Code Review and Governance Pipeline



The capstone will demonstrate a governed multi-agent engineering workflow that supports software changes from planning through implementation, review, testing, human approval, and project tracking.



The workflow reuses and integrates the agentic engineering components developed during Modules 1–4.



\## 2. Problem



Software changes require multiple review steps, including planning, implementation, code review, testing, and approval. Performing all of these steps manually can increase review time and create inconsistent results.



The capstone will demonstrate how specialized AI agents can assist with judgment-heavy engineering tasks while deterministic checks and human approval provide predictable and safe controls.

### Representative Before-State Baseline

Because this is a job-seeker capstone rather than a live production deployment, the before-state is defined using a representative manual-review scenario rather than proprietary company data.

For one representative software change, the manual workflow requires approximately:

- 10 minutes for planning and change review
- 10 minutes for implementation review
- 10 minutes for reviewer validation
- 5 minutes for test-result verification
- 5 minutes for approval and documentation

This produces a representative baseline of approximately **40 minutes of human review effort per change**.

At a representative volume of **10 changes per week**, this equals approximately **400 minutes (6.7 reviewer hours) per week**.

The capstone evaluates whether the governed multi-agent pipeline can reduce this review burden while maintaining deterministic validation, governance controls, human approval where required, and an auditable record of the workflow.

These values are representative planning assumptions for the capstone and are not claimed as measurements from a production organization.

### Why a Custom Governed Pipeline

A single prebuilt or unrestricted coding agent could generate or review code, but it would not provide the same separation of responsibilities, scoped tool permissions, deterministic validation, independent review, human approval checkpoints, and audit evidence required by this workflow.

This capstone therefore uses a custom multi-agent pipeline because the workflow combines several different responsibilities:

- planning and implementation
- independent review and testing
- role-specific MCP tool permissions
- deterministic policy and schema checks
- persistent audit evidence
- human escalation for higher-risk or conflicting decisions

A simpler automation is appropriate for predictable checks such as schema validation and policy enforcement, and those steps remain deterministic in this architecture. Agent reasoning is reserved for judgment-heavy work such as planning, implementation, and review.

This separation provides a concrete reason to use a governed custom pipeline rather than replacing the entire workflow with one general-purpose agent.

\## 3. Stakeholder



The primary stakeholder is a software development team that wants to reduce code-review burden while maintaining quality, governance, and traceability.



For this job-seeker capstone, the workflow will use public, representative, or sanitized project data rather than proprietary production data.



\## 4. Trigger



The workflow begins when a developer submits or prepares a software change that needs review and validation.



\## 5. Inputs



Typical inputs include:



\* Feature or change request

\* Repository or code change

\* Acceptance criteria

\* Relevant project context

\* Governance and tool-access rules



\## 6. Workflow



Developer Change

→ Orchestrator

→ Planner

→ Implementer

→ Reviewer

→ Tester

→ Human Approval

→ Project Manager



The Orchestrator delegates work to specialized agents. Each role receives only the tools and context needed for its responsibility.



\## 7. Outputs



The workflow produces:



\* Implementation or proposed code change

\* Reviewer decision

\* Test result

\* Evaluation results

\* Governance and policy decisions

\* Human approval record

\* Audit trail

\* Project status update



\## 8. Acceptance Criteria



A successful workflow run should:



1\. Route the task to the correct agent roles.

2\. Keep tool permissions within the defined role boundaries.

3\. Produce a valid implementation or review result.

4\. Pass required deterministic checks.

5\. Pass applicable rubric-based evaluation thresholds.

6\. Require human approval where defined.

7\. Record agent actions, tool calls, policy decisions, failures, and approvals.

8\. Prevent unauthorized tool or data access.

9\. Produce enough evidence to reproduce and audit the run.



\## 9. Expected Failure Modes



Important failure modes include:



\* Incorrect agent routing

\* Context leakage between roles

\* Excessive tool permissions

\* Invalid output structure or schema

\* Retrieval miss

\* Conflicting reviewer or agent outputs

\* Governance or policy bypass attempt

\* Evaluation regression

\* Agent step used where deterministic code would be more appropriate



\## 10. Delivery Path



\*\*Selected path:\*\* Job-Seeker / No-Deployment



The project will use public, representative, synthetic, or sanitized data. It will not depend on proprietary customer or employer data.



\## 11. Final Demo



The final walkthrough will demonstrate:



\* Repository structure and setup

\* Containerized agent harness

\* Multi-agent orchestration

\* Scoped tool grants

\* MCP-backed storage or retrieval

\* Evaluation results

\* Governance blocking an unauthorized action

\* Agent vs. deterministic vs. human decision-making

\* Deterministic conversion

\* Baseline vs. final impact metrics

\* Reliability and cost controls



\## 12. Existing Module 1–4 Evidence



The current repository already contains substantial capstone evidence, including:



\* PRD

\* Iteration log

\* Versioned agent definitions

\* Orchestration documentation

\* Routing and tool-grant map

\* Retrieval ground-truth set

\* Retrieval quality report

\* Holdout task set

\* Calibration log

\* Evaluation harness

\* Governance policy

\* CI/CD guardrails

\* Red-team tests

\* Enforcement verification

\* Deterministic conversion work

\* Deterministic tests

\* Architecture Decision Records related to deterministic conversion



\## 13. Known Capstone Gaps



Items still requiring completion or final capstone packaging include:



\* Final architecture write-up

\* Complete ADR package

\* Baseline-vs-after impact report

\* Tool-evolution drill summary

\* Stakeholder one-pager

\* Ops-ready runbook

\* Rubric self-check

\* Capstone-focused README/run instructions

\* Final production-like end-to-end runs

\* Final evaluation and impact metrics

\* Technical walkthrough video

\* Final sanitization review



