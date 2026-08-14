# Capstone Sanitization Review

## Purpose

This review verifies that the final capstone repository and submission evidence do not expose secrets, private credentials, personal information, or machine-specific sensitive data.

## Checks Performed

### Secret-pattern scan

The repository was scanned for common credential patterns, including:

- OpenRouter API keys;
- Anthropic API keys;
- Slack bot tokens;
- Google API keys;
- private-key blocks;
- suspicious hard-coded `OPENROUTER_API_KEY` assignments.

The only match was a test regex in `eval/test_policy.py` used to detect Anthropic-style key patterns. No actual secret value was found.

### Personal and local-data scan

The repository was scanned for:

- local Windows user paths;
- the local project path;
- personal names;
- personal email addresses;
- `credentials.json`;
- `token.json`.

No personal name, personal email address, or machine-specific Windows path was found.

References to `credentials.json` and `token.json` occur only in documentation describing OAuth setup and safe credential handling.

### Sensitive-file scan

The repository was checked for actual sensitive files matching names or extensions such as:

- `credentials.json`;
- `token.json`;
- `.env`;
- `.pem`;
- `.key`;
- `id_rsa`;
- `id_ed25519`.

No matching sensitive file was found.

### Runtime evidence review

Final workflow evidence under `logs/` was reviewed for secret exposure. The logs contain workflow, audit, retrieval, storage, evaluation, and governance evidence rather than API credential values.

## Sanitization Result

No actual API key, OAuth credential file, private key, personal email address, personal name, or machine-specific sensitive path was found in the reviewed repository content.

The capstone uses environment variables for runtime credentials and does not intentionally persist secret values in committed artifacts.

## Submission Guidance

Before final submission:

- do not add local `.env`, OAuth token, or credential files;
- do not expose API keys in screenshots or the walkthrough video;
- do not display environment-variable values during recording;
- keep final PDFs limited to sanitized project evidence;
- preserve placeholder credential examples rather than real values.

## Final Status

**Sanitization review: PASS**

The repository is suitable for final packaging based on the completed repository scans and reviewed runtime evidence.