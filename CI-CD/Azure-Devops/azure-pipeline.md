## A STARTER PIPELINE
The heirarchy in the structure of an azure pipeline yaml file looks like this:

- Pipeline
  - Stage A
    - Job 1
      - Step 1.1
      - Step 1.2
      - ...
    - Job 2
      - Step 2.1
      - Step 2.2
      - ...
  - Stage B
    - ...

[This](https://github.com/ekongsimpson/Resources/blob/main/CI-CD/Azure-Devops/azdo-starter-pipeline.yaml) is example of a starter pipeline.




Considering the structure of the heirarchy above the starter pipeline could fit into **JOB 1** under stage A in the pipeline. <br/>
The jobs, stages and pipeline keywords are missing in this example. A single stage pipeline can do without them. You jump straight into steps.

You cannot do that in a multi-stage pipeline, though. Hence, if I had a 2 stage-pipeline, I must define them and remember that the trigger keyword is used at the pipeline level, not within the stages because it defines when the pipeline as a whole should run (e.g., on specific branches, tags, or schedules). <br/> E.g.<br/>

- Pipeline
  trigger:
  - main

  - Stage A
    - Job 1
      pool:
        vmImage: ubuntu-latest

      steps: <br/>
      - script: echo Hello, world! <br/>
        displayName: 'Run a one-line script' <br/>

      - script: | <br/>
          echo Add other tasks to build, test, and deploy your project. <br/>
          echo See https://aka.ms/yaml <br/>
        displayName: 'Run a multi-line script' 
  
  - Stage B <br/>
    Job 1 <br/>
    - deployment: Deploy2MYENV <br/>
      displayName: Deploy2MYENV <br/>
      environment: MYENV <br/>
      pool: <br/>
        vmImage: ubuntu-latest <br/>
      strategy: <br/>
       runOnce: <br/>
        deploy: <br/>
         steps: <br/>
          - script: | <br/>
            echo Add other tasks to build, test, and deploy your project. <br/>
            echo See https://aka.ms/yaml <br/>


## Stages Cannot Have Triggers: <br/>
Stages themselves cannot have triggers. However, you can use conditions to control when specific stages execute. For example:

condition: eq(variables['Build.SourceBranchName'], 'main')

## Best Practices
- Use pipeline-level trigger for simplicity unless you need more granular control via conditions or dependencies.
- Use a pipeline-level pool when all stages/jobs run on the same type of agent, and stage-level pools for mixed environments (e.g., Windows for build, Linux for testing).
- For controlling execution of individual stages, use dependsOn or condition.



## Key Concepts
![image](https://github.com/user-attachments/assets/362e5177-cf70-401b-b057-d700393300cc)


* A trigger tells a pipeline to run.
* A pipeline is made up of one or more stages. A pipeline can deploy to one or more environments.
* A stage is a way of organizing jobs in a pipeline and each stage can have one or more jobs.
* Each job runs on one agent. A job can also be agentless.
* Each agent runs a job that contains one or more steps.
* A step can be a task or script and is the smallest building block of a pipeline.
* A task is a prepackaged script that performs an action, such as invoking a REST API or publishing a build artifact.
* An artifact is a collection of files or packages published by a run.

For a complete guide, please refer to https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops
