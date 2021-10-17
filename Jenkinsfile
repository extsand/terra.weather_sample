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
			VAR_TEXT = 'Hello from docker master'
       
		
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
           withCredentials([string(
						credentialsId: 'chat_id', 
						variable: 'TELEGRAM_CHAT_ID'
						), 
						string(
						credentialsId: 'Bot_TOKEN', 
						variable: 'TELEGRAM_BOT_TOKEN')]) {
							sh  ("""
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d 
								text='
								*${VAR_TEXT}* : 
								POC *Branch*: some_branch
								*Build* : OK 
								*Published* = YES'
							""")
						}	

					aborted {            
           withCredentials([string(
						credentialsId: 'chat_id', 
						variable: 'TELEGRAM_CHAT_ID'
						), 
						string(
						credentialsId: 'Bot_TOKEN', 
						variable: 'TELEGRAM_BOT_TOKEN')]) {
							sh  ("""
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d 
								text='
								*OTMENILY* : 
								POC *Branch*: some_branch
								*Build* : OK 
								*Published* = YES'
							""")
						}	
						
					failure {            
           withCredentials([string(
						credentialsId: 'chat_id', 
						variable: 'TELEGRAM_CHAT_ID'
						), 
						string(
						credentialsId: 'Bot_TOKEN', 
						variable: 'TELEGRAM_BOT_TOKEN')]) {
							sh  ("""
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d 
								text='
								*POLOMALOS* : 
								POC *Branch*: some_branch
								*Build* : OK 
								*Published* = YES'
							""")
						}	
				
		}
    
}