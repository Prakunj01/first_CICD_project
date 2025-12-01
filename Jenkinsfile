pipeline {
  agent any

  environment {
    AWS_CRED_ID = 'aws-ecr-creds'
    AWS_REGION  = 'ap-south-1'
    ECR_ACCOUNT = '160056257840'
    ECR_REPO    = 'bt-test-app'
    IMAGE_TAG   = "${env.BUILD_NUMBER}"
  }

  stages {

    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Login to ECR') {
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: "${AWS_CRED_ID}"]]) {
          sh '''
            aws configure set default.region ${AWS_REGION}
            aws ecr get-login-password --region ${AWS_REGION} \
            | docker login --username AWS --password-stdin \
              ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
          '''
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${ECR_REPO}:${IMAGE_TAG} ."
      }
    }

    stage('Push to ECR') {
      steps {
        sh """
          docker tag ${ECR_REPO}:${IMAGE_TAG} \
            ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

          docker push ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
        """
      }
    }

    stage('Deploy to EKS') {
  steps {

    withCredentials([
      file(credentialsId: 'kubeconfig-eks', variable: 'KUBECONFIG_FILE'),
      [$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${AWS_CRED_ID}"]
    ]) {

      sh '''
        export KUBECONFIG=$KUBECONFIG_FILE

        # Force AWS CLI to authenticate EKS
        aws sts get-caller-identity

        # Generate token manually to ensure kubectl auth works
        aws eks get-token --region ${AWS_REGION} --cluster-name devops-eks > /dev/null

        # Replace deployment image
        sed -i "s|<IMAGE>|${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}|g" k8s/deployment.yaml

        echo "Deploying to EKS..."
        kubectl apply --validate=false -f k8s/deployment.yaml
      '''
    }
  }
}

  }
}
