pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Jenkins credential ID
        IMAGE_NAME = 'malligayathri/calculator'
        GIT_URL = 'https://github.com/Gayathri-malli/Calculator_ui'
        KUBECONFIG = 'C:\\Users\\K UPENDRA\\.kube\\config'
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo '📥 Cloning repository...'
                git branch: 'main', url: "${env.GIT_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def timestamp = new Date().format("yyyyMMddHHmmss")
                    env.IMAGE_TAG = "${IMAGE_NAME}:${timestamp}"
                    echo "🐳 Building Docker image: ${env.IMAGE_TAG}"
                    bat """
                        docker build -t ${env.IMAGE_TAG} .
                    """
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '📤 Pushing Docker image...'
                script {
                    bat """
                        echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin
                        docker push ${env.IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '🚀 Deploying to Kubernetes...'
                script {
                    // Update deployment with new image
                    bat """
                        kubectl set image deployment/calculator calculator=${env.IMAGE_TAG} --record
                        kubectl rollout status deployment/Calculator
                    """
                }
            }
        }

        stage('Port Forward for Local Testing') {
            steps {
                echo '🔗 Forwarding Kubernetes service to localhost:5000'
                echo 'Run this manually in a separate terminal:'
                echo 'kubectl port-forward svc/python-app 5000:5000'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! Access app via localhost:5000'
        }
        failure {
            echo '❌ Build or deployment failed!'
        }
    }
}
