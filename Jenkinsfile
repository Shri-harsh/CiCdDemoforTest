pipeline{
    agent any
    parameters{
        choice(name: 'Environment', choices: ['Stage','Prod'], description: 'where to deploy')
    }
    stages{
        stage('checkout'){
            steps{
                checkout scm  
            }
        }
        stage('Show Files'){
            steps{
                sh 'ls -l'
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