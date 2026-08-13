\# ADR-004: Persistent Memory Layout and Scope



\## Status



Accepted



\## Context



The multi-agent engineering workflow needs persistent state and reusable reference knowledge across runs, but memory must not become an unrestricted shared context that leaks information between roles or sessions.



The repository already contains a persistent memory area under:



```text

.memory/

```



Current artifacts include:



\* `storage.db`

\* `storage-audit.log`

\* `.memory/reference/`



The reference directory contains reusable project and lesson knowledge such as:



\* API and spreadsheet references

\* cost information

\* CSV format decisions

\* error codes

\* feature notes

\* security guidance

\* governance lessons

\* memory-scope guidance



The design therefore needs to distinguish persistent project state from reusable reference material and to control which roles are allowed to mount or use that memory.



\## Decision



Use a layered memory layout with persistent project state separated from reference knowledge.



\### Persistent project state



The SQLite database:



```text

.memory/storage.db

```



stores persistent workflow or project state.



Changes to persistent storage are traceable through:



```text

.memory/storage-audit.log

```



\### Reference knowledge



Reusable reference documents are stored under:



```text

.memory/reference/

```



These files contain project decisions, feature notes, security guidance, lessons learned, and other context that may be retrieved when a role requires it.



\### Role-scoped mounting



Persistent memory is not mounted for every role.



Roles that require stateful implementation context may receive memory access, while read-only or advisory roles can run without the persistent memory mount.



For example, the current governance design records the Implementer with:



```text

workspace: read-write

memory: mounted

```



while the Reviewer and Tester operate with memory omitted.



This reduces unnecessary exposure of persistent state.



\### Separation principle



The memory design separates:



1\. \*\*Persistent project state\*\*

2\. \*\*Reusable reference knowledge\*\*

3\. \*\*Temporary role context\*\*

4\. \*\*Agent instructions and skills\*\*



Persistent memory is reserved for information that should survive across runs. Temporary task-specific context should remain in the current workflow handoff rather than being written into persistent storage automatically.



\## Rejected Alternatives



\### Alternative 1: Give every agent the same persistent memory mount



Rejected because not every role requires persistent state.



A Reviewer or Tester only needs enough context to inspect and report. Giving all roles access to the same persistent memory would increase the risk of unnecessary data exposure and cross-role context leakage.



\### Alternative 2: Store all knowledge directly in the agent prompt



Rejected because prompts are not a good durable store for evolving project knowledge.



Embedding all prior decisions and reference material into prompts would increase context size, make updates harder to track, and reduce separation between stable instructions and changing project knowledge.



\### Alternative 3: Store everything in one undifferentiated database



Rejected because reference documents and mutable workflow state serve different purposes.



Keeping reusable references in a distinct directory makes them easier to inspect, version, retrieve, and reason about separately from mutable operational state.



\### Alternative 4: Use only session-local memory



Rejected because the workflow needs continuity across runs.



Project decisions, lessons, and reusable reference material would otherwise have to be reconstructed repeatedly.



\## Evidence



The current repository contains:



```text

.memory/storage.db

.memory/storage-audit.log

.memory/reference/

```



The reference directory includes multiple durable knowledge artifacts, including governance, retrieval, security, feature, and memory-scope lessons.



The repository also contains:



```text

.memory/reference/lesson-memory-scope-check.md

```



which documents memory-scope concerns.



The agent-run script includes logic for mounting persistent memory selectively rather than treating it as universally available.



Governance documentation also differentiates role-level memory behavior. The Implementer may run with memory mounted, while read-only roles such as Reviewer and Tester operate without persistent memory.



This supports the principle that persistent memory should be scoped to role responsibility rather than globally exposed.



\## Consequences



\### Positive consequences



\* Persistent state survives across workflow runs.

\* Reusable reference knowledge remains inspectable and separate from mutable state.

\* Audit logging improves traceability of persistent-memory operations.

\* Role-specific mounting reduces unnecessary memory exposure.

\* Temporary task context does not automatically become long-term project memory.

\* The design supports least privilege.



\### Negative consequences



\* The architecture is more complex than using one shared memory store.

\* Developers must decide whether new information belongs in persistent state, reference knowledge, or temporary context.

\* Reference content can become stale if it is not reviewed.

\* Persistent memory must be sanitized before public submission.



\## Open Risks



1\. Reference documents may become outdated and continue to influence retrieval.

2\. Incorrect role configuration could mount persistent memory for a role that should not receive it.

3\. Sensitive information could accidentally be written into persistent storage.

4\. Audit logs themselves may contain operational information that requires sanitization.

5\. SQLite storage is sufficient for the current capstone scale but may not be appropriate for larger concurrent production workloads.



These risks are mitigated through role-scoped access, governance policy, audit evidence, retrieval validation, and final sanitization review.



\## Decision Summary



The capstone uses a layered persistent-memory design.



Mutable workflow state is stored in `.memory/storage.db`, persistent operations are recorded in `.memory/storage-audit.log`, and reusable knowledge is kept separately in `.memory/reference/`.



Memory is not globally mounted. Access is scoped according to role responsibility, supporting least privilege and reducing cross-role context leakage.



