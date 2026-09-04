# Orchestration Diagram

```mermaid
flowchart TD
    A[Orchestrator] --> B[Planner]
    B --> C[Implementer]
    C --> D[Reviewer]
    D --> E[Tester]
    E --> F{Human Approval}

    F -->|Approve| G[Project Manager / Completion]
    F -->|Reject| H[Completion Blocked]
    F -->|Pending| H

    D -->|Reviewer Conflict| I[Escalate to Human]

    B --> J[Scoped MCP Tools]
    C --> J
    D --> J
    E --> J

    J --> K[Policy and Evaluation Gates]
```

## Workflow

The default governed workflow is:

**Planner → Implementer → Reviewer → Tester → Human Approval → Completion**

Automated review and testing do not authorize final completion by themselves. After the Tester finishes, the workflow records an explicit human decision.

- `approve` → completion is authorized.
- `reject` → completion is blocked.
- `pending` → completion remains blocked.
- Conflicting reviewer verdicts trigger escalation to a human.

The orchestrator also applies scoped tool grants, deterministic validation, token budgets, request timeouts, bounded retries, and audit/transcript logging.

The Human Approval gate ensures that successful automated agent output cannot silently become final workflow completion without an explicit human decision.