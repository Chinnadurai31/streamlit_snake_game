pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('Docker-credentials')
        SONARQUBE_SERVER = 'sonarqube_test' 
        SONARQUBE_TOKEN = 'sqp_92a46b8de376a5d918366290303956e2327d8545'
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
                    echo "Scanning the image with Trivy..."
                    sh "trivy image --severity CRITICAL ${imageTag}"
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    echo "Running SonarQube analysis..."
                    
                    // Set SonarQube Scanner environment variables
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        // Run SonarQube Scanner
                        sh '''
                            sonar-scanner \
                            -Dsonar.projectKey=sonar.projectKey=sonarqube_test \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=https://26b2e3c6a6c20f30c83e8ea36a3fed0c.serveo.net \
                            -Dsonar.login=${SONARQUBE_TOKEN}
                        '''
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo "Pushing the image to Docker Hub..."
                    def imageTag = "chinnadurai123/steamlit_game:game-${BUILD_NUMBER}"
                    
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_HUB_CREDENTIALS) {
                        docker.image(imageTag).push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image successfully built, scanned with Trivy, analyzed with SonarQube, and pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
