pipeline {
  agent any

  environment {
    IMAGE_NAME = "cla-exchange-rate"
    IMAGE_TAG = "v2"
    REGISTRY = "nexus:18081"
    FULL_IMAGE = "${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
    GITOPS_REPO = "https://github.com/6510685016/gitops.git" 
    GITOPS_BRANCH = "main"
  }

  stages {
    stage('Checkout Source') {
      steps {
        git credentialsId: 'github-cred', url: 'https://github.com/6510685016/CLA-Exchange-Rate.git', branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${FULL_IMAGE} ."
      }
    }

    stage('Push to Nexus') {
      steps {
        withDockerRegistry([credentialsId: 'nexus-creds', url: "http://${REGISTRY}"]) {
          sh "docker push ${FULL_IMAGE}"
        }
      }
    }

    stage('Update GitOps') {
      steps {
        dir('gitops') {
          git credentialsId: 'github-cred', url: "${GITOPS_REPO}", branch: "${GITOPS_BRANCH}"
          dir('CLA-Exchange-Rate') {
            sh '''
              yq e '.image.tag = "${IMAGE_TAG}"' -i values.yaml
            '''
          }
          sh '''
            git config user.name "jenkins"
            git config user.email "jenkins@localhost"
            git add .
            git commit -m "Update image tag to ${IMAGE_TAG}"
            git push origin ${GITOPS_BRANCH}
          '''
        }
      }
    }
  }
}
