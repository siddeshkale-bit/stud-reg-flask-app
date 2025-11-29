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
                "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                call venv\\Scripts\\activate
                "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip
                "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" install -r requirements.txt
                """
            }
        }

        stage('Run App Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                echo No tests added yet
                """
            }
        }
    }
}
