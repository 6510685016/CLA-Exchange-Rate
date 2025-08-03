pipeline {
  agent any

  environment {
    VERSION = "1.0.${BUILD_NUMBER}"
    IMAGE_NAME = "nexus:8082/docker-hosted/cli-exc:${VERSION}"
    GITOPS_REPO = "https://github.com/6510685016/CLA-Exchange-Rate"
    CHART_PATH = "helm/cli-exc/values.yaml"
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/6510685016/CLA-Exchange-Rate'
      }
    }

    stage('Build Docker') {
      steps {
        sh 'docker build -t $IMAGE_NAME .'
      }
    }

    stage('Scan with Trivy') {
      steps {
        sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL $IMAGE_NAME'
      }
    }

    stage('Push Image to Nexus') {
      steps {
        sh 'docker push $IMAGE_NAME'
      }
    }

    stage('Update GitOps Repo') {
      steps {
        sh '''
          rm -rf gitops-repo
          git clone $GITOPS_REPO
          cd gitops-repo

          sed -i "s/tag: .*/tag: \\\"$VERSION\\\"/" $CHART_PATH

          git config user.email "jenkins@example.com"
          git config user.name "Jenkins Bot"
          git commit -am "Update CLI image tag to $VERSION"
          git push
        '''
      }
    }
  }

  post {
    success {
      echo "✅ Deploy tag $VERSION successfully updated."
    }
    failure {
      echo "❌ Pipeline failed."
    }
  }
}
