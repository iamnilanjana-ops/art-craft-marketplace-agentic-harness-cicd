# Agentic Engineer Capstone -- Rubric Self-Check



## Purpose



This self-check maps the current capstone evidence to the Canvas scoring criteria.



Statuses are intentionally conservative:



\* \*\*Complete\*\* means repository evidence currently supports the criterion.

\* \*\*Partial\*\* means meaningful evidence exists but additional final evidence is still needed.

\* \*\*Blocked\*\* means completion currently depends on an external runtime dependency.

\* \*\*Pending\*\* means the artifact or evidence has not yet been completed.



No criterion is marked complete based on estimated or invented results.



---



## 1. Workflow Scoping



\*\*Status: Complete\*\*



Evidence:



\* `docs/capstone-scope.md`

\* Stakeholder identified

\* Trigger defined

\* Inputs and outputs defined

\* Acceptance criteria defined

\* Failure modes identified

\* Job-seeker/no-deployment path selected

\* Existing Module 1-4 evidence and gaps inventoried



The selected workflow is an AI-assisted code review and governance pipeline with measurable review, quality, governance, and cost goals.



---



## 2. Sandboxed Environment



\*\*Status: Complete\*\*



Evidence:



\* `Dockerfile`

\* `docker-entrypoint.sh`

\* `scripts/run-agent.sh`

\* Role-specific read-only/read-write container behavior

\* Memory mounted only where required

\* Enforcement evidence in `eval/enforcement-verification.md`



The system runs in a containerized environment with explicit role-based workspace and memory boundaries.



The README now documents the capstone run path, required model credential, governed agents, preserved final-run evidence, and operational limitations for a new reviewer.



---



## 3. Quality Spec & Baseline

**Status: Partial**

Evidence:

- `docs/prd.md`
- `eval/rubric.json`
- historical Module 1 PRD/rubric/iteration evidence
- `docs/calibration-log.md`
- `docs/capstone-impact-report.md`
- `docs/run-summary.md`
- `logs/capstone-final-run-002.json`

The rubric defines four judgment dimensions with pass thresholds.

Measured baseline and comparison evidence exists for the deterministic conversion, including cycle time, model-token cost, review latency, structural checks, and repeatability.

The successful final production-like run also provides final execution evidence, including a 59.6-second full-pipeline runtime and recorded Planner, Reviewer, and Tester evaluation outcomes.

### Limitation

The available historical Module 1 artifacts do not provide one complete baseline containing every capstone impact metric.

In addition, the final transcript does not establish a trustworthy full-pipeline model-cost measurement, and one successful run is not sufficient evidence for a general defect-rate percentage.

The impact report therefore keeps historical baseline evidence, deterministic-conversion measurements, and final production-like measurements separate rather than reconstructing or inventing missing values.

---

## 4. Agents, Skills & Memory



\*\*Status: Complete\*\*



Evidence:



\* versioned role definitions under `agents/`

\* persistent state in `.memory/storage.db`

\* storage audit evidence

\* reusable references under `.memory/reference/`

\* role-scoped memory mounting

\* `docs/adr/ADR-004-memory-layout.md`



The memory architecture separates persistent state, reusable references, task context, and role instructions.



---



## 5. Orchestration & MCP Tools



\*\*Status: Complete\*\*



Evidence:



\* `docs/orchestration-diagram.md`

\* `docs/routing-and-tool-grant-map.md`

\* `mcp-servers/storage/`

\* `mcp-servers/retrieval/`

\* role-specific allow-lists

\* classification ceilings

\* retrieval ground-truth set

\* retrieval quality report

\* `schemas/handoff.json`



The Orchestrator delegates to scoped roles and MCP capabilities are not exposed globally.



---



## 6. Evaluation & Calibration

**Status: Complete**

Evidence:

- `eval/test_deterministic.py`
- `eval/test_rubric_suite.py`
- `eval/rubric.json`
- `docs/holdout-task-set.md`
- `docs/calibration-log.md`
- `eval/run_holdout.py`
- `eval/run_regression.py`
- regression and policy tests
- retrieval validation evidence
- `logs/capstone-final-run-002.json`
- `docs/run-summary.md`

