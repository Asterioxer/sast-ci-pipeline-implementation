# Organization-Wide SAST Policy

## Purpose
This policy defines how Static Application Security Testing (SAST) findings
are handled across all backend services to ensure consistent security
enforcement without impacting development velocity.

---

## Severity Levels
SAST findings are categorized into the following severity levels:

- CRITICAL
- HIGH
- MEDIUM
- LOW

---

## Pipeline Enforcement Rules

| Severity  | Pipeline Behavior | Action Required |
|---------|-------------------|-----------------|
| CRITICAL | Fail build | Must be fixed before merge |
| HIGH     | Fail build | Must be fixed before merge |
| MEDIUM   | Warn only | Fix recommended |
| LOW      | Informational | Fix optional |

---

## Remediation Expectations

| Severity  | Expected Resolution Time |
|---------|--------------------------|
| CRITICAL | Immediate |
| HIGH     | Within 7 days |
| MEDIUM   | Within 30 days |
| LOW      | Best effort |

---

## Exception Handling
Exceptions may be granted under the following conditions:
- The finding is a confirmed false positive
- The risk is accepted temporarily due to business constraints

All exceptions must:
- Be documented with justification
- Have an owner
- Include an expiry date

Expired exceptions must be reviewed or removed.

---

## Ownership
- Development teams are responsible for fixing SAST findings in their services
- Security teams define and maintain SAST rules
- DevOps teams maintain CI/CD enforcement and templates

---

## Policy Review
This policy will be reviewed periodically to ensure alignment with
organizational security standards and development practices.
