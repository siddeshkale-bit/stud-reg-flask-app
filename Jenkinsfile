pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                bat """
                python -m venv venv
                .\\venv\\Scripts\\activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Run App Tests') {
            steps {
                bat """
                .\\venv\\Scripts\\activate
                echo No tests added yet
                """
            }
        }
    }
}
