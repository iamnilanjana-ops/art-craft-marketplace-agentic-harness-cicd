# Agentic Engineer Capstone — Governed Multi-Agent Engineering Pipeline

This repository contains my Agentic Engineer Capstone: a forkable, containerized, governed multi-agent engineering pipeline that demonstrates safe agent orchestration, evaluation, governance, deterministic automation, and human checkpoints.

## Capstone Workflow

**Selected workflow:** AI-Assisted Code Review and Governance Pipeline

The pipeline coordinates specialized agents across an engineering workflow:

Developer Change → Orchestrator → Planner → Implementer → Reviewer → Tester → Human Approval → Project Manager

Each agent receives scoped context and only the tools required for its role. Governance controls, deterministic checks, evaluation gates, and human approval are used to keep the workflow safe, predictable, and auditable.

This capstone builds on artifacts developed throughout Modules 1–4, including the containerized agent harness, versioned agents and skills, persistent memory, MCP tooling, evaluation harness, governance policy, CI/CD guardrails, and deterministic conversion.

The repository includes:

- **Specialized agents** — Planner, Implementer, Reviewer, Tester, Project Manager, Documentation Writer, and Code Reviewer roles with scoped responsibilities.
- **Storage MCP server** — provides governed persistent project-state access with role-specific operation allow-lists and audit logging.
- **Retrieval MCP server** — provides semantic retrieval with project scoping, similarity thresholds, classification ceilings, and retrieval audit evidence.
- **Deterministic workflow steps** — handoff validation and routing move stable structural work out of model inference.
- **Evaluation harness** — holdout, regression, deterministic, rubric, retrieval, and policy evidence used to diagnose and verify workflow behavior.
- **Governance controls** — least-privilege permissions, read-only roles, data-classification ceilings, human-checkpoint rules, and red-team tests.
- **CI/CD guardrails** — policy, governed-file, pipeline-integrity, advisory-review, and audit-trail checks.
- **Persistent evidence** — transcripts, audit logs, calibration records, ADRs, and final capstone reports.

## Quick Start

Build and run locally:

```bash
docker build -t agentic_engineer_4 .

docker run -it --rm \
  -p 8501:8501 -p 8502:8502 \
  -e OPENROUTER_API_KEY=$OPENROUTER_API_KEY \
  -v "$PWD":/workspace \
  agentic_engineer_4
```
For the core capstone workflow, `OPENROUTER_API_KEY` is the required model credential.

Slack and Gmail credentials are optional and are only needed when exercising those integration-specific skills. Do not hardcode real credentials in the repository.

Or pull the pre-built image from DockerHub:

```bash
docker run -it --rm -p 8501:8501 -p 8502:8502 \
  -e SLACK_BOT_TOKEN=xoxb-your-token \
  -e SLACK_TEAM_ID=T0123456 \
  -v "$PWD":/workspace \
  heatonresearch/agentic_engineer_4:latest
```

Full setup with Slack and Gmail (reads credentials from your shell environment):

```bash
docker run -it --rm \
  -p 8501:8501 -p 8502:8502 \
  -e OPENROUTER_API_KEY=$OPENROUTER_API_KEY \
  -e SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN \
  -e SLACK_TEAM_ID=$SLACK_TEAM_ID \
  -v "$PWD":/workspace \
  -v "$HOME/.gmail-mcp":/root/.gmail-mcp \
  heatonresearch/agentic_engineer_4:latest
```

Place `credentials.json` (from Google Cloud Console) in `$PWD` before running. The Gmail MCP will trigger OAuth on first use and persist the token in `~/.gmail-mcp/`.

## Build

```bash
docker build -t agentic_engineer_4 .
```

Force a complete rebuild (no cached layers):

```bash
docker build --no-cache -t agentic_engineer_4 .
```
## Capstone Run

The capstone production-like workflow is implemented in `eval/orchestrator.py`.

The orchestrator coordinates the configured agent roles and writes an auditable transcript to `logs/`.

### Windows PowerShell

Set the OpenRouter API key in the current PowerShell session:

```powershell
$env:OPENROUTER_API_KEY = Read-Host -Prompt "Paste OpenRouter API key"
```

