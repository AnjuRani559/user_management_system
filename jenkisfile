pipeline {
    environment {
    IMAGE_TAG = "${GIT_COMMIT}".take(7)
    }
    agent any
    stages {
        stage('Build and Push Image') {

            when {
                expression { env.BUILD == 'true' }
            }
            steps {
                echo 'Building and pushing image...'
                echo "${env.BACKEND_IMAGE}"
                script {
                    def backend_image = docker.build("${env.BACKEND_IMAGE}")
                    docker.withRegistry('https://registry.hub.docker.com', "${env.DOCKER_CREDENTIALS_ID}") {
                       backend_image.push("latest")
                       backend_image.push("${env.GIT_COMMIT.take(7)}")
                    }
            	}
            	
            }
	}
    }

    post {
        always {
            echo 'Cleaning workspace. . .'
            deleteDir()
            cleanWs()
        }
    }
}
