# Capstone Tool-Evolution Drill

## Purpose

This drill tests whether the governance and evaluation system can detect a meaningful tool-permission regression and confirm recovery after the issue is fixed.

## Change Attempted

The storage MCP allow-list was changed so that the `documentation-writer` role temporarily lost its previously granted `read_entry` permission.

The change was made in:

`mcp-servers/storage/allow-list.json`

This simulated a tool-evolution or permission-change event that could occur when governance configuration is modified.

## Baseline

Before the change, the policy test suite was executed inside the project Docker container.

Command:

```powershell
docker run --rm `
  -v "${PWD}:/workspace" `
  -w /workspace `
  agentic_engineer_4:latest `
  pytest eval/test_policy.py -v
```

Baseline result:

```text
6 passed in 0.18s
```

All governance and policy-alignment checks were passing before the permission change.

## Regression Introduced

The `documentation-writer` role was removed from the `read_entry` allow-list.

Before:

```json
"read_entry": [
  "implementer",
  "reviewer",
  "tester",
  "project-manager",
  "orchestrator",
  "documentation-writer"
]
```

Temporary changed configuration:

```json
"read_entry": [
  "implementer",
  "reviewer",
  "tester",
  "project-manager",
  "orchestrator"
]
```

## What Broke

After the permission change, the policy suite was run again.

Result:

```text
FAILED eval/test_policy.py::test_documentation_writer_policy_matches_enforcement

1 failed, 5 passed in 0.27s
```

The failing test showed that executable enforcement no longer matched the documented governance policy.

The regression was therefore detected automatically rather than through manual inspection.

## What the Evaluation System Detected

The policy test specifically detected a mismatch between:

- the documented role policy; and
- the storage MCP allow-list.

This demonstrates that governance configuration changes are testable and that permission drift can be caught before being treated as a valid system state.

## Fix

The `documentation-writer` role was restored to the `read_entry` allow-list.

Restored configuration:

```json
"read_entry": [
  "implementer",
  "reviewer",
  "tester",
  "project-manager",
  "orchestrator",
  "documentation-writer"
]
```

## Final Verification

The same policy suite was executed after the fix.

Final result:

```text
6 passed in 0.21s
```

All policy checks passed again.

## Outcome

The drill demonstrated the full self-improving loop:

1. Start from a passing baseline.
2. Change a tool permission.
3. Introduce a governance regression.
4. Run the evaluation suite.
5. Detect the regression automatically.
6. Restore the correct permission.
7. Rerun the evaluation.
8. Confirm the regression is resolved.

## Evidence Summary

| Stage | Result |
| --- | --- |
| Baseline | 6 passed |
| Permission changed | 1 failed, 5 passed |
| Permission restored | 6 passed |

## Conclusion

The tool-evolution drill shows that the pipeline does not rely only on written governance documentation.

A real permission change created a detectable mismatch, the policy test suite caught the problem, and the restored configuration returned the system to a passing state.

This provides evidence that the capstone evaluation harness can catch governance regressions caused by tool or permission evolution.