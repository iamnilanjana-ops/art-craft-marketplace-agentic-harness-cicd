# Prompt Pack — Inbound Lead Triage

## 1. Purpose

This prompt pack documents the structured prompts used in the Inbound Lead Triage workflow, including the base prompt, meta-prompted refinement, safety boundaries, fallback behavior, and version history.

The goal is to keep prompts consistent, reviewable, and safe while supporting deterministic downstream processing.

## 2. Base Prompt — Lead Classification

### Version 1.0

Classify the inbound email into one of these categories:

- DEMO REQUEST
- PRICING QUESTION
- PARTNERSHIP
- GENERAL INQUIRY

Return only the category and a concise summary of the sender's request.

Do not invent missing company information.
Do not include credentials, secrets, or sensitive data.
If the intent is unclear, use GENERAL INQUIRY.
## 3. Meta-Prompt Refinement

### Version 1.1

The original classification prompt was reviewed using a meta-prompt to identify ambiguity, unsafe assumptions, and output inconsistency.

Meta-prompt:

Review the lead-classification prompt for ambiguity, unsupported assumptions, inconsistent output, and unsafe handling of missing information.

Improve the prompt so that:

- Classification categories are fixed.
- Missing information is never invented.
- Unclear intent has a defined fallback.
- Output is concise and structured.
- Sensitive information is not exposed unnecessarily.
- The result can be consumed reliably by downstream workflow steps.

### Improvement Made

Version 1.1 introduced:

- Fixed classification categories
- GENERAL INQUIRY as the fallback
- Explicit instruction not to invent missing data
- More consistent structured output
- Safety boundaries for sensitive information

These changes reduce ambiguity and make downstream Zapier and Slack processing more predictable.
## 4. Safety Boundaries and Fallback Instructions

The workflow follows these prompt safety rules:

- Never invent missing lead information.
- Never expose API keys, passwords, Slack tokens, or other credentials.
- Use only information provided by the inbound lead or approved workflow data.
- Do not automatically treat ambiguous information as high priority.
- If email intent is unclear, classify it as GENERAL INQUIRY.
- If required scoring information is missing, the Python agent must return an invalid result rather than guess.
- Needs Review and invalid cases remain available for human review.
- External communication remains controlled by the Reply Sender workflow.

### Fallback Behavior

If classification is uncertain:

GENERAL INQUIRY → Human Review

If required qualification data is missing:

validation_status: invalid  
total_score: 0  
qualification_status: Not Qualified  
Action: Human Review

If the Python worker or Zapier workflow fails:

Stop the affected automation and continue manual lead review in Slack until the issue is resolved and regression tests pass.
## 5. Version History and Change Log

### Version 1.0 — Base Prompt

Initial lead-classification prompt created with four categories:

- DEMO REQUEST
- PRICING QUESTION
- PARTNERSHIP
- GENERAL INQUIRY

### Version 1.1 — Meta-Prompt Refinement

Changes:

- Added fixed output categories.
- Added GENERAL INQUIRY fallback.
- Added instruction not to invent missing information.
- Added sensitive-data safety boundary.
- Improved output consistency for downstream processing.

Reason:

The refinement reduces ambiguity and makes the classification output safer and more reliable for Zapier and Slack handoffs.

### Python Qualification Iteration

The Python qualification component uses deterministic logic instead of relying on an LLM prompt for scoring.

Regression protection covers:

- Qualified lead
- Needs Review lead
- Not Qualified lead
- Invalid or incomplete lead

Current regression result:

4 tests passed.

Any future change to prompts, scoring logic, or orchestration should be documented here and validated with the regression suite before release.
## 6. Prompt Iteration Evidence

### Actual Version 1.1 Prompt

Classify the inbound email into exactly one of these categories:

- DEMO REQUEST
- PRICING QUESTION
- PARTNERSHIP
- GENERAL INQUIRY

Use only information explicitly provided in the inbound email.

Do not invent or infer missing company information, urgency, budget, or qualification details.

If the sender's intent is unclear or does not clearly match DEMO REQUEST, PRICING QUESTION, or PARTNERSHIP, classify it as GENERAL INQUIRY.

Do not expose or repeat credentials, passwords, API keys, Slack tokens, or unnecessary sensitive information.

Return the result in this exact structure:

category: <one allowed category>
summary: <concise summary based only on provided information>

Do not add additional categories or unsupported information.

### Meta-Prompt Critique Findings

The review of Version 1.0 identified these issues:

1. The requested output format was not strict enough for reliable downstream parsing.
2. The prompt did not explicitly prohibit inference of urgency, budget, or qualification details.
3. Ambiguous messages needed a stronger deterministic fallback rule.
4. Sensitive-data handling needed to be more explicit.
5. Downstream automation needed predictable field names.

### Accepted and Rejected Recommendations

Accepted:

- Use fixed classification categories.
- Require exact `category` and `summary` output fields.
- Use GENERAL INQUIRY for ambiguous intent.
- Prohibit invention or inference of missing lead information.
- Add explicit sensitive-data boundaries.
- Keep the output concise for downstream Zapier and Slack processing.

Rejected:

- Allow the model to create new categories dynamically — rejected because this would make routing unpredictable.
- Ask the model to generate a qualification score — rejected because qualification scoring is handled deterministically by the Python agent.
- Automatically send an external response from the classification step — rejected because human oversight remains part of the workflow.

### Before/After Evaluation Case

Test input:

"Hi, I saw your company online and wanted to learn more about what you offer. Please send me some information."

Version 1.0 risk:

The request is ambiguous. The model is asked for a category and concise summary, but the output structure is not strict enough for reliable downstream parsing.

Version 1.1 expected result:

category: GENERAL INQUIRY
summary: Sender is requesting general information about the company's offerings.

Result:

Version 1.1 provides a defined fallback and predictable structured fields without inventing qualification information. This makes the output safer and easier for downstream workflow steps to consume.