# Onboarding a Backend Service to Standardized SAST

## Purpose
This guide explains how to enable standardized Static Application Security
Testing (SAST) for a backend service using the organization's reusable
CI/CD templates.

Following these steps ensures the service is secure-by-default.

---

## Prerequisites
Before enabling SAST, ensure:
- The service repository is hosted on GitHub
- GitHub Actions is enabled
- Required SAST secrets are available via GitHub Secrets (synced from Vault)

---

## Step 1: Add the SAST Workflow
Create a workflow file in your service repository:

.github/workflows/sast.yml


Add the following configuration:

```yaml
name: SAST Scan

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  sast:
    uses: <ORG>/<REPO>/.github/workflows/sast.yml@main
    secrets:
      SAST_TOKEN: ${{ secrets.SAST_TOKEN }}

```

