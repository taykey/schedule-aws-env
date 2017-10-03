pipeline {
    agent any
        // Adds timestamps to the output logged by steps inside the wrapper.
    timestamps {
        stages {
            stage('Prepare') {
                steps {
                    echo 'Preparing environment..'
                    if(isUnix()) {
                        sh 'sudo add-apt-repository ppa:jonathonf/python-3.6'
                        sh 'sudo apt-get update'
                        sh 'sudo apt-get install python3.6'
                        sh 'sudo apt-get install pip'
                        sh 'pip install virtualenv'
                        sh 'virtualenv -p python3.6 venv'
                        sh 'source venv/bin/activate'
                        sh 'pip install pybuilder'
                        sh 'pyb install_dependencies'
                    }
                }
            }
            stage('Build') {
                steps {
                    echo 'Building..'
                }
            }
            stage('Test') {
                steps {
                    echo 'Testing..'
                }
            }
            stage('Deploy') {
                steps {
                    echo 'Deploying....'
                }
            }
        }
    }
}