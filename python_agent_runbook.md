# Python Agent Runbook — Inbound Lead Triage

## 1. Purpose

The Python Lead Qualification Agent monitors Slack for structured `NEW LEAD` messages, validates the lead data, calculates a deterministic qualification score, and posts the result back to the same Slack thread.

Python is used because the scoring and validation logic is easier to maintain, test, and regression-check in code than as a large set of Zapier conditions.

## 2. Main Files

### lead_qualification_util.py

Contains the reusable lead qualification logic:

- Parses structured lead messages
- Validates required fields
- Calculates component scores
- Calculates the total score
- Assigns qualification status
- Formats structured Slack output
- Provides a CLI for standalone testing

### slack_lead_worker.py

Runs the Slack worker.

It:

- Connects to Slack
- Monitors Slack messages
- Detects relevant `NEW LEAD` posts
- Passes lead data to the qualification utility
- Posts the result back to the Slack thread

### test_lead_qualification.py

Contains automated regression tests for:

- Qualified
- Needs Review
- Not Qualified
- Invalid lead

## 3. Required Python Dependency

The project uses:

```text
slack-sdk==3.44.0

## 4. Credentials

The Slack worker requires:

- SLACK_APP_TOKEN
- SLACK_BOT_TOKEN

Credentials are loaded from environment variables and must never be hardcoded in the Python files or included in screenshots.
## 5. Test the Agent

Test the scoring utility:

python lead_qualification_util.py --presets

Expected results:

- Acme Corp → 75 → Qualified
- Beta Industries → 50 → Needs Review
- Gamma Startups → 18 → Not Qualified
- Delta Unknown → 0 → Invalid / Not Qualified

## 6. Run Regression Tests

Run:

python -m pytest test_lead_qualification.py -v

Current verified result:

4 passed

All regression tests should pass before scoring logic is changed or deployed.

## 7. Start the Slack Worker

Set the Slack credentials in the environment and run:

python slack_lead_worker.py

A successful startup confirms that the credentials were loaded and the worker connected to Slack.

Keep the terminal open while the worker is running.
## 8. Agent Execution Flow

The workflow is:

1. Slack receives a NEW LEAD message.
2. The Slack worker detects the message.
3. Lead fields are parsed.
4. Required fields are validated.
5. Valid leads are scored.
6. Qualification status is assigned.
7. A scoring explanation is generated.
8. The result is posted back to the same Slack thread.

## 9. Scoring Rules

The deterministic score has four dimensions:

- Budget: 0–30 points
- Business Need: 0–30 points
- Company Size: 0–20 points
- Purchase Timeline: 0–20 points

Qualification thresholds:

- 70–100 = Qualified
- 40–69 = Needs Review
- 0–39 = Not Qualified
## 10. Validation

Required fields are:

- company_name
- contact_name
- company_size
- budget
- business_need
- purchase_timeline

If required information is missing, the agent returns an invalid result instead of producing a normal qualification score.

Example:

total_score: 0
qualification_status: Not Qualified
validation_status: invalid
validation_issues: Missing required field: budget
## 11. Expected Slack Output

Successful processing creates a Slack thread reply beginning with:

LEAD SCORED

The result contains:

- company_name
- total_score
- qualification_status
- validation_status
- validation_issues
- scoring_reason
## 12. Monitoring

Monitor:

- Slack worker connection
- NEW LEAD event processing
- LEAD SCORED replies
- Validation failures
- Unexpected scores
- Slack API errors
## 13. Troubleshooting

If credentials are missing, confirm that SLACK_APP_TOKEN and SLACK_BOT_TOKEN are set.

If the worker connects but receives no messages, confirm:

- Event Subscriptions is enabled.
- message.channels is subscribed.
- Required Slack permissions are granted.
- The Slack app was reinstalled after permission changes.

If scoring behavior changes unexpectedly, run:

python -m pytest test_lead_qualification.py -v

Do not release the change if regression tests fail.
## 14. Stop and Roll Back

Stop the worker with:

Ctrl+C

If the automation becomes unreliable:

1. Stop the Python worker.
2. Continue manual lead review in Slack.
3. Diagnose the issue.
4. Restore the previous working logic if necessary.
5. Run all regression tests.
6. Restart only after the tests pass.
## 15. Current Verified Status

The prototype has demonstrated:

- Python deterministic lead scoring
- Slack worker connection
- Qualified lead processing
- Needs Review processing
- Not Qualified processing
- Invalid-input handling
- Structured Slack thread responses
- Four passing regression tests

The current implementation is ready for capstone demonstration.

Production deployment would require stronger monitoring, centralized secret management, retry handling, and production-system integration.

