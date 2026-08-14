# Agentic Engineer Capstone -- Stakeholder One-Pager



## What Problem Does This Solve?



Software changes often require several separate activities: implementation, review, testing, documentation, policy checks, and human approval.



When these steps are handled manually or by one unrestricted AI agent, teams can face slower reviews, inconsistent decisions, unnecessary model cost, and higher risk from over-broad permissions.



This capstone demonstrates a governed engineering pipeline that divides work across specialized AI agents, deterministic automation, and human checkpoints.



## What the System Does



The workflow coordinates specialized roles for:

- implementation;
- code review;
- testing;
- project summaries;
- documentation;
- workflow orchestration.



Each role receives only the tools and data access required for its responsibility.



Stable structural work is moved out of AI agents and into deterministic code when possible.



Human approval remains in the workflow for higher-risk or consequential actions.



## Why This Matters to the Business



The system is designed to reduce review burden without giving AI agents unrestricted authority.



Measured evidence from one deterministic conversion shows:



| Metric | Before | After |
| --- | ---: | ---: |
| Validation cycle time | 45 seconds | 0.2 seconds |
| Model-token cost | $0.003/run | $0/run |
| Review latency | ~30 seconds | ~5 seconds |
| Structural checks | 7/7 passing | 7/7 passing |



The deterministic implementation also produced zero output variance across three repeated runs.



This shows that a stable workflow step can become faster, cheaper, and more predictable without reducing the recorded validation quality.



## Risk Reduction



The project identified real governance near-misses, including:



- overly broad delete permissions;

- a read-only reviewer nearly receiving testing capability;

- retrieval attempts above a role's approved data-classification level.



The final design addresses these risks through:



- least-privilege tool access;

- role-specific MCP allow-lists;

- data-classification ceilings;

- read-only containers for advisory roles;

- policy and regression tests;

- human escalation;

- red-team testing.



## Evidence That Governance Works



A controlled tool-evolution drill temporarily removed a required permission from the Documentation Writer role.



The policy test suite changed from:



`6 passed`



to:



`1 failed, 5 passed`



After the permission was restored, the same suite returned to:



`6 passed`



This demonstrates that permission drift can be detected automatically instead of depending only on manual review.



## What Is Already Demonstrated



The capstone currently demonstrates:



- containerized agent execution;

- specialized agent roles;

- deterministic handoff validation;

- scoped storage and retrieval access;

- evaluation and regression tests;

- enforceable governance rules;

- CI/CD guardrails;

- policy-bypass testing;

- architecture decision records;

- measurable latency and cost improvements for a converted workflow step.



## Final Production-Like Evidence

The final production-like workflow completed the expected:

`Planner -> Implementer -> Reviewer -> Tester`

path in 59.6 seconds.

The run exercised semantic retrieval, persistent-storage reads, an Implementer storage write, independent Reviewer verification, and Tester validation.

All recorded evaluation items in the successful run were approved: 3 Planner review items, 4 Reviewer review items, and 1 Tester review item. No recorded review item was rejected.

Governance enforcement was also demonstrated separately. An unauthorized `documentation-writer` attempt to call `write_entry` was denied by the storage MCP allow-list and recorded as `authorization_denied`, while the same role's permitted `read_entry` operation succeeded.

## Remaining Limitations

Two limitations remain explicit:

- The final transcript does not provide a trustworthy full-pipeline model-cost measurement, so no unsupported end-to-end cost claim is made.
- Human-checkpoint conditions are defined in governance policy, but the successful final production-like run did not require or trigger human escalation.

One successful evaluated run is also not sufficient evidence to claim a general 0% defect rate across all future workloads.

## Next Steps

The remaining capstone work is primarily final packaging and operational validation:

1. finalize the operations runbook and rubric self-check;
2. complete the final sanitization review;
3. package the required architecture, ADR, impact, stakeholder, and runbook artifacts;
4. record the technical walkthrough video.


## Business Value



The project demonstrates how an engineering team can use AI agents for judgment-heavy work while keeping predictable tasks deterministic and preserving human control over higher-risk decisions.



The result is a workflow designed to improve speed and consistency while reducing unnecessary model usage and limiting the operational risk of over-reaching agents.




