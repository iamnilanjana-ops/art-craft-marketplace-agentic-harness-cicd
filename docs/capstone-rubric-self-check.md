# Agentic Engineer Capstone â€” Rubric Self-Check



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

\* Existing Module 1â€“4 evidence and gaps inventoried



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



Final README polish is still required to make the capstone run path clearer for a new reviewer.



---



## 3. Quality Spec & Baseline



\*\*Status: Partial\*\*



Evidence:



\* `docs/prd.md`

\* `eval/rubric.json`

\* historical Module 1 PRD/rubric/iteration evidence

\* `docs/calibration-log.md`

\* `docs/capstone-impact-report.md`



The rubric defines four judgment dimensions with pass thresholds.



Measured deterministic-conversion baseline evidence exists for latency, cost, validation checks, and review latency.



Limitation:



The currently available Module 1 artifacts do not provide one complete historical baseline containing every final capstone metric.



The final report will distinguish historical evidence, deterministic-conversion evidence, and final production-like measurements rather than reconstruct missing values.



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



\*\*Status: Partial\*\*



Evidence:



\* `eval/test\_deterministic.py`

\* `eval/test\_rubric\_suite.py`

\* `eval/rubric.json`

\* `docs/holdout-task-set.md`

\* `docs/calibration-log.md`

\* regression and policy tests

\* retrieval validation evidence



The two-layer evaluation design is present and deterministic/policy testing is functioning.



Remaining evidence:



\* final model-backed production-like evaluation run;

\* final holdout/rubric results after the current external API policy blocker is resolved.



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



\*\*Status: Blocked / Partial\*\*



Completed evidence:



\* deterministic integration evidence;

\* policy suite;

\* governance enforcement;

\* tool-evolution drill;

\* regression detection and recovery.



Tool-evolution result:



| Stage               | Result             |

| ------------------- | ------------------ |

| Baseline            | 6 passed           |

| Permission revoked  | 1 failed, 5 passed |

| Permission restored | 6 passed           |



External blocker:



The final OpenRouter-backed orchestration currently fails with a managed guardrail/data-policy routing restriction even though the API key authenticates successfully.



Final production-like model-backed run is therefore still pending.



---



## 10. Iteration Narrative & Impact



\*\*Status: Partial\*\*



Evidence:



\* `docs/iteration-log.md`

\* `docs/calibration-log.md`

\* `docs/capstone-impact-report.md`

\* deterministic conversion before/after evidence

\* tool-evolution drill



The current evidence shows multiple evidence-driven improvement cycles.



Remaining work:



\* capture final full-pipeline quality;

\* review latency;

\* defect-rate metric or proxy;

\* cycle time;

\* cost per run.



These will be reported only after a successful production-like run.



---



## 11. Stakeholder Communication



\*\*Status: Partial\*\*



Evidence:



\* `docs/capstone-stakeholder-one-pager.md`

\* architecture write-up

\* impact report

\* business-value framing

\* risk-reduction explanation



Remaining requirement:



\* record the final five-to-ten-minute walkthrough video after the model-backed workflow run can be demonstrated.



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



| Criterion                                     | Status                  |

| --------------------------------------------- | ----------------------- |

| Workflow Scoping                              | Complete                |

| Sandboxed Environment                         | Complete                |

| Quality Spec & Baseline                       | Partial                 |

| Agents, Skills & Memory                       | Complete                |

| Orchestration & MCP Tools                     | Complete                |

| Evaluation & Calibration                      | Partial                 |

| Governance, Security & CI/CD                  | Complete                |

| Right-Tool Decisions & ADRs                   | Complete                |

| Production Integration & Tool-Evolution Drill | Blocked / Partial       |

| Iteration Narrative & Impact                  | Partial                 |

| Stakeholder Communication                     | Partial                 |

| Clarity & Flow                                | Partial                 |

| Design                                        | Pending Final Packaging |



## Remaining Critical Path



The remaining capstone critical path is:



1\. Resolve or receive guidance for the managed OpenRouter policy restriction.

2\. Run the complete production-like workflow.

3\. Save transcript and audit evidence.

4\. Run final deterministic and rubric evaluation.

5\. Record final quality, review latency, defect rate, cycle time, and cost-per-run metrics.

6\. Update the impact report.

7\. Polish README run instructions.

8\. Convert final deliverables to PDF.

9\. Record the five-to-ten-minute walkthrough.

10\. Perform final sanitization and submission review.



## Self-Check Conclusion



The repository already contains substantial evidence for workflow design, orchestration, governance, deterministic conversion, MCP boundaries, evaluation infrastructure, ADRs, and tool-evolution testing.



The remaining gap is concentrated around the final model-backed production-like run and the metrics and presentation evidence that depend on that run.



The submission should not claim full completion of those criteria until the runtime dependency is resolved and the remaining measurements are captured.




