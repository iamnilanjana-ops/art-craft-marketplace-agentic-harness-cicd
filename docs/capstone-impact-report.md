# Capstone Impact Report



## 1. Purpose



This report measures the impact of right-sizing the agentic engineering pipeline and records the evidence available before the final production-like capstone run.



The report separates measured results from metrics that still require final runtime execution. No missing metric is estimated or invented.



## 2. Measured Deterministic Conversion



One stable workflow step, handoff validation, was converted from agentic execution to deterministic code.



The measurements recorded in `docs/calibration-log.md` are:



| Metric | Before: Agentic Validation | After: Deterministic Validation | Result |

|---|---:|---:|---|

| Average cycle time | 45 seconds | 0.2 seconds | Improved |

| Token cost per run | $0.003 | $0 | Improved |

| Review latency | ~30 seconds | ~5 seconds | Improved |

| Deterministic harness checks | 7/7 passing | 7/7 passing | Quality preserved |

| Output variance | Not recorded | Zero across 3 runs | Repeatable |



## 3. Cycle-Time Impact



The measured handoff-validation cycle time decreased from 45 seconds to 0.2 seconds.



This represents a reduction of approximately 44.8 seconds per validation run.



The deterministic implementation therefore performs the stable validation step substantially faster while preserving the recorded deterministic checks.



## 4. Cost Impact



The agentic handoff-validation step recorded a token cost of approximately:



`$0.003 per run`



The deterministic implementation records:



`$0 per run`



for model-token cost.



The deterministic implementation therefore removes model-token cost from this specific validation step.



This does not mean the complete multi-agent workflow has zero cost. Other agentic steps may still require model execution.



## 5. Review-Latency Impact



Recorded review latency decreased from approximately:



`30 seconds`



to:



`5 seconds`



for the converted validation path.



This is a measured improvement for the converted step, not yet a claim about total end-to-end capstone review latency.



## 6. Reliability and Repeatability



Before conversion, the recorded deterministic harness result was:



`7/7 passing`



After conversion, the result remained:



`7/7 passing`



The deterministic implementation also produced zero output variance across three repeated runs, with no differences reported.



This provides evidence that the conversion improved speed and cost without reducing the measured structural quality of the step.



## 7. Integrated Regression Evidence



After the deterministic validator was integrated into the larger workflow, the calibration log recorded:



`24/24 harness checks passing`



The policy suite also passed.



This indicates that the conversion did not introduce a detected regression in the recorded integration check.



## 8. Governance Impact



Calibration identified several governance near-misses:



- overly broad Implementer delete access;

- Reviewer access that could trigger an inappropriate testing capability;

- retrieval above the Implementer's classification ceiling.



The final governance design responds to these risks through:



- role-specific MCP allow-lists;

- data-classification ceilings;

- read-only role boundaries;

- policy tests;

- governed-file tests;

- red-team testing;

- human checkpoints.



These controls reduce the blast radius of an incorrect or overreaching agent action.



## 9. Final Production-Like Run Evidence

The final production-like capstone run was completed using the course-approved Claude Haiku 4.5 model.

| Metric | Result |
|---|---|
| Model | anthropic/claude-haiku-4.5 |
| Agent path | planner → implementer → reviewer → tester |
| Full-pipeline runtime | 59.6 seconds |
| Audit entries | 15 |
| Transcript | logs/capstone-final-run-002.json |
| Audit log | logs/capstone-final-run-002.log |

The run successfully exercised retrieval, storage reads, and an implementer storage write. Reviewer and tester steps completed with recorded validation results.

The final run establishes production-like execution evidence. Full-pipeline quality score, defect-rate measurement, and reliable cost-per-run measurement are still pending because the current transcript does not provide a trustworthy final cost value.

## 10. Baseline Limitation



The repository contains historical Module 1 PRD, rubric, and iteration evidence, but the currently available Module 1 artifacts do not provide a complete single baseline containing every capstone impact metric.



Historical measurements must therefore be labeled according to their actual source rather than reconstructed or estimated.



The final capstone comparison will distinguish:



1. historical Module 1 evidence;

2. deterministic-conversion measurements;

3. final production-like capstone measurements.

## 11. Tool-Evolution Drill

A controlled permission-change drill was performed on the storage MCP allow-list.

The `documentation-writer` role temporarily lost its granted `read_entry` permission.

Results:

| Stage | Policy Test Result |
|---|---|
| Baseline | 6 passed |
| Permission revoked | 1 failed, 5 passed |
| Permission restored | 6 passed |

The failing test was:

`test_documentation_writer_policy_matches_enforcement`

This demonstrated that the evaluation and governance system can detect permission drift between the documented policy and executable MCP enforcement.

The permission was restored and the same policy suite returned to a fully passing state.

Detailed evidence is available in:

`docs/capstone-tool-evolution-drill.md`

## 12. Current Conclusion



The evidence currently supports a strong conclusion for the handoff-validation conversion:



- cycle time decreased;

- model-token cost was removed from that step;

- review latency decreased;

- deterministic checks remained passing;

- repeated deterministic output showed zero variance;

- integrated regression checks remained passing.



A broader claim about total capstone impact will be made only after the final production-like workflow is executed and measured.

