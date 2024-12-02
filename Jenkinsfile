pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'posad97/flask-app:latest'
        APP_CONTAINER_NAME = 'flask-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Pull the latest code from GitHub
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub using credentials from Jenkins
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'docker login -u DOCKER_USERNAME -p DOCKER_PASSWORD'
                    }
                }
            }
        }
        stage('Run Container from Docker Hub') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker rm -f ${APP_CONTAINER_NAME} || true"
                    
                    // Pull the image from Docker Hub and run the new container
                    sh """
                    docker run -d \
                        --name ${APP_CONTAINER_NAME} \
                        -p 5000:5000 \
                        ${DOCKER_IMAGE}
                    """
                }
            }
        }
    }
}