The project uses a two-layer evaluation design combining deterministic checks with judgment-based evaluation criteria.

Calibration and regression evidence includes:

- 7/7 deterministic checks passing before and after the handoff-validation conversion;
- zero output variance across three deterministic runs after conversion;
- 24/24 integrated regression checks passing;
- passing policy evidence;
- retrieval calibration and validation evidence;
- preserved holdout tasks;
- a successful production-like model-backed workflow run.

The final production-like run completed the Planner -> Implementer -> Reviewer -> Tester path and recorded successful evaluation outcomes.

Measurement limitations, including the lack of a trustworthy full-pipeline model-cost value and the inability to generalize a defect-rate percentage from one successful run, are documented separately in `docs/capstone-impact-report.md`.

---




## 7. Governance, Security & CI/CD



\*\*Status: Complete\*\*



Evidence:



\* `docs/governance-policy.md`

\* `docs/routing-and-tool-grant-map.md`

\* MCP allow-lists

\* data-classification ceilings

\* `eval/test\_policy.py`

\* `eval/test\_governed\_files.py`

\* `eval/red-team-prompts.md`

\* `eval/red-team-results.md`

\* `eval/enforcement-verification.md`

\* `.github/workflows/ci.yml`

\* `docs/ci-step-design.md`



The tool-evolution drill also demonstrated that permission drift is automatically detected by the policy suite.



Known platform-level limitation:



Direct pushes from the authorized repository owner can bypass the configured pull-request and required-check rules. This is documented separately from repository-level enforcement.



---



## 8. Right-Tool Decisions & ADRs



\*\*Status: Complete\*\*



Evidence:



\* `docs/step-classification.md`

\* deterministic handoff validation

\* deterministic routing decision history

\* before/after latency and cost measurements

\* ADR package under `docs/adr/`



ADR coverage includes:



\* rubric design;

\* memory layout;

\* MCP boundaries;

\* subagent scoping and routing;

\* governance policy;

\* agent-to-deterministic conversion.



Measured handoff conversion evidence shows:



\* 45 seconds to 0.2 seconds cycle time;

\* $0.003 to $0 model-token cost;

\* approximately 30 seconds to 5 seconds review latency;

\* 7/7 structural checks preserved.



---



## 9. Production Integration & Tool-Evolution Drill

**Status: Complete**

Completed evidence:

- successful production-like model-backed orchestration;
- Planner -> Implementer -> Reviewer -> Tester execution;
- semantic retrieval and persistent-storage activity;
- Implementer storage write with downstream verification;
- governance enforcement;
- tool-evolution drill;
- regression detection and recovery;
- preserved transcript and audit evidence.

The successful final production-like run completed in 59.6 seconds.

Evidence:

- `logs/capstone-final-run-002.json`
- `logs/capstone-final-run-002.log`
- `docs/run-summary.md`
- `docs/capstone-tool-evolution-drill.md`

Tool-evolution result:

| Stage | Result |
|---|---|
| Baseline | 6 passed |
| Permission revoked | 1 failed, 5 passed |
| Permission restored | 6 passed |

Governance enforcement was also demonstrated independently. An unauthorized `documentation-writer` `write_entry` request was denied by the storage MCP allow-list and recorded as `authorization_denied`.

The earlier `capstone-final-run-001` is retained as evidence of an integration failure that was diagnosed and corrected before the successful final run.

## 10. Iteration Narrative & Impact

**Status: Complete with documented measurement limitations**

Evidence:

- `docs/iteration-log.md`
- `docs/calibration-log.md`
- `docs/capstone-impact-report.md`
- `docs/run-summary.md`
- deterministic conversion before/after evidence
- successful production-like run
- tool-evolution drill

The evidence shows multiple evidence-driven improvement cycles.

Measured deterministic-conversion impact includes:

