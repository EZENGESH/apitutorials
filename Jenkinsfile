pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python -m venv venv'
                // Using dot notation instead of source
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                // Using the full path to ensure activation
                sh '''
                . venv/bin/activate
                python manage.py test
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()  // Clean up workspace after build
        }
    }
}