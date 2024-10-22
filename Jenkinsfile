pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "my-django-app"
        DOCKER_TAG = "latest"
    }
    
    stages {
        stage('Clone Repo') {
            steps {
                // Clone the repository from Git
                git branch: 'main', url: 'https://github.com/dharaniselvaraj01/Task_manager.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image using the Dockerfile
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests using pytest inside the Docker container
                    sh 'docker run ${DOCKER_IMAGE}:${DOCKER_TAG} pytest'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Use docker-compose to deploy the application
                    sh 'docker-compose -f docker-compose.yml up -d --build'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}