- cycle time: 45 seconds -> 0.2 seconds;
- model-token cost: $0.003/run -> $0/run for the converted step;
- review latency: approximately 30 seconds -> approximately 5 seconds;
- structural quality: 7/7 checks passing before and after conversion;
- output variance: zero across three deterministic runs;
- integrated regression: 24/24 checks passing.

The final production-like pipeline completed in 59.6 seconds. In that successful run, 3 Planner review items, 4 Reviewer review items, and 1 Tester review item were approved, with no recorded rejected item.

Two measurement limitations remain explicit:

- one successful run is not sufficient evidence for a general 0% defect-rate claim;
- the transcript does not provide a trustworthy full-pipeline model-cost measurement.

No unsupported values are estimated or invented.



## 11. Stakeholder Communication

**Status: Partial**

Evidence:

- `docs/capstone-stakeholder-one-pager.md`
- `docs/capstone-architecture-writeup.md`
- `docs/capstone-impact-report.md`
- business-value framing
- risk-reduction explanation
- successful production-like run evidence in `docs/run-summary.md`

The stakeholder one-pager and supporting reports now describe the completed production-like workflow, measured deterministic-conversion impact, governance enforcement, business value, and remaining measurement limitations.

Remaining requirement:

- record the final five-to-ten-minute technical walkthrough demonstrating the completed workflow, governance enforcement, evaluation evidence, right-tool decision, measured impact, and operational readiness.

---

## 12. Clarity & Flow



\*\*Status: Partial\*\*



The planned final narrative follows:



1\. Problem and baseline

2\. Architecture

3\. Live workflow

4\. Governance

5\. Evaluation

6\. Right-tool decisions

7\. Impact

8\. Operations



Evidence documents already follow this narrative structure.



Final scoring depends on the completed walkthrough and presentation package.



---



## 13. Design



\*\*Status: Pending Final Packaging\*\*



Current content artifacts are complete enough to support final presentation design.



Remaining work includes:



\* convert required documents to polished PDFs;

\* ensure architecture diagrams and tables remain legible;

\* create the final slide/video presentation;

\* perform consistent visual formatting and sanitization.



---



## Current Readiness Summary

| Criterion | Status |
|---|---|
| Workflow Scoping | Complete |
| Sandboxed Environment | Complete |
| Quality Spec & Baseline | Partial — historical baseline limitations documented |
| Agents, Skills & Memory | Complete |
| Orchestration & MCP Tools | Complete |
| Evaluation & Calibration | Complete |
| Governance, Security & CI/CD | Complete |
| Right-Tool Decisions & ADRs | Complete |
| Production Integration & Tool-Evolution Drill | Complete |
| Iteration Narrative & Impact | Complete with documented measurement limitations |
| Stakeholder Communication | Partial — walkthrough video remaining |
| Clarity & Flow | Partial — final walkthrough/package remaining |
| Design | Pending Final Packaging |

## Remaining Critical Path

The remaining capstone critical path is now focused on final packaging and presentation rather than core workflow implementation:

1. perform the final sanitization and secret review;
2. run the final test and repository-status checks;
3. convert the required final documents to polished PDFs;
4. verify architecture diagrams and tables remain legible in the packaged artifacts;
5. record the five-to-ten-minute technical walkthrough;
6. perform the final submission review.

The production-like workflow, transcript and audit evidence, impact-report update, README run instructions, governance demonstration, and tool-evolution drill are already complete.


## Self-Check Conclusion

The repository now contains substantial completed evidence for workflow design, sandboxed execution, specialized agents, memory architecture, orchestration, MCP boundaries, evaluation and calibration, governance, CI/CD controls, deterministic conversion, ADRs, production-like integration, and tool-evolution testing.

A successful production-like run is preserved in `logs/capstone-final-run-002.json` with supporting audit evidence and a final run summary.

The remaining work is concentrated on final submission packaging and presentation rather than core system implementation.

Known limitations remain explicitly documented: the historical baseline does not contain every desired capstone metric, the final transcript does not establish a trustworthy full-pipeline model-cost measurement, one successful run is not sufficient to claim a general 0% defect rate, and the successful final run did not trigger the human-escalation path.

These limitations are reported rather than filled with estimated or invented results.




