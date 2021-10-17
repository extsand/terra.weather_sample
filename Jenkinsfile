// https://www.jenkins.io/doc/pipeline/tour/environment/
// jenkins snipets
pipeline {
    agent any

		// chek git repo every minute
    triggers {
		// 	// every 1 minute
		// 	// pollSCM('H/2 * * * *')
			// pollSCM( '* * * * *')
		}

    environment {
       
		
    } 

		options {
        buildDiscarder(logRotator(
					numToKeepStr: '3', 
					artifactNumToKeepStr: '3'
					))
        timestamps()
    }

    stages {
        stage('Introducting') {
            steps {
                echo 'Hi User'
            }
        }
  
    }

		post {
          success {            
            // script here
					}
					aborted {             
            // script here
					}
					failure {
            // script here
					}
		}
    
}