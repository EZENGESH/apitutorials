pipeline {
    agent any
    environment {
        // Customize these:
        DOCKER_IMAGE = "ezengesh/myapp"
        DOCKER_REGISTRY = "https://index.docker.io/v1/"
    }
    
    stages {
        // Stage 1: Checkout code from Git
        stage('Checkout') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/EZENGESH/apitutorials.git'
            }
        }

        // Stage 2: Build Docker image
        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        // Stage 3: Push to Docker Registry
        stage('Push') {
            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY, 'docker-hub-creds') {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                        // Optional: Also push as 'latest'
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')
                    }
                }
            }
        }
    }
}