pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t base_python --rm -f DockerfileCI.base_python .'
            }
        }
        stage('Tests'){
            steps {
                sh 'docker run --name ad_tests -i base_python pytest -n2 --color=yes --quiet --showlocals --disable-pytest-warnings -p no:warnings --alluredir=allure-result'
            }
        }
    }
    post {
        always ('Allure reports') {
            sh 'docker cp ad_tests:/tests/allure-result $PWD/'
            sh 'docker rm ad_tests'
            sh 'docker images -q -f dangling=true | xargs -I ARGS docker rmi -f ARGS'
            allure results: [[path: 'allure-result']]
        }
    }
}