Verify only that the environment variable is populated:

```powershell
$env:OPENROUTER_API_KEY.Length
```

Do not print or commit the API key.

Run the production-like orchestration through the Module 4 Docker image:

```powershell
docker run --rm `
  -e OPENROUTER_API_KEY="$env:OPENROUTER_API_KEY" `
  -v "${PWD}:/workspace" `
  -w /workspace `
  agentic_engineer_4:latest `
  python eval/orchestrator.py `
    --task "Review a representative code change, validate the handoff, route the work to the appropriate agents, and produce an auditable final result." `
    --project "capstone-demo" `
    --out "logs/capstone-demo-run.json"
```

The example command writes its transcript to:

`logs/capstone-demo-run.json`

The preserved successful capstone evidence is:

- `logs/capstone-final-run-002.json` — successful final transcript
- `logs/capstone-final-run-002.log` — successful final audit log
- `logs/capstone-final-run-001.json` — preserved earlier integration-failure evidence

Do not overwrite the preserved final-run evidence when experimenting with the workflow.

### Current Runtime Status

The production-like capstone workflow has completed successfully using the configured `anthropic/claude-haiku-4.5` model.

The successful final run completed:

`Planner -> Implementer -> Reviewer -> Tester`

in 59.6 seconds.

The run exercised semantic retrieval, persistent-storage reads, an Implementer storage write, independent Reviewer verification, and Tester validation.

Final evidence:

- Transcript: `logs/capstone-final-run-002.json`
- Audit log: `logs/capstone-final-run-002.log`
- Run summary: `docs/run-summary.md`
- Impact report: `docs/capstone-impact-report.md`

All recorded evaluation items in the successful run were approved. This is evidence of a successful evaluated run, but it is not sufficient to claim a general 0% defect rate.

The available transcript does not establish a trustworthy full-pipeline model cost, so no unsupported end-to-end cost claim is made.

Human-checkpoint conditions are defined in `docs/governance-policy.md`; the successful final run did not require or trigger human escalation.

## Run

### With a local workspace (recommended)

```bash
# macOS / Linux
docker run -it --rm -p 8501:8501 -p 8502:8502 \
  -e SLACK_BOT_TOKEN=xoxb-your-token \
  -e SLACK_TEAM_ID=T0123456 \
  -v "$PWD":/workspace \
  agentic_engineer_4

# Windows (PowerShell)
docker run -it --rm -p 8501:8501 -p 8502:8502 `
  -e SLACK_BOT_TOKEN=xoxb-your-token `
  -e SLACK_TEAM_ID=T0123456 `
  -v "${PWD}:/workspace" `
  agentic_engineer_4
```

Files created or edited inside `/workspace` are saved to your local folder and persist after the container exits.

### Without a local workspace

```bash
docker run -it --rm -p 8501:8501 agentic_engineer_4
```

Any files created inside the container will be lost when it exits.

---

## MCP Servers

MCP (Model Context Protocol) servers extend Claude Code so that prompts can take real-world actions — posting to Slack, reading email, etc. — without writing any extra code. Both servers are pre-installed as global npm packages and pre-configured in `/root/.claude/settings.json` inside the image.

### Slack MCP Server

**Package:** `@modelcontextprotocol/server-slack`

**Required environment variables** (pass with `-e` at `docker run`):

| Variable          | Description                                           |
| ----------------- | ----------------------------------------------------- |
| `SLACK_BOT_TOKEN` | Bot User OAuth Token from your Slack App (`xoxb-…`)   |
| `SLACK_TEAM_ID`   | Your Slack workspace ID (found in workspace settings) |

**Getting a Slack Bot Token:**

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app.
2. Under **OAuth & Permissions**, add Bot Token Scopes: `channels:read`, `chat:write`, `channels:history`, `users:read`.
3. Install the app to your workspace and copy the **Bot User OAuth Token**.
4. Copy your workspace's **Team ID** from the workspace URL or settings.

**What it enables:** Claude Code prompts can list channels, read message history, post messages, and look up users in your Slack workspace.

### Gmail MCP Server

**Package:** `@gongrzhe/server-gmail-autoauth-mcp`

