# Python Agent Runbook — Inbound Lead Triage

## 1. Purpose

The Python Lead Qualification Agent supports the Inbound Lead Triage workflow by validating structured lead data, calculating a deterministic lead-quality score, and producing a structured qualification result for use in the Slack-based workflow.

Python is used because the scoring and validation logic is easier to maintain, test, and regression-check in code than as a large set of Zapier conditions.

## 2. Main Files

### lead_qualification_util_v2.py

Contains the capstone-aligned V2 lead qualification logic.

It:

- Validates required lead fields
- Calculates deterministic component scores
- Calculates a total lead-quality score
- Assigns an ICP fit assessment
- Assigns a suggested response priority
- Returns validation status and validation issues
- Generates a readable scoring reason
- Can be run directly with a sample lead for standalone verification

### lead_qualification_util.py

Contains the earlier qualification implementation based on budget, business need, company size, and purchase timeline.

This file is retained as earlier implementation evidence, but the capstone presentation and final V2 scoring model use `lead_qualification_util_v2.py`.

### slack_lead_worker.py

Runs the Slack worker.

It:

- Connects to Slack
- Monitors Slack messages
- Detects relevant `NEW LEAD` posts
- Passes structured lead data to the qualification utility
- Posts the qualification result back to the Slack thread

### test_lead_qualification.py

Contains automated regression tests for representative qualification outcomes, including:

- Qualified / strong-fit behavior
- Needs Review / moderate-fit behavior
- Not Qualified / low-fit behavior
- Invalid-input behavior

## 3. Required Python Dependency

The Slack worker uses:

```text
slack-sdk==3.44.0
```

The regression suite also requires `pytest`.

## 4. Credentials

The Slack worker requires:

- `SLACK_APP_TOKEN`
- `SLACK_BOT_TOKEN`

Credentials should be loaded from environment variables and must never be hardcoded into submitted Python source files or exposed in screenshots.

If a local credential file is used during development, it must not be committed to source control or included in submission evidence.

## 5. Test the V2 Agent

Run the capstone-aligned V2 scoring utility:

```powershell
python lead_qualification_util_v2.py
```

The built-in sample lead is:

- Company: Example SaaS Company
- Company Size: 500
- Use Case: security automation
- Industry: saas
- Urgency Signals: immediate

The V2 agent returns a structured result containing:

- `company_name`
- `lead_quality_score`
- `icp_fit_assessment`
- `suggested_response_priority`
- `validation_status`
- `validation_issues`
- `scoring_reason`

## 6. Run Regression Tests

Run:

```powershell
python -m pytest test_lead_qualification.py -v
```

Current verified result:

```text
4 passed
```

All regression tests should pass before scoring logic is changed or the workflow is demonstrated.

## 7. Start the Slack Worker

Set the Slack credentials in the environment and run:

```powershell
python slack_lead_worker.py
```

A successful startup confirms that the credentials were loaded and the worker connected to Slack.

Keep the terminal open while the worker is running.

## 8. Agent Execution Flow

The workflow is:

1. Slack receives a structured `NEW LEAD` message.
2. The Slack worker detects the message.
3. Lead fields are parsed or passed to the V2 scoring utility.
4. Required fields are validated.
5. Invalid inputs are returned safely without a normal score.
6. Valid leads are scored across four deterministic dimensions.
7. The total lead-quality score is calculated.
8. ICP fit and response priority are assigned.
9. A readable scoring explanation is generated.
10. The structured result is returned to the workflow and posted to the Slack thread.

## 9. V2 Scoring Rules

The capstone-aligned V2 score has four dimensions:

- **Company Size:** up to 35 points
- **Use Case:** up to 25 points
- **Industry:** up to 20 points
- **Urgency Signals:** up to 20 points

Maximum score: **100 points**

### Company Size

- 1000+ employees = 35
- 500–999 = 30
- 200–499 = 25
- 50–199 = 15
- Below 50 = 5

