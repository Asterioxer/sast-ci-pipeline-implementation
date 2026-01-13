# Developer Guide: Understanding and Fixing SAST Findings

## Purpose
This guide helps developers understand Static Application Security
Testing (SAST) findings and take appropriate action when issues
are reported in CI/CD pipelines.

The goal is to fix real security issues efficiently while avoiding
unnecessary friction.

---

## Understanding SAST Findings
SAST analyzes source code to identify potential security issues
such as:
- Injection vulnerabilities
- Insecure API usage
- Hardcoded secrets
- Unsafe data handling patterns

Findings are reported with a severity level indicating potential risk.

---

## Severity Levels Explained

| Severity  | What It Means |
|---------|---------------|
| CRITICAL | High confidence vulnerability with serious impact |
| HIGH     | Likely security issue requiring prompt attention |
| MEDIUM   | Potential risk or insecure pattern |
| LOW      | Minor issue or best-practice recommendation |

---

## How to Respond to Findings

### CRITICAL / HIGH
- These findings fail the CI/CD pipeline
- Review the code path carefully
- Apply recommended fixes or refactor logic
- Re-run the pipeline to verify resolution

### MEDIUM
- Does not fail the pipeline
- Fix when working in the affected area
- Track as technical debt if needed

### LOW
- Informational only
- Fix opportunistically

---

## Handling False Positives
If a finding is believed to be a false positive:
1. Review the code and confirm expected behavior
2. Document the justification
3. Follow the SAST exception handling process

Do not suppress findings without documentation or approval.

---

## Best Practices for Reducing Findings
- Validate and sanitize user input
- Avoid hardcoded credentials
- Use secure libraries and APIs
- Follow secure coding guidelines for the language in use

---

## Getting Help
If unsure how to fix a finding:
- Consult the SAST tool documentation
- Reach out to the security team for clarification
- Coordinate with DevOps for pipeline-related questions

---

## Summary
SAST is a tool to assist developers in writing secure code.
Clear understanding and consistent handling of findings
helps maintain security without slowing development.

