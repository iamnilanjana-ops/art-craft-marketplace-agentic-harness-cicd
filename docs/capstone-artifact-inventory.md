\# Capstone Artifact Inventory



\## Purpose



This inventory maps the Agentic Engineer Capstone requirements to artifacts already created during Modules 1–4 and identifies remaining gaps for the final capstone submission.



\## Existing Evidence



| Capstone Area                         | Status   | Existing Evidence                                                                                    |

| ------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |

| PRD                                   | Complete | `docs/prd.md`                                                                                        |

| Iteration log                         | Complete | `docs/iteration-log.md`                                                                              |

| Agent definitions                     | Complete | `agents/`                                                                                            |

| Orchestration diagram                 | Complete | `docs/orchestration-diagram.md` and `docs/orchestration-diagram-ascii.md`                            |

| Routing and tool-grant map            | Complete | `docs/routing-and-tool-grant-map.md` and `.json`                                                     |

| Retrieval ground-truth set            | Complete | `docs/retrieval-ground-truth.md`                                                                     |

| Retrieval quality report              | Complete | `docs/retrieval-quality-report.md`                                                                   |

| Holdout task set                      | Complete | `docs/holdout-task-set.md`                                                                           |

| Calibration log                       | Complete | `docs/calibration-log.md`                                                                            |

| Evaluation harness                    | Complete | `eval/orchestrator.py`, `eval/run\_holdout.py`, `eval/run\_regression.py`                              |

| Evaluation rubric                     | Complete | `eval/rubric.json`                                                                                   |

| Governance policy                     | Complete | `docs/governance-policy.md`                                                                          |

| CI/CD guardrails                      | Complete | `.github/workflows/ci.yml`                                                                           |

| CI/CD design documentation            | Complete | `docs/ci-step-design.md`                                                                             |

| Governance enforcement tests          | Complete | `eval/test\_policy.py`, `eval/test\_governed\_files.py`                                                 |

| Red-team prompts                      | Complete | `eval/red-team-prompts.md`                                                                           |

| Red-team results                      | Complete | `eval/red-team-results.md`                                                                           |

| Enforcement verification              | Complete | `eval/enforcement-verification.md`                                                                   |

| Agent-vs-deterministic classification | Complete | `docs/step-classification.md`                                                                        |

| Deterministic tests                   | Complete | `eval/test\_deterministic.py`, `eval/test\_deterministic\_router.py`, `eval/test\_deterministic\_step.py` |

| Deterministic conversion ADRs         | Complete | `docs/adr/`                                                                                          |

| Capstone workflow scope               | Complete | `docs/capstone-scope.md`                                                                             |



\## Existing ADRs



Current ADRs include:



\* `ADR-001-json-schema-validation-deterministic-conversion.md`

\* `ADR-002-routing-deterministic-conversion.md`

\* `ADR-002-tester-acceptance-verification-deterministic-conversion.md`



These provide evidence for deterministic conversion decisions.



\## Remaining Capstone Gaps



The following artifacts still need to be completed or packaged for the final capstone:



1\. Capstone-focused README and reproducible run path

2\. Final architecture write-up

3\. ADR for rubric design

4\. ADR for memory layout

5\. ADR for MCP boundaries

6\. ADR for subagent scoping and routing

7\. ADR for governance policy

8\. Final baseline-vs-after impact report

9\. Tool-evolution drill and summary

10\. Stakeholder one-pager

11\. Ops-ready runbook

12\. Rubric self-check

13\. Final production-like end-to-end run

14\. Final evaluation results

15\. Final quality, latency, defect-rate, cycle-time, and cost metrics

16\. Final sanitization review

17\. Five-to-ten-minute technical walkthrough video



\## API-Key Dependency



Most documentation, repository organization, governance, ADR, and architecture work can be completed without an external model API key.



An API key or authenticated agent runtime may be required later for:



\* Live multi-agent executions

\* Rubric-based model evaluation

\* Final holdout evaluation runs

\* Production-like end-to-end workflow demonstration

\* Cost-per-run measurements

\* Tool-evolution model-swap experiments, if a model change is selected



The capstone should continue with non-runtime tasks while API access is pending.



\## Current Readiness



The repository already contains substantial Module 1–4 evidence and is suitable as the starting point for the capstone.



The next priority is to package and document the existing system before performing the final production-like integration and measurement runs.



