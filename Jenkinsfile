pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout scm  
            }
        }
        stage('Show Files'){
            steps{
                sh 'dir'
            }
        }
        stage('Run Test'){
            steps{
                sh 'python3 -m unittest test_calculator.py -v'
            }
        }
        stage('Deploy'){
            steps{
                sh 'echo "Deploying the code"'
            }
        }
    }
}