\# ADR-006: Subagent Scoping and Routing



\## Status



Accepted



\## Context



The engineering workflow contains multiple responsibilities that should not be handled by one unrestricted agent.



Planning, implementation, review, testing, project communication, and workflow coordination require different capabilities, levels of autonomy, and tool access.



Using one general-purpose agent for all steps would make it difficult to enforce least privilege and would increase the chance that one role could accidentally perform work that belongs to another role.



The pipeline therefore requires explicit subagent boundaries and a routing model that assigns work according to task type.



\## Decision



Use an Orchestrator to coordinate specialized subagents.



Current specialized roles include:



\* Implementer

\* Reviewer

\* Tester

\* Project Manager

\* Documentation Writer



The Orchestrator remains responsible for parent-workflow coordination and delegation.



The current orchestration path is:



```text

Orchestrator

&#x20;   |

&#x20;   v

Detect Changed Files

&#x20;   |

&#x20;   v

Validate Handoff

&#x20;   |

&#x20;   v

Route Task

&#x20;   |

&#x20;   +--> Implementer

&#x20;   |

&#x20;   +--> Reviewer

&#x20;   |

&#x20;   +--> Tester

&#x20;   |

&#x20;   +--> Project Manager

```



The routed outputs then continue through policy and evaluation gates.



\## Role Scoping



\### Implementer



The Implementer owns code and implementation work.



It may modify project state within its permitted scope and receives the tools needed for implementation.



It does not receive destructive storage access such as `delete\_entry`.



\### Reviewer



The Reviewer owns code-review work.



It is intentionally advisory and read-only.



The Reviewer is not permitted to modify stored project state or apply implementation changes.



\### Tester



The Tester owns test execution and test reporting.



Its workspace remains read-only for tracked source files, preventing test execution from becoming an implementation path.



\### Project Manager



The Project Manager owns description and summary work.



It may read project state but does not receive implementation, testing, or retrieval capabilities that are unnecessary for its role.



\### Documentation Writer



The Documentation Writer may read stored state and retrieve internal reference material when documentation work requires context.



Its access remains narrower than the Orchestrator.



\## Routing Rules



The routing design maps work to the role that owns the task.



Current route categories include:



| Route                          | Role            |

| ------------------------------ | --------------- |

| Code or implementation         | Implementer     |

| Code review                    | Reviewer        |

| Tests                          | Tester          |

| Description or project summary | Project Manager |



The routing layer is deliberately kept separate from agent execution.



This allows routing behavior to be inspected, tested, and eventually converted to deterministic logic when the categories become stable enough.



\## Deterministic Routing Direction



The repository includes a deterministic routing example as decision-history evidence.



This reflects the right-tool principle:



If routing depends only on stable, precisely defined structural conditions, it should not remain agentic indefinitely.



Agentic routing is appropriate only when task classification still requires ambiguity handling or contextual interpretation.



\## Rejected Alternatives



\### Alternative 1: Use one agent for the entire workflow



Rejected because one agent would require broad permissions across implementation, review, testing, storage, retrieval, and project communication.



This would weaken least privilege and make audit trails less meaningful.



\### Alternative 2: Give every subagent the same tools



Rejected because tool needs differ by responsibility.



For example:



\* the Reviewer should not modify state;

\* the Tester should not become an implementation role;

\* the Project Manager does not need retrieval;

\* the Orchestrator requires broader coordination and audit access.



\### Alternative 3: Route tasks manually every time



Rejected because manual routing would reduce automation value and would not scale well as the workflow repeats.



Human checkpoints should remain for consequential decisions, not routine role assignment when the route can be determined safely.



\### Alternative 4: Make routing fully deterministic immediately



Rejected because routing should only be deterministic when task categories and edge cases are sufficiently stable and specifiable.



The project preserves a deterministic routing example but does not assume every future routing decision can be reduced to rules.



\## Evidence



The orchestration documentation shows:



```text

Orchestrator

→ Detect changed files

→ Validate handoff

→ Route task

→ Specialized role

→ Policy and eval gates

```



The routing-and-tool-grant map records distinct route conditions for:



\* Implementer

\* Reviewer

\* Tester

\* Project Manager



The governance policy applies different permissions, classification ceilings, skills, autonomy levels, and container permissions to each role.



Calibration evidence also supports role separation.



Observed near-misses included:



\* an Implementer with overly broad delete access;

\* a Reviewer nearly triggering a testing skill;

\* an Implementer requesting data above its classification ceiling.



These near-misses demonstrate why role scope must be enforced rather than treated as documentation only.



\## Consequences



\### Positive consequences



\* Each agent has a clear responsibility.

\* Tool grants can remain narrow.

\* Review independence is preserved.

\* Testing authority is separated from implementation authority.

\* Routing and execution can be tested independently.

\* Future deterministic conversion of stable routing rules remains possible.

\* Audit evidence becomes easier to interpret by role.



\### Negative consequences



\* More roles increase configuration and maintenance overhead.

\* Routing mistakes can send a task to the wrong specialist.

\* Changes to workflow responsibilities may require synchronized updates across agent definitions, governance policy, allow-lists, and tests.

\* Some tasks may cross role boundaries and require escalation or multiple agents.



\## Open Risks



1\. Ambiguous tasks may be routed incorrectly.

2\. A new workflow category may not map cleanly to an existing role.

3\. Role definitions and routing rules could drift apart over time.

4\. Overlapping responsibilities could produce duplicate or conflicting outputs.

5\. Deterministic routing could become too rigid if converted before edge cases are understood.



These risks are mitigated through evaluation, regression testing, governance checks, calibration, and human escalation when task ownership is unclear.



\## Decision Summary



The capstone uses an Orchestrator plus scoped subagents rather than one unrestricted agent.



Routing assigns work to specialized roles according to task type, and each role receives only the tools, data access, and autonomy required for its responsibility.



This design improves least privilege, auditability, review independence, and future right-tool conversion opportunities.