**Setup (OAuth):**

1. Go to [Google Cloud Console](https://console.cloud.google.com/) and create a project.
2. Enable the **Gmail API**.
3. Create OAuth 2.0 credentials (Desktop App type) and download `credentials.json`.
4. Place `credentials.json` in your workspace directory (mounted at `/workspace`).
5. On first use, the MCP server will open an OAuth flow and save a token. To persist the token across container restarts, mount the credentials directory:

```bash
docker run -it --rm -p 8501:8501 \
  -v "$PWD":/workspace \
  -v "$HOME/.gmail-mcp":/root/.gmail-mcp \
  agentic_engineer_4
```

**What it enables:** Claude Code prompts can read, search, and send Gmail messages on behalf of the authenticated user.

---

## Skills

Skills are custom slash commands invoked by typing `/skill-name` inside a Claude Code session. Claude Code supports two ways to define skills, and this image uses both.

### Pre-installed Skills

| Skill                 | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| `/send-slack-message` | Send a message to a Slack channel via the Slack MCP server  |
| `/check-gmail`        | Retrieve and summarize recent unread Gmail messages         |
| `/send-email`         | Draft and send an email via the Gmail MCP server            |
| `/summarize-session`  | Generate a bullet-point summary of the current work session |
| `/rebuild-and-deploy` | Rebuild the Docker image and push it to DockerHub           |

---

### SKILL.md files

Each skill lives in its own Markdown file at `.claude/skills/<skill-name>/SKILL.md`. Inside the container these are placed at `/root/.claude/skills/`.

```
skills/
  send-slack-message/SKILL.md
  check-gmail/SKILL.md
  send-email/SKILL.md
  summarize-session/SKILL.md
```

**When to use this method:**

- The skill prompt is more than a sentence or two.
- The skill has multiple steps, conditional logic, or examples that benefit from formatting.
- You want each skill in its own file for easier editing and version control.
- You are building skills that will be shared or maintained over time.

To add a skill, create a new directory and SKILL.md file:

```bash
mkdir -p skills/my-skill
cat > skills/my-skill/SKILL.md << 'EOF'
Description of what this skill does.

Steps:
1. First step Claude should take.
2. Second step.
3. Confirm result to the user.
EOF
```

Then rebuild the image so the file is copied into `/root/.claude/skills/`:

```bash
docker build -t agentic_engineer_4 .
```

**Adding a skill at runtime (no rebuild required):**

You can also add a skill directly inside a running container without rebuilding the image. The full path inside the container is:

```
/root/.claude/skills/<skill-name>/SKILL.md
```

For example:

```bash
mkdir -p /root/.claude/skills/my-skill
nano /root/.claude/skills/my-skill/SKILL.md
```

Note: since the container is run with `--rm`, any skills added this way will be lost when the container exits. To persist them, add them to the `skills/` directory in this repo and rebuild.

---

## Agents

The capstone uses specialized agents with scoped responsibilities rather than one unrestricted general-purpose agent.

Agent definitions are version-controlled in the `agents/` directory. Runtime permissions are further constrained by the governance policy, MCP allow-lists, container permissions, and orchestration rules.

### Governed Agents

| Agent | Primary responsibility | Access model |
| --- | --- | --- |
| `planner` | Analyze the task, retrieve relevant project context, and prepare the implementation plan | Read-oriented, scoped retrieval |
| `implementer` | Perform approved implementation work and write permitted project state | Read/write within approved scope |
| `reviewer` | Independently review implementation results and report findings | Read-only |
| `tester` | Validate implementation behavior and acceptance criteria | Read-only for tracked project state |
| `project-manager` | Produce project-facing summaries and coordination output | Advisory/read-only |
| `documentation-writer` | Prepare documentation using approved project information | Read-only with scoped storage access |
| `code-reviewer` | Review code changes for quality, security, and maintainability | Advisory/read-only |

The Orchestrator coordinates the workflow and applies routing, validation, governance, and evaluation controls around these specialized roles.

### Production-Like Agent Path

The successful final capstone run exercised:

`Planner -> Implementer -> Reviewer -> Tester`

The Planner gathered relevant evidence, the Implementer performed the permitted state update, the Reviewer independently evaluated the result, and the Tester validated the implementation evidence.

The successful run is preserved in:

- `logs/capstone-final-run-002.json`
- `logs/capstone-final-run-002.log`
- `docs/run-summary.md`

### Agent Governance

Agents do not receive unrestricted access simply because a tool is available.

Access is controlled through:

- role-specific MCP allow-lists;
- data-classification ceilings;
- read-only workspace boundaries for advisory roles;
- deterministic handoff validation;
- policy and evaluation tests;
- human-checkpoint rules for higher-risk actions.

For example, the `documentation-writer` role is permitted to read approved stored project information but is not permitted to call `write_entry`. An attempted unauthorized write was denied by the storage MCP server and recorded as `authorization_denied` in the audit log.

See:

- `docs/governance-policy.md`
- `docs/routing-and-tool-grant-map.md`
- `eval/red-team-results.md`
- `logs/storage-audit-log.jsonl`

### Adding a New Agent

1. Create a Markdown file in `agents/` with a YAML frontmatter block:

```markdown
---
name: my-agent
description: >
  One or two sentences describing when Claude Code should invoke this agent.
tools: Read, Grep, Glob, Bash
model: inherit
permissionMode: default
---

Your agent prompt goes here.
```

2. Rebuild the image:

```bash
docker build -t agentic_engineer_4 .
```

**Adding an agent at runtime (no rebuild required):**

```bash
mkdir -p /root/.claude/agents
nano /root/.claude/agents/my-agent.md
```

Note: agents added this way are lost when the container exits (since it runs with `--rm`). Add them to `agents/` in this repo and rebuild to persist them.

### Agent File Format

| Field            | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| `name`           | Identifier used to reference the agent                              |
| `description`    | Tells Claude Code when to invoke the agent (be specific)            |
| `tools`          | Comma-separated list of tools the agent may use                     |
| `model`          | Model to use (`inherit` uses the same model as the parent session)  |
| `permissionMode` | `default` respects normal permission prompts; `allowAll` skips them |

---

## Running Subagent Containers

`scripts/run-agent.sh` (macOS/Linux) and `scripts/run-agent.ps1` (Windows) launch a subagent container enforcing the governance policy for the given role. Pass the role name as the first argument; any additional arguments are forwarded to the container.

**macOS / Linux:**

```bash
# Read-only workspace, no memory mount (reviewer, tester, project-manager)
./scripts/run-agent.sh reviewer

# Read-write workspace, memory mounted (implementer, orchestrator)
./scripts/run-agent.sh implementer

# Pass a command to run inside the container
./scripts/run-agent.sh tester python3 -m pytest eval/ -v
```

**Windows (PowerShell):**

```powershell
# Read-only workspace, no memory mount
.\scripts\run-agent.ps1 reviewer

# Read-write workspace, memory mounted
.\scripts\run-agent.ps1 implementer

# Pass a command to run inside the container
.\scripts\run-agent.ps1 tester python3 -m pytest eval/ -v
```

Override the default image (`launchcode-agentic:module4`) with the `AGENT_IMAGE` environment variable:

```bash
AGENT_IMAGE=heatonresearch/agentic_engineer_4:latest ./scripts/run-agent.sh implementer
```

```powershell
$env:AGENT_IMAGE = 'heatonresearch/agentic_engineer_4:latest'
.\scripts\run-agent.ps1 implementer
```

---

## Gmail API Credentials (Python SDK)

In addition to the MCP server, the Python `google-api-python-client` library is available for direct API use in your code.

Place `credentials.json` (from Google Cloud Console) in your workspace directory. On first run it triggers OAuth and saves `token.json`. Reference it in code as:

```python
from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
```

Keep both files out of source control:

```
# .gitignore
credentials.json
token.json
```

---

## Running Streamlit Apps

From inside the container:

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Running Unit Tests

The test suite runs inside the Docker container, which has all dependencies pre-installed. Build the image first if you haven't already:

```bash
docker build -t agentic_engineer_4 .
```

### Run all eval tests

```bash
docker run --rm \
  -v "$PWD":/workspace \
  agentic_engineer_4 \
  python3 -m pytest eval/ -v
```

### Run specific test suites

```bash
# Deterministic router and handoff-validator unit tests (fast, no external deps)
docker run --rm -v "$PWD":/workspace agentic_engineer_4 \
  python3 -m pytest eval/test_deterministic_router.py eval/test_deterministic_step.py -v

# Full deterministic suite including CLI subprocess and directory-structure checks
docker run --rm -v "$PWD":/workspace agentic_engineer_4 \
  python3 -m pytest eval/test_deterministic.py -v

# Governance policy / allow-list / skill-scope enforcement tests
docker run --rm -v "$PWD":/workspace agentic_engineer_4 \
  python3 -m pytest eval/test_policy.py -v

# Rubric and documentation consistency checks
docker run --rm -v "$PWD":/workspace agentic_engineer_4 \
  python3 -m pytest eval/test_rubric_suite.py -v
```

### What each suite checks

| Suite | What it tests |
| --- | --- |
| `test_deterministic_router.py` | `scripts/route_task_deterministic.py` path-to-role routing logic |
| `test_deterministic_step.py` | `scripts/validate_handoff_deterministic.py` field validation logic |
| `test_deterministic.py` | CLI invocation of the validator, directory structure, governance-policy content |
| `test_policy.py` | Storage allow-list, retrieval allow-list, skill-scope files, and container permissions all agree with `docs/governance-policy.md` |
| `test_rubric_suite.py` | Rubric and documentation consistency checks — confirms ADR and CI design docs contain required content |

### Notes

- `eval/test_policy.py` reads `.skills/*.md` for skill-scope enforcement. The `.skills/` directory is currently empty — add per-role skill scope files there as you build out the governance lesson content.
- Tests that check directory structure (`.agents`, `.skills`, `docs/adr`, etc.) expect those directories to exist in the bind-mounted workspace. They are created automatically when the container runs without a bind-mount.
- `scripts/run-reviewer.py` is a safe sample that does **not** call a live LLM. It writes a deterministic advisory review so the CI workflow can be exercised without API spend.
- Runtime logs belong under `logs/` and are gitignored.
- Configure branch protection so `Policy Test Suite`, `Evaluation Harness`, and `Pipeline Integrity Check` are required status checks before merge.

---

## Build & Deploy to DockerHub

This section covers the full workflow for building the image and publishing it to DockerHub so students can pull it without building locally.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- A DockerHub account (free at [hub.docker.com](https://hub.docker.com))
- Logged in to DockerHub on your machine:

```bash
docker login
```

### Step 1 — Build and tag for DockerHub

Build the image and tag it with your DockerHub username and repository name. Replace `heatonresearch` with your DockerHub username if different.

```bash
docker build -t heatonresearch/agentic_engineer_4:latest .
```

To tag a specific version number alongside `latest` (recommended so students can pin to a known-good version):

```bash
docker build \
  -t heatonresearch/agentic_engineer_4:latest \
  -t heatonresearch/agentic_engineer_4:3.0 .
```

Force a full rebuild ignoring all cached layers:

```bash
docker build --no-cache \
  -t heatonresearch/agentic_engineer_4:latest \
  -t heatonresearch/agentic_engineer_4:3.0 .
```

### Step 2 — Push to DockerHub

```bash
docker push heatonresearch/agentic_engineer_4:latest
docker push heatonresearch/agentic_engineer_4:3.0
```

Both tags must be pushed separately. The `latest` tag is what students get by default when they don't specify a version.

### Step 3 — Verify the image is public

Visit `https://hub.docker.com/r/heatonresearch/agentic_engineer_4` and confirm the repository visibility is set to **Public** so students can pull without logging in.

### Pulling the image (students)

Once published, students can run the image directly without cloning the repo or building anything:

```bash
docker run -it --rm -p 8501:8501 -p 8502:8502 \
  -e SLACK_BOT_TOKEN=xoxb-your-token \
  -e SLACK_TEAM_ID=T0123456 \
  -v "$PWD":/workspace \
  heatonresearch/agentic_engineer_4:latest
```
