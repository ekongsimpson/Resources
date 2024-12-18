## Your basic jenkins build pipeline could look like this:<br/>

Jenkinsfile (Declarative Pipeline)<br/>
    pipeline {<br/>
        agent any<br/>
        stages {<br/>
            stage('Build') {<br/>
                steps {<br/>
                    sh 'echo "Hello World"'<br/>
                    sh '''<br/>
                        echo "Multiline shell steps works too"<br/>
                        ls -lah<br/>
                    '''<br/>
                }<br/>
            }<br/>
        }<br/>
    }<br/>

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
