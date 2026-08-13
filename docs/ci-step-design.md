# CI Agentic Step Design

## Step: Policy test suite

- Does: Confirms `docs/governance-policy.md`, MCP allow-lists, skill scopes, and container permissions agree.
- Input: whole repository.
- Produces: `policy-report.json` artifact.
- Classification: gating, permanent.
- Time limit: 5 minutes.
- Credentials: none.

## Step: eval-gate (Evaluation Harness)

- Does: Runs deterministic and rubric checks on agent-affecting changes.
- Input: whole repository plus changed-file classifier output.
- Produces: `deterministic-report.json` and `rubric-report.json`.
- Classification: gating, conditional.
- Time limit: 10 minutes.
- Credentials: `ANTHROPIC_API_KEY` only for model-backed rubric runs.

## Step: agent-review (Advisory Code Review)

- Does: Reviewer subagent scores changed files and provides advisory review output.
- Input: changed files from the shared classifier.
- Produces: advisory review artifacts, including reviewer output and audit evidence.
- Classification: advisory; not a required status check.
- Time limit: 15 minutes.
- Credentials: `ANTHROPIC_API_KEY`, scoped to the reviewer step only.

## Step: Audit trail

- Does: Combines policy, evaluation harness, agent-review, and pipeline-integrity artifacts into one durable JSON trail.
- Input: CI artifacts and results from earlier jobs.
- Produces: `ci-audit-trail-[sha].json` artifact.
- Classification: required operational evidence; always runs.
- Credentials: none for artifact generation.

## Step: Pipeline Integrity Check

- Does: Inspects `.github/workflows/ci.yml` to confirm that required CI/CD guardrails have not been weakened or removed.
- Input: the workflow definition in `.github/workflows/ci.yml`.
- Produces: `pipeline-integrity-report.json`, which records the integrity check results and is uploaded as a CI artifact.
- Classification: gating and permanent.
- Rationale: This check protects an invariant that must always hold. A pull request must not be able to weaken or remove the same CI/CD guardrails that are supposed to evaluate it.
- Checks:
  - Confirms `policy-gate` and `eval-gate` have not been weakened with `continue-on-error: true`.
  - Confirms `audit-trail` still runs with `if: always()`.
  - Confirms the `change-type-check` classifier job still exists.
- Required Status Check: `Pipeline Integrity Check` is configured as a required status check for the `main` branch.
- Audit Trail Wiring: `pipeline-integrity` is included in the `audit-trail` job's `needs:` list so its result is part of the durable CI record.
- Artifact: `pipeline-integrity-report.json`; the report identifies the job, display name, gating classification, overall status, and individual guardrail check results.
- Credentials: none. This is a deterministic workflow integrity check and does not require an API key.
- Verified: On the throwaway `test-pipeline-integrity` branch, I deliberately added `continue-on-error: true` to `policy-gate`. The Pipeline Integrity Check failed as expected and identified the weakened gate. The Audit Trail still ran and completed, preserving evidence from the failed run. After removing the temporary weakening, the next CI run completed successfully with the Pipeline Integrity Check and the required CI guardrails restored.