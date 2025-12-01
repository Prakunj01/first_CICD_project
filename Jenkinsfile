pipeline {
  agent {
    docker {
      image 'amazon/aws-cli:2.15.0'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  environment {
    AWS_CRED_ID = 'aws-ecr-creds'
    AWS_REGION  = 'ap-south-1'
    ECR_ACCOUNT = '160056257840'
    ECR_REPO    = 'bt-test-app'
    IMAGE_TAG   = "${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Login to ECR') {
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CRED_ID}"]]) {
          sh '''
            aws ecr get-login-password --region ${AWS_REGION} \
              | docker login --username AWS --password-stdin ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
          '''
        }
      }
    }

    stage('Build Image') {
      steps {
        sh '''
          docker build -t ${ECR_REPO}:${IMAGE_TAG} .
        '''
      }
    }

    stage('Push Image') {
      steps {
        sh '''
          docker tag ${ECR_REPO}:${IMAGE_TAG} ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
          docker push ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
        '''
      }
    }
  }
}
