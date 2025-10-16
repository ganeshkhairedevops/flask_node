pipeline {
    agent any
    stages{
        
        stage("code"){
            steps{
                echo "this is cloning the code"
                git url: "https://github.com/ganeshkhairedevops/flask_node.git", branch: "main"
                echo "Code Cloneing Sucessful"
            }
        
        }
        stage("build"){
            steps{
                echo "this is cloning the code"
                
            }
        }
        stage("Test"){
            steps{
                echo "this is testing the code"
            }
        }
        stage("deploy"){
            steps{
                echo "this is deploy the code"
                sh "docker-compose up --build -d"
                
            }
        }
    }
}
