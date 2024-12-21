## 1. Use YAML for Pipeline Definition
- Define pipelines as code using azure-pipelines.yaml. This enables versioning, collaboration, and easier updates. <br/>
- Store the pipeline YAML file in the same repository as your code for traceability.

## 2. Organize the pipeline with Stages, Jobs, and Steps
- **Stages**: Divide the pipeline into logical stages (e.g., Build, Test, Deploy) to reflect your deployment workflow.
- **Jobs**: Use jobs within stages to run tasks in parallel or sequentially.
- **Steps**: Use steps to define specific tasks (e.g., build commands, deployment scripts).

## 3. Implement Deployment Approvals
- Use environments in Azure DevOps to manage deployment approvals.
- Configure pre- or post-deployment approvals to ensure changes are reviewed before going to production.

![image](https://github.com/user-attachments/assets/cf7c93bc-1911-433e-b69a-8795bd4a5adf) <br/>

Approvals and other checks aren't defined in the yaml file. Users modifying the pipeline yaml file can't modify the checks performed before start of a stage. Administrators of resources manage checks using the web interface of Azure Pipelines. 
Check [Microsoft documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops&tabs=check-pass) for reference.

There are five categories of approvals and checks and they run in the order they were created within each category. Checks are reevaluated based on the retry interval specified in each check. If all checks aren't successful until the timeout specified, then that stage isn't executed. If any of the checks terminally fails (for example, if you reject an approval on one of the resources), then that stage isn't executed.

You can retry a stage when approvals and checks time out.

Static checks run first and then pre-check approvals run. The categories in order are:

- Static checks: Branch control, Required template, and Evaluate artifact
- Pre-check approvals
- Dynamic checks: Approval, Invoke Azure Function, Invoke REST API, Business Hours, Query Azure Monitor alerts
- Post-check approvals
- Exclusive lock
You can also see the execution order on the Approvals and checks tab.

## $${\color{red}Important \space}$$ 

Checks can be configured on $${\color{red}environments, \space service \space connections, \space repositories, \space variable \space groups, \space secure \space files, \space and \space agent pools}$$.

_Service connections cannot be specified by variable._


Taking [this](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/pre-approval.yaml) YAML pipeline for example, it will reference the variable group Feature Deployment on the condition ${{ if eq(variables['Build.SourceBranchName'], 'feature') }}, and will keep waiting for the approval to use this variable group.

Keep in mind that $${\color{red}ManualValidation@1}$$ could also be very helpful in many scenario - combining it with the **dependsOn** property on **jobs**. 



## 4. Use Variables and Variable Groups
- Define reusable variables for deployment targets, credentials, or configuration.
- Store sensitive information (e.g., passwords, API keys) securely in Azure DevOps Library as secret variables.

## 5. Secure Secrets and Credentials
- Store secrets like connection strings or API tokens in [Azure Key Vault](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/keyvault-step.yaml) or as pipeline secrets in variable groups.
- Use Azure DevOps’ built-in integration with Azure Key Vault for secure secret management.

## 6. Use [Deployment Strategies](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/deployment-strategy-step.yaml)
- Rolling Deployment: Gradually replace instances in a target environment to minimize downtime.
- Blue-Green Deployment: Deploy to a new environment and switch traffic to it after testing.
- Canary Deployment: Deploy to a small subset of users first, then gradually increase.

## 7. Define Clear Triggers
- Use branch-specific triggers to run the pipeline only on relevant branches.
- Use pipeline triggers or artifact triggers for dependency pipelines.
- Avoid running pipelines unnecessarily (e.g., [exclude certain branches](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/trigger-only-needed-branches.yaml)).

## 8. Use Templates for Reusability
- Extract common steps into templates to avoid duplication and improve maintainability.
- Include [templates](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/template-reusabiliity.yaml) for tasks like deployment or environment setup.

## 9. Monitor and Report
- Enable logging and telemetry for each stage to debug issues quickly.
- Use Azure DevOps' Test Plans and integration with tools like **Application Insights** for detailed monitoring.
- Set up notifications for pipeline failures or deployment issues.

## 10. Align with Infrastructure as Code (IaC)
- Deploy infrastructure alongside your application using tools like Terraform, Bicep, or ARM templates.
- Use tasks like AzureResourceManagerTemplateDeployment or TerraformCLI.

## 11. Optimize for Performance
- Use [pipeline caching]() to speed up builds
- Use pipeline parallelism and multi-agent jobs where applicable.

## 12. Use [Conditional Logic](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/condition-logic.yaml) for Flexibility
- Apply conditions to control execution based on branch, variables, or environment.

## 13. Test Before Deploying
- Include automated unit, integration, and smoke tests as part of your pipeline.
- Run tests in isolated environments before deploying to production.

## 14. Use Artifacts
- Package and [publish build outputs](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/publish-build-artifacts.yaml) (e.g., .zip, Docker images) as artifacts for reuse in deployment stages.

## 15. Regularly Review and Update Pipelines
- Periodically review pipelines for outdated dependencies, unused tasks, or inefficiencies.
- Keep tooling, agents, and dependencies up to date.