### Use Case

Recognized keywords contribute points, capped at 25.

Examples include:

- automation = 25
- security = 25
- compliance = 25
- integration = 20
- AI = 20
- analytics = 15
- productivity = 10

### Industry

- software = 20
- SaaS = 20
- fintech = 20
- healthcare = 15
- education = 10
- retail = 10
- other = 5

### Urgency Signals

Recognized urgency phrases contribute points, capped at 20.

Examples include:

- immediate = 20
- ASAP = 20
- high = 20
- this month = 15
- 1–3 months = 10
- exploratory = 5
- low = 5

## 10. ICP Fit and Response Priority

### ICP Fit

- 70–100 = **Strong Fit**
- 40–69 = **Moderate Fit**
- 0–39 = **Low Fit**

### Suggested Response Priority

- 70–100 = **High**
- 40–69 = **Medium**
- 0–39 = **Low**

## 11. Validation

Required V2 fields are:

- `company_name`
- `company_size`
- `use_case`
- `industry`
- `urgency_signals`

If required information is missing, the V2 agent returns an invalid result instead of guessing or producing a normal qualification score.

Example invalid result:

```text
lead_quality_score: 0
icp_fit_assessment: Low Fit
suggested_response_priority: Low
validation_status: invalid
validation_issues: Missing required field: <field>
```

`company_size` must also be a positive integer.

## 12. Expected Structured Output

A successful V2 result contains:

- `company_name`
- `lead_quality_score`
- `icp_fit_assessment`
- `suggested_response_priority`
- `validation_status`
- `validation_issues`
- `scoring_reason`

The scoring reason identifies the component contribution from:

- Company Size
- Use Case
- Industry
- Urgency

Example format:

```text
Company Size: <score>/35,
Use Case: <score>/25,
Industry: <score>/20,
Urgency: <score>/20.
Total: <score>/100.
```

## 13. Monitoring

Monitor:

- Slack worker connection
- `NEW LEAD` event processing
- Structured lead-score replies
- Validation failures
- Unexpected scores
- Slack API errors
- Regression-test failures

A healthy run should show that the worker remains connected, receives the expected lead event, and returns a structured result without an exception.

## 14. Troubleshooting

If credentials are missing, confirm that `SLACK_APP_TOKEN` and `SLACK_BOT_TOKEN` are set.

If the worker connects but receives no messages, confirm:

- Event Subscriptions is enabled
- `message.channels` is subscribed
- Required Slack permissions are granted
- The Slack app was reinstalled after permission changes

If V2 scoring behavior changes unexpectedly, run:

```powershell
python -m pytest test_lead_qualification.py -v
```

Do not release or demonstrate a scoring change if regression tests fail.

If V2 standalone execution fails, run:

```powershell
python lead_qualification_util_v2.py
```

and inspect the validation or Python error before reconnecting the workflow.

## 15. Stop and Roll Back

Stop the worker with:

```text
Ctrl+C
```

Rollback trigger:

- Stop automation if **two consecutive invalid or clearly incorrect results occur on valid inputs**, or if a regression test fails after a scoring change.

Rollback procedure:

1. Stop the Python worker.
2. Continue manual lead review in Slack.
3. Diagnose the issue.
4. Restore the previous working logic if necessary.
5. Run the full regression suite.
6. Restart only after all regression tests pass and a valid sample lead produces the expected structured output.

## 16. Current Verified Status

The prototype has demonstrated:

- Deterministic Python lead scoring
- V2 scoring across company size, use case, industry, and urgency
- ICP fit assessment
- Suggested response priority
- Invalid-input handling
- Structured workflow output
- Slack worker integration
- Four passing regression tests

The current implementation is ready for capstone demonstration and controlled pilot evaluation.

Production deployment would require stronger monitoring, centralized secret management, retry handling, production-system integration, and measured operational KPIs.
