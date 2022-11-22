pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('practise') {
            steps {
                echo 'practising jenkins for job'
            }
        }      
        stage('python') {
            steps {
                echo 'running python script'
                bat 'python abhi/text.py'
            } 
            
       }    
    }        
}    
    
    
    
