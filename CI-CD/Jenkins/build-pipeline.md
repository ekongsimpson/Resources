## The definition of a Jenkins Pipeline is typically written into a text file (called a Jenkinsfile)
## Your basic jenkins build pipeline could look like this:<br/>

Jenkinsfile (Declarative Pipeline)<br/>

pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}

... if jenkins is running on Linux, BSD, and Mac OS

If it's running on Windows, you would be using **bat** instead of **sh** to execute commands<br/>

Jenkinsfile (Declarative Pipeline)<br/>

pipeline {

    agent any
    stages {
        stage('Build') {
            steps {
                bat '''
                    ECHO Hello World
                '''
            }
        }
    }
}


Jenkins is heavily dependent on plugins for building, testing and deployment.<br/>
Depending on the programming language you're developing on, you would need a corrisponding plugin.
If you're using python and an agent running on a container, you would very likely need a pipeline like this:

Jenkinsfile (Declarative Pipeline)<br/>
/* Requires the Docker Pipeline plugin */<br/>
pipeline {

    agent { docker { image 'python:3.13.1-alpine3.21' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}


A java developer, on the other hand, would need: <br/>
Jenkinsfile (Declarative Pipeline) <br/>
/* Requires the Docker Pipeline plugin */ <br/>
pipeline {

    agent { docker { image 'maven:3.9.9-eclipse-temurin-21-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}


And those usign node.js would go for... <br/>
Jenkinsfile (Declarative Pipeline) <br/>
/* Requires the Docker Pipeline plugin */ <br/>

pipeline {

    agent { docker { image 'node:22.12.0-alpine3.21' } }
    stages {
        stage('build') {
            steps {
                sh 'node --version'
            }
        }
    }
}

