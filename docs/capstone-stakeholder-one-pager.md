# Agentic Engineer Capstone â€” Stakeholder One-Pager



## What Problem Does This Solve?



Software changes often require several separate activities: implementation, review, testing, documentation, policy checks, and human approval.



When these steps are handled manually or by one unrestricted AI agent, teams can face slower reviews, inconsistent decisions, unnecessary model cost, and higher risk from over-broad permissions.



This capstone demonstrates a governed engineering pipeline that divides work across specialized AI agents, deterministic automation, and human checkpoints.



## What the System Does



The workflow coordinates specialized roles for:



\* implementation;

\* code review;

\* testing;

\* project summaries;

\* documentation;

\* workflow orchestration.



Each role receives only the tools and data access required for its responsibility.



Stable structural work is moved out of AI agents and into deterministic code when possible.



Human approval remains in the workflow for higher-risk or consequential actions.



## Why This Matters to the Business



The system is designed to reduce review burden without giving AI agents unrestricted authority.



Measured evidence from one deterministic conversion shows:



| Metric                |      Before |       After |

| --------------------- | ----------: | ----------: |

| Validation cycle time |  45 seconds | 0.2 seconds |

| Model-token cost      |  $0.003/run |      $0/run |

| Review latency        | ~30 seconds |  ~5 seconds |

| Structural checks     | 7/7 passing | 7/7 passing |



The deterministic implementation also produced zero output variance across three repeated runs.



This shows that a stable workflow step can become faster, cheaper, and more predictable without reducing the recorded validation quality.



## Risk Reduction



The project identified real governance near-misses, including:



\* overly broad delete permissions;

\* a read-only reviewer nearly receiving testing capability;

\* retrieval attempts above a role's approved data-classification level.



The final design addresses these risks through:



\* least-privilege tool access;

\* role-specific MCP allow-lists;

\* data-classification ceilings;

\* read-only containers for advisory roles;

\* policy and regression tests;

\* human escalation;

\* red-team testing.



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



\* containerized agent execution;

\* specialized agent roles;

\* deterministic handoff validation;

\* scoped storage and retrieval access;

\* evaluation and regression tests;

\* enforceable governance rules;

\* CI/CD guardrails;

\* policy-bypass testing;

\* architecture decision records;

\* measurable latency and cost improvements for a converted workflow step.



## Current Limitation



The final production-like OpenRouter-backed workflow run is still pending because the course-managed API key currently reaches OpenRouter successfully but encounters a managed guardrail/data-policy routing restriction for the configured Claude model.



This limitation is being treated as an external runtime dependency rather than hidden or replaced with invented results.



## Next Steps



The remaining work is to:



1\. complete the final production-like workflow run after the course API policy issue is resolved;

2\. capture final quality, latency, defect-rate, cycle-time, and cost-per-run metrics;

3\. update the impact report with final measured results;

4\. complete the operational runbook and rubric self-check;

5\. record the final technical walkthrough.



## Business Value



The project demonstrates how an engineering team can use AI agents for judgment-heavy work while keeping predictable tasks deterministic and preserving human control over higher-risk decisions.



The result is a workflow designed to improve speed and consistency while reducing unnecessary model usage and limiting the operational risk of over-reaching agents.




