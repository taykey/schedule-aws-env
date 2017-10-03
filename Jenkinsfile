node {
    stage ('checkout'){
         checkout([$class: 'GitSCM',
             branches: [[name: '*/master']],
             doGenerateSubmoduleConfigurations: false,
             extensions: [
                 [$class: 'CleanBeforeCheckout'],
                 [$class: 'CloneOption', noTags: true, reference: '', shallow: true]
             ],
             submoduleCfg: [],
             userRemoteConfigs: [[url: 'https://github.com/taykey/schedule-aws-env.git']]
         ])

    }
    stage('Prepare') {
        echo 'Preparing environment..'
        if (isUnix()) {
            sh 'sudo add-apt-repository ppa:jonathonf/python-3.6'
            sh 'sudo apt-get update'
            sh 'sudo apt-get install python3.6 -y'
            sh 'sudo apt-get install python-pip -y'
            sh 'sudo apt-get install build-essential libssl-dev libffi-dev python3-dev -y'
            sh 'pip install virtualenv'
            sh """
                virtualenv -p python3.6 venv
                . venv/bin/activate
                pip install --user pybuilder
                pyb install_dependencies
            """
        }
    }
    stage('Build') {
        echo 'Building..'
    }
    stage('Test') {
        echo 'Testing..'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }

}