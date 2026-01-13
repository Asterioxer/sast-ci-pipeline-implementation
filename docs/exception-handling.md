# SAST Exception Handling Process

## Purpose
This document defines the standardized process for handling exceptions
to SAST findings in cases where immediate remediation is not feasible.

The goal is to allow flexibility without compromising security visibility
or long-term remediation.

---

## When Exceptions Are Allowed
Exceptions may be requested only if:
- The finding is a confirmed false positive
- The affected code is legacy and scheduled for refactor
- There is a temporary business constraint preventing immediate fixes

Exceptions must not be used to permanently bypass security controls.

---

## Exception Request Process

1. A SAST finding is identified during CI/CD execution
2. The development team documents:
   - Finding details
   - Justification for exception
   - Impact assessment
3. The request is reviewed by:
   - Security team (risk validation)
   - DevOps team (pipeline impact)
4. If approved, the exception is granted with:
   - A clear owner
   - An expiry date

---

## Exception Tracking
All approved exceptions must be tracked using one of the following:
- Issue tracker (e.g., Jira)
- Repository labels or annotations
- Central exception registry (if available)

Tracking must include:
- Service name
- Severity
- Approval date
- Expiry date

---

## Expiry and Review
- Exceptions expire automatically after the defined period
- Expired exceptions must be:
  - Renewed with justification, or
  - Removed by fixing the finding

Unreviewed expired exceptions are treated as policy violations.

---

## Ownership
- Development teams own exception requests and remediation
- Security teams approve or reject exceptions
- DevOps teams ensure enforcement mechanisms remain intact
