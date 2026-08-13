\# ADR-007: Least-Privilege Governance Policy



\## Status



Accepted



\## Context



The multi-agent engineering pipeline allows AI agents to interact with project state, retrieval systems, tools, skills, and repository resources.



Without explicit governance, an agent could receive broader access than its task requires, modify information it should only inspect, retrieve data above its intended classification level, or activate tools outside its assigned responsibility.



Calibration identified concrete near-miss patterns, including:



1\. An Implementer nearly receiving destructive `delete\_entry` access.

2\. A Reviewer nearly triggering the `run-tests` skill despite being a read-only advisory role.

3\. An Implementer requesting a document classified above its `internal` retrieval ceiling.



These observations showed that role expectations written only in prompts were not sufficient. Governance needed to be explicit, versioned, testable, and enforced independently of agent behavior.



\## Decision



Adopt a deny-by-default, least-privilege governance policy for every agent role.



The governing principle is:



> Every role starts with no access. Every permission must be explicitly granted and justified. Anything not explicitly granted is denied.



The policy is version-controlled in:



```text

docs/governance-policy.md

```



Governance applies across multiple dimensions:



\* MCP server and operation access

\* Skill activation

\* Data-classification ceilings

\* Agent autonomy

\* Human checkpoints

\* Container permissions

\* Persistent-memory access

\* Role-specific state mutation permissions



\## Role-Based Governance



Permissions attach to stable roles rather than temporary agent instances.



This allows governance rules to remain consistent across repeated workflow executions.



\### Orchestrator



The Orchestrator receives broader coordination privileges because it owns workflow-level orchestration and auditing.



It may access destructive storage and audit operations that are denied to narrower subagents.



\### Implementer



The Implementer may modify approved project state but does not receive destructive delete authority.



Its retrieval ceiling is `internal`.



Higher-risk actions outside its normal implementation scope require a human checkpoint.



\### Reviewer



The Reviewer is advisory and read-only.



It may inspect relevant state and retrieve internal context but may not modify stored project state or activate implementation-oriented tools.



\### Tester



The Tester may execute approved testing responsibilities and inspect required context but may not modify tracked project state.



\### Project Manager



The Project Manager receives only the access required for project descriptions and summaries.



Retrieval is denied because the current workflow does not require it.



\### Documentation Writer



The Documentation Writer receives read-oriented storage access and internal retrieval access for documentation tasks.



It does not inherit the broader authority of the Orchestrator or Implementer.



\## Permission Widening



Permissions may not be expanded silently.



To widen access, the governance policy requires a pull request containing:



1\. the proposed permission;

2\. a concrete justification;

3\. confirmation that the new permission does not conflict with a known calibration near-miss.



This prevents gradual access creep and creates reviewable evidence for governance changes.



\## Human Checkpoints



Human review is required when an action exceeds the safe autonomy assigned to a role.



Examples include:



\* an Implementer attempting shell activity outside the approved testing path;

\* writes outside the intended feature scope;

\* a Reviewer attempting to perform state-changing work;

\* a Tester attempting to modify tracked repository state;

\* a request for permissions beyond the role's approved policy.



The system should escalate these cases rather than automatically broadening agent authority.



\## Enforcement



Governance is not implemented only as written guidance.



The repository includes enforcement mechanisms and evidence such as:



```text

mcp-servers/storage/allow-list.json

mcp-servers/retrieval/allow-list.json

eval/test\_policy.py

eval/test\_governed\_files.py

eval/enforcement-verification.md

eval/red-team-prompts.md

eval/red-team-results.md

.github/workflows/ci.yml

```



These artifacts allow policy assumptions to be checked automatically and tested against attempted bypasses.



\## Rejected Alternatives



\### Alternative 1: Trust agent prompts to enforce permissions



Rejected because prompts describe expected behavior but do not provide an independent authorization boundary.



A model may misunderstand or drift beyond instructions.



Tool-level enforcement is therefore required.



\### Alternative 2: Give every agent broad permissions for convenience



Rejected because convenience does not justify unnecessary authority.



An error by a broadly privileged agent would have a larger blast radius.



The Implementer delete-access near-miss provides direct evidence of this risk.



\### Alternative 3: Use identical permissions for every role



Rejected because roles have different responsibilities.



A Reviewer does not need write access, a Project Manager does not currently need retrieval, and only the Orchestrator requires audit and destructive storage authority.



\### Alternative 4: Allow agents to request and automatically receive additional permissions



Rejected because an agent should not be able to authorize its own privilege escalation.



Permission widening requires explicit review and justification.



\### Alternative 5: Treat governance as a one-time configuration



Rejected because agent roles, tools, workflow requirements, and failure patterns can evolve.



Governance must therefore remain versioned, testable, and reviewable.



\## Evidence



The governance policy records least privilege as the default rule.



The storage allow-list restricts:



```text

delete\_entry

audit\_read

```



to the Orchestrator.



The retrieval allow-list enforces classification ceilings, including:



\* `internal` for Implementer, Reviewer, Tester, and Documentation Writer;

\* `confidential` for Orchestrator;

\* retrieval denied for Project Manager.



The calibration log records three concrete near-misses that informed these boundaries.



The repository also includes policy tests, governed-file tests, enforcement verification, red-team prompts and results, and CI/CD integration.



Together, these artifacts show that governance decisions are connected to observed risks and executable controls.



\## Consequences



\### Positive consequences



\* Agent permissions remain narrow and explainable.

\* The blast radius of an agent failure is reduced.

\* Review and testing roles preserve independence.

\* Sensitive retrieval is limited by classification level.

\* Permission changes leave an auditable decision trail.

\* Governance violations can be tested in CI.

\* Human accountability remains available for higher-risk decisions.



\### Negative consequences



\* Governance configuration requires ongoing maintenance.

\* New roles or tools require explicit policy updates.

\* Legitimate work may occasionally be blocked until permissions are reviewed.

\* Multiple policy artifacts must remain synchronized.



\## Open Risks



1\. Policy documentation and executable allow-lists could drift apart.

2\. A future tool could introduce capabilities not covered by the current policy.

3\. A classification label could be incorrect or incomplete.

4\. Branch-protection or CI settings could be weakened outside the repository files.

5\. Authorized users with bypass privileges may still circumvent required pull-request or status-check workflows.



The final risk is particularly important because repository push output has shown that protected-branch rules can be bypassed by an authorized account. The capstone should therefore distinguish between repository-level governance controls and external platform permissions when discussing enforcement guarantees.



These risks are mitigated through policy tests, pipeline-integrity checks, red-team exercises, explicit access reviews, human checkpoints, and audit evidence.



\## Decision Summary



The capstone adopts deny-by-default, role-based, least-privilege governance.



Permissions are explicit, scoped to role responsibilities, constrained by data classification and container boundaries, and backed by executable allow-lists and tests.



Privilege widening requires review rather than autonomous agent approval.



This design provides enforceable boundaries around agent behavior while preserving human accountability for higher-risk actions.



