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

