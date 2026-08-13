\# ADR-005: MCP Boundaries and Least-Privilege Tool Access



\## Status



Accepted



\## Context



The multi-agent pipeline requires persistent storage and retrieval capabilities, but exposing every MCP operation to every agent would violate least-privilege design and increase the impact of agent mistakes.



The repository implements two MCP-backed capabilities:



\* persistent storage;

\* retrieval.



These capabilities serve different purposes and have different risk profiles.



Storage operations can modify or remove project state, while retrieval can expose information at different data-classification levels.



The architecture therefore needs explicit boundaries that define:



\* which roles can call which operations;

\* which roles may modify state;

\* which roles may inspect audit information;

\* which roles may retrieve data;

\* what classification level each role may access.



\## Decision



Use separate MCP servers for storage and retrieval, with explicit role-based allow-lists enforced at the operation level.



\### Storage MCP



The storage server is located under:



```text

mcp-servers/storage/

```



The storage allow-list grants operations by role.



Current permissions are:



| Operation      | Allowed Roles                                                                      |

| -------------- | ---------------------------------------------------------------------------------- |

| `write\_entry`  | implementer, orchestrator                                                          |

| `read\_entry`   | implementer, reviewer, tester, project-manager, orchestrator, documentation-writer |

| `list\_entries` | implementer, reviewer, tester, project-manager, orchestrator, documentation-writer |

| `update\_entry` | implementer, orchestrator                                                          |

| `delete\_entry` | orchestrator                                                                       |

| `audit\_read`   | orchestrator                                                                       |



This means destructive and audit-sensitive operations are restricted more heavily than read operations.



\### Retrieval MCP



The retrieval server is located under:



```text

mcp-servers/retrieval/

```



Retrieval permission is granted per role and includes a data-classification ceiling.



Current configuration is:



| Role                 | Retrieval | Classification Ceiling |

| -------------------- | --------- | ---------------------- |

| implementer          | granted   | internal               |

| reviewer             | granted   | internal               |

| tester               | granted   | internal               |

| orchestrator         | granted   | confidential           |

| documentation-writer | granted   | internal               |

| project-manager      | denied    | not applicable         |



The Project Manager is explicitly denied retrieval because its current workflow responsibility does not require it.



\### Schema boundary



Agent handoffs are also constrained by:



```text

schemas/handoff.json

```



The schema requires:



\* `task\_id`

\* `summary`

\* `owner`



Each required field must be a non-empty string.



This gives the workflow a structural boundary before downstream agent execution continues.



\## Rejected Alternatives



\### Alternative 1: Expose all MCP operations to every role



Rejected because most roles do not need full storage or retrieval authority.



For example, a Reviewer needs to inspect state but should not be able to modify or delete it.



The calibration log also records a near-miss involving excessive delete access for the Implementer, demonstrating that over-broad grants create a real governance risk.



\### Alternative 2: Use one shared global MCP permission set



Rejected because storage and retrieval have different security concerns.



Storage controls state mutation, while retrieval controls information exposure.



Combining them into one undifferentiated permission model would make it harder to reason about risk and apply least privilege.



\### Alternative 3: Rely only on agent prompt instructions



Rejected because prompt-level rules are not sufficient enforcement.



An agent may misunderstand, ignore, or drift beyond instructions.



Operation-level allow-lists provide an independent enforcement boundary.



\### Alternative 4: Allow retrieval without classification ceilings



Rejected because successful tool authorization alone does not mean every role should see every document.



The calibration log records an Implementer request for confidential material that exceeded its internal ceiling.



Classification ceilings therefore protect data exposure independently from basic tool access.



\## Evidence



The current repository contains:



```text

mcp-servers/storage/allow-list.json

mcp-servers/retrieval/allow-list.json

mcp-servers/storage/schema.json

mcp-servers/retrieval/schema.json

schemas/handoff.json

```



The storage allow-list shows that only the Orchestrator may:



```text

delete\_entry

audit\_read

```



The Implementer may write and update state but may not delete it.



Reviewer, Tester, Project Manager, and Documentation Writer are limited to read-oriented storage access.



The retrieval allow-list records classification ceilings of:



```text

internal

```



for Implementer, Reviewer, Tester, and Documentation Writer, and:



```text

confidential

```



for the Orchestrator.



The Project Manager is explicitly denied retrieval.



The calibration log provides supporting evidence for these boundaries through near-misses involving:



\* over-broad Implementer delete access;

\* Reviewer tool overreach;

\* retrieval above a role's classification ceiling.



These events show that the allow-list design is responding to observed risks rather than hypothetical ones.



\## Consequences



\### Positive consequences



\* Tool access follows least privilege.

\* Destructive storage operations are tightly restricted.

\* Audit information is limited to the coordinating role.

\* Retrieval exposure is constrained by classification level.

\* Role responsibilities remain easier to reason about.

\* Policy violations can be tested independently of agent prompts.

\* MCP boundaries are visible in version-controlled configuration.



\### Negative consequences



\* Adding a new role requires explicit updates to allow-lists.

\* Permission configuration must remain synchronized with governance documentation.

\* Incorrect allow-list changes could unintentionally widen or block access.

\* Classification rules introduce additional configuration complexity.



\## Open Risks



1\. A future role may require a permission that is not currently represented.

2\. Governance documentation and allow-list configuration could drift apart.

3\. A classification label could be assigned incorrectly to retrieved content.

4\. Schema validation currently permits additional properties, which may allow fields beyond the minimum required handoff structure.

5\. MCP server implementation bugs could weaken enforcement even when configuration is correct.



These risks are mitigated through CI checks, policy tests, calibration review, schema validation, red-team testing, and required justification for permission widening.



\## Decision Summary



The capstone uses separate MCP storage and retrieval boundaries with explicit role-based allow-lists.



Storage permissions are granted by operation, retrieval permissions are constrained by role and classification ceiling, and handoffs are structurally validated before downstream execution.



This design keeps MCP capabilities narrow, auditable, and aligned with least-privilege governance.



