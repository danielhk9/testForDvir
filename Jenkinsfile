pipeline {
  agent any

  environment {
    IMAGE = 'pytest-selenium-tests'
  }

  options { timestamps() }

  parameters {
    string(name: 'BASE_URL',  defaultValue: 'https://www.saucedemo.com', description: 'Target base URL')
    booleanParam(name: 'HEADLESS', defaultValue: true, description: 'Run headless browser')
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }

    stage('Run Tests (Docker)') {
      steps {
        sh '''
          rm -rf reports || true
          mkdir -p reports
          docker run --rm \
            -e BASE_URL=${BASE_URL} \
            -e HEADLESS=${HEADLESS} \
            -v "$PWD/reports:/reports" \
            $IMAGE
        '''
      }
    }

    stage('Publish Allure in Jenkins') {
      steps {
        archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: false
        allure([
          includeProperties: false,
          jdk: '',
          results: [[path: 'reports/allure-results']]
        ])
      }
    }
  }

  post {
    always {
      sh 'docker image prune -f || true'
    }
  }
}
