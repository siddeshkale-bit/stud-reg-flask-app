Flask Student Registration Web Application with Jenkins
Overview

A simple Flask web application where users can register students through a form. The submitted data is stored in a MySQL database and can be viewed on a separate page. The project includes Jenkins CI integration for automated builds.

Features

Student registration form

Stores data in MySQL

View all students in a table

Jenkins pipeline for automated setup and installation

Tech Stack

Flask (Python)

HTML, CSS

MySQL

Git & GitHub

Jenkins CI

Repository
https://github.com/siddeshkale-bit/stud-reg-flask-app.git

Database Setup
CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    course VARCHAR(100),
    address TEXT
);

How to Run Locally
git clone https://github.com/siddeshkale-bit/stud-reg-flask-app.git
cd stud-reg-flask-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


App starts at:

http://127.0.0.1:5000/

Jenkins Pipeline

The Jenkinsfile performs:

Git checkout

Virtual environment creation

Dependency installation

Test stage

Jenkinsfile (short version)
pipeline {
    agent any
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Setup Env') {
            steps {
                bat """
                "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                """
            }
        }
        stage('Test') { steps { bat "echo Tests done" } }
    }
}
