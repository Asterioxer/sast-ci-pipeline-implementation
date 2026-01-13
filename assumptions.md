## Assumptions

The following assumptions are made initially for the implementation:

- Source control and CI/CD platform is GitHub.
- GitHub Actions is used for CI/CD pipelines.
- A SAST tool such as Semgrep is used for static code analysis.
- Secrets required for SAST tools are stored in HashiCorp Vault.
- The solution is designed to be language-agnostic and reusable across backend services.

These assumptions can be revisited as the implementation evolves.