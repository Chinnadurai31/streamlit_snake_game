pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('Docker-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Chinnadurai31/streamlit_snake_game.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def imageTag = "chinnadurai123/steamlit_game:game-${BUILD_NUMBER}"
                    docker.build(imageTag)
                }
            }
        }

        stage('Scan with Trivy') {
            steps {
                script {
                    def imageTag = "chinnadurai123/steamlit_game:game-${BUILD_NUMBER}"
                    
                    // Run Trivy scan
                    echo "scanning the image with trivy..."
                    sh "trivy image --severity CRITICAL ${imageTag}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "pushing the image to the dockerhub..."
                    def imageTag = "chinnadurai123/steamlit_game:game-${BUILD_NUMBER}"
                    
                    docker.withRegistry('https://index.docker.io/v1/', 'Docker-credentials') {
                        docker.image(imageTag).push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image successfully built, scanned with Trivy, and pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
