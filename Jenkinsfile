pipeline {
  agent any

  environment {
    AWS_CRED_ID = 'aws-ecr-creds'          // AWS Jenkins Credentials ID
    AWS_REGION  = 'ap-south-1'
    ECR_ACCOUNT = '160056257840'           // Your AWS Account ID
    ECR_REPO    = 'bt-test-app'            // Your ECR repo
    IMAGE_TAG   = "${env.BUILD_NUMBER}"    // Auto image version: 1, 2, 3...
  }

  stages {

    /* 1️⃣ CHECKOUT CODE FROM GITHUB */
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    /* 2️⃣ LOGIN TO AWS ECR */
    stage('Login to ECR') {
      steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                          credentialsId: "${env.AWS_CRED_ID}"]]) {

          sh '''
            aws configure set default.region ${AWS_REGION}

            aws ecr get-login-password --region ${AWS_REGION} \
              | docker login --username AWS --password-stdin \
                ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
          '''
        }
      }
    }

    /* 3️⃣ BUILD DOCKER IMAGE */
    stage('Build Docker Image') {
      steps {
        sh '''
          docker build -t ${ECR_REPO}:${IMAGE_TAG} .
        '''
      }
    }

    /* 4️⃣ TAG & PUSH TO AWS ECR */
    stage('Push to ECR') {
      steps {
        sh '''
          docker tag ${ECR_REPO}:${IMAGE_TAG} \
            ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

          docker push ${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}
        '''
      }
    }

    /* 5️⃣ DEPLOY TO AWS EKS */
    stage('Deploy to EKS') {
      steps {

        withCredentials([file(credentialsId: 'kubeconfig-eks', variable: 'KUBECONFIG_FILE')]) {

          sh '''
            export KUBECONFIG=$KUBECONFIG_FILE

            echo "🔄 Updating deployment YAML with new image..."

            sed -i "s|<IMAGE>|${ECR_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}|g" k8s/deployment.yaml

            echo "🚀 Applying deployment to EKS..."
            kubectl apply -f k8s/deployment.yaml

            echo "🛰  Applying service (if exists)..."
            if [ -f k8s/service.yaml ]; then
              kubectl apply -f k8s/service.yaml
            fi

            echo "✅ Deployment Successfully Updated on EKS!"
          '''
        }
      }
    }
  }
}
