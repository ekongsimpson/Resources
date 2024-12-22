## 1. Secure Access and Permissions <br/>

Use Role-Based Access Control (RBAC):
- Assign permissions to users and groups based on the principle of least privilege.
- Ensure only authorized users can edit or run pipelines, access secrets, and deploy to production.
- Use Azure DevOps roles like Contributor, Reader, or Administrator effectively. <br/>

Restrict Pipeline Variables Access:
- Use secret variables and restrict them to specific pipelines or environments.

## 2. Protect Secrets and Credentials <br/>
Use Azure Key Vault Integration:
- Store sensitive information like API keys, certificates, and passwords in Azure Key Vault.
- Configure pipelines to fetch [secrets](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/secrets-step.yaml) dynamically during execution.
- Mark Secrets as Hidden:
- Mark pipeline [variables](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/variables-step.yaml) containing sensitive information as secret to mask them in logs.

Avoid Hardcoding Credentials:
- Never hardcode sensitive values in the pipeline YAML file or scripts.

## 3. Use Secure Repositories <br/>
Protect the source code repository by:
- Enforcing branch policies like pull requests and code reviews.
- Enabling required reviewers and preventing direct pushes to protected branches (e.g., main).
- Scanning the repository for sensitive data leaks (e.g., credentials in the code) using tools like GitGuardian or Azure DevOps native scanning tools.

## 4. Use Secure Agents <br/>
Self-Hosted Agents:
- Secure the network and host where the agent is running.
- Avoid running agents with admin/root privileges unless absolutely necessary.
- Rotate agent credentials regularly. <br/>

Microsoft-Hosted Agents:
- Prefer these for short-lived builds/deployments as they are ephemeral and well-secured by Azure DevOps.

## 5. Enforce Secure Deployment Practices <br/>
Deployment Approvals:
- Use manual or automated approvals for critical environments like staging or production.
- Require multiple approvers for production deployments. <br/>

Environment-Specific Permissions:

- Use Azure DevOps environments to define deployment targets and enforce security controls.
- Restrict access to environments based on roles or groups. <br/>
Lock Resources During Deployment:

- Prevent unintended changes during deployment by using resource locks in Azure.

## 6. Validate and Secure Artifacts
- Use signed or verified artifacts to ensure integrity and authenticity. <br/>
Store artifacts securely:
- Use the Azure DevOps artifact storage or a private repository like Azure Artifacts or Docker Registry.
- Scan artifacts for vulnerabilities (e.g., container images) using tools like Trivy or Azure Security Center.

## 7. Implement Secure Coding Practices <br/>
Static Application Security Testing (SAST):
- Integrate tools like SonarQube or Azure DevOps' built-in Security Scan tasks to check for vulnerabilities in the codebase. <br/>

Dynamic Application Security Testing (DAST):
- Use tools like OWASP ZAP or third-party extensions to test running applications for vulnerabilities.

## 8. Isolate Secrets from the Build Process
- Use ephemeral containers or environments for builds and deployments to minimize exposure.
- Fetch secrets only during runtime and ensure they are not persisted in logs or artifacts.

## 9. Encrypt Data in Transit and at Rest
- Use HTTPS for all external and internal communications.
- Encrypt sensitive files and data used in the pipeline (e.g., deployment manifests, configuration files).

## 10. Monitor and Audit Pipeline Activity
- Enable logging for all pipeline activities.
- Use Azure Monitor or Azure Security Center to monitor resource usage and unusual activities.
- Regularly audit pipeline runs, approvals, and changes to detect unauthorized access.

## 11. Manage Pipeline Dependencies Securely
- Use signed or verified package sources (e.g., NuGet, npm).
- Scan dependencies for vulnerabilities using tools like Dependabot, WhiteSource, or Azure DevOps' built-in vulnerability scanning.

## 12. Apply Conditional Logic for Sensitive Actions
Use [condition](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/condition-logic.yaml) to prevent sensitive actions from running on unintended branches or in unauthorized scenarios.

## 13. Use Multi-Factor Authentication (MFA)
- Enforce MFA for all users in Azure DevOps and related Azure resources.
- Integrate with Azure AD for enhanced security and Single Sign-On (SSO).

## 14. Regularly Rotate Secrets and Access Tokens
- Set up policies to rotate keys, tokens, and credentials at regular intervals.
- Use Azure Managed Identity for secure and automated access to Azure resources without explicit credentials.

## 15. Stay Updated
- Regularly update self-hosted agents, pipeline tasks, and scripts to patch known vulnerabilities.
- Stay informed about Azure DevOps updates and security advisories.

