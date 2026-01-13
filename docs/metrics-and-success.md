# Metrics and Success Criteria for Infrastructure-Wide SAST

## Purpose
This document defines how the effectiveness of the standardized
SAST implementation is measured across backend services.

The goal is to ensure consistent adoption, clear enforcement,
and continuous improvement of code security.

---

## Adoption Metrics
The following indicators measure adoption across services:

- Percentage of backend repositories with SAST enabled
- Number of services using the standardized SAST CI/CD template
- Number of new services onboarded with SAST enabled by default

---

## Policy Enforcement Metrics
These metrics ensure security policies are applied consistently:

- Number of pipeline failures due to CRITICAL or HIGH findings
- Consistency of severity thresholds across services
- Reduction in manual SAST configuration across repositories

---

## Security Improvement Metrics
These metrics indicate improvement in code quality over time:

- Reduction in recurring SAST findings
- Decrease in repeated vulnerabilities across releases
- Time to remediation for CRITICAL and HIGH findings

---

## Exception Tracking Metrics
Exception handling effectiveness is measured by:

- Number of active SAST exceptions
- Percentage of expired exceptions reviewed on time
- Trend of exception usage over time

---

## Developer Experience Indicators
To ensure SAST does not negatively impact productivity:

- Frequency of false positive reports
- Developer feedback on clarity of findings
- Reduction in pipeline bypass requests

---

## Review and Continuous Improvement
Metrics should be reviewed periodically by:
- DevOps teams
- Security teams

Based on observed trends, policies and tooling may be refined
to improve effectiveness and developer adoption.

---

## Summary
Clear metrics ensure that standardized SAST implementation
delivers measurable security improvements while maintaining
development velocity.

