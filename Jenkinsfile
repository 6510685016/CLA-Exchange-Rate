pipeline {
  agent any

  environment {
    VERSION = "1.0.${BUILD_NUMBER}"
    IMAGE_NAME = "10.0.2.5:8082/docker-hosted/cli-exc:${VERSION}"
    GITOPS_REPO = "https://github.com/6510685016/gitops-repo.git"
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

    stage('Trivy Scan') {
      steps {
        sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL $IMAGE_NAME'
      }
    }

    stage('Push to Nexus') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'nexus-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh '''
            echo "$PASS" | docker login 10.0.2.5:8082 -u "$USER" --password-stdin
            docker push $IMAGE_NAME
          '''
        }
      }
    }

    stage('Update GitOps Repo') {
      steps {
        sh '''
          rm -rf gitops-repo
          git clone --depth 1 $GITOPS_REPO
          cd gitops-repo

          sed -i "s/tag: .*/tag: \\"$VERSION\\"/" $CHART_PATH

          git config user.email "jenkins@example.com"
          git config user.name "Jenkins Bot"
          git commit -am "🔁 Update image tag to $VERSION"
          git push
        '''
      }
    }
  }

  post {
    success {
      echo "✅ Deploy tag $VERSION pushed to GitOps repo"
    }
    failure {
      echo "❌ Pipeline failed. Check logs."
    }
  }
}
