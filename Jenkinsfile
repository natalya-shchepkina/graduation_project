pipeline {
  agent any
  stages {
         stage('Get Code') {
            steps {
                 git 'https://github.com/natalya-shchepkina/graduation_project.git'
            }
         }
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'py.test-3 ./tests --headless'
      }
      post {
          script {
            allure([
              includeProperties: false,
              jdk: '',
              properties: [],
              reportBuildPolicy: 'ALWAYS',
              results: [
                [path: 'allure-results']
              ]
            ])
      }
  }
}