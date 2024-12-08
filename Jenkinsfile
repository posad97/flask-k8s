pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'posad97/flask-app:latest'
        APP_CONTAINER_NAME = 'flask-app'
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
        DB_CREDENTIALS_ID = 'db-credentials'
        DB_HOSTNAME = credentials('db-hostname')
        DB_NAME = credentials('db-name')
    }
    stages {
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
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    }
                }

                sh "docker push ${DOCKER_IMAGE}"
            }
        }
        stage('Run Container from Docker Hub') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker rm -f ${APP_CONTAINER_NAME} || true"
                    
                    // Pull the image from Docker Hub and run the new container
                    withCredentials([usernamePassword(credentialsId: DB_CREDENTIALS_ID, passwordVariable: 'DB_PASSWORD', usernameVariable: 'DB_USERNAME')]) {
                        sh """
                        docker run -d \
                        --name ${APP_CONTAINER_NAME} \
                        --network backend \
                        -p 5000:5000 \
                        -e DB_HOSTNAME=${env.DB_HOSTNAME} \
                        -e DB_USERNAME=${DB_USERNAME} \
                        -e DB_PASSWORD=${DB_PASSWORD} \
                        -e DB_NAME=${env.DB_NAME} \
                        ${DOCKER_IMAGE}
                    """
                    }
                    
                }
            }
        }
    }
}