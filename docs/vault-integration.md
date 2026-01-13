# Vault Integration for SAST Token Management

## Purpose
This document describes how secrets required for SAST scanning
are securely managed using HashiCorp Vault and consumed by
GitHub Actions workflows.

The goal is to avoid hardcoded credentials and ensure
secure, centralized secret management.

---

## Secret Ownership
- SAST tool tokens are stored centrally in Vault
- Security teams own token creation and rotation
- DevOps teams manage access to secrets in CI/CD

---

## Access Pattern

1. The SAST token is stored in Vault under a defined path
2. GitHub Actions is configured to retrieve the token securely
3. The token is injected into the workflow as an environment variable
4. The SAST tool consumes the token during scan execution

At no point is the token stored in source control.

---

## CI/CD Integration
GitHub Actions workflows reference the SAST token via encrypted secrets.

Example:

```yaml
env:
  SEMGREP_APP_TOKEN: ${{ secrets.SAST_TOKEN }}
