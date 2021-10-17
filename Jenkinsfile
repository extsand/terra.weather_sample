// https://www.jenkins.io/doc/pipeline/tour/environment/
// jenkins snipets+
// More about telegram notifications
// https://42point.com/posts/telegram-notifications-jenkins
pipeline {
    agent any

	
    environment {
			HEADER_MESSAGE = 'Notify example'
			BODY_MESSAGE = 'Application was deployed. You can open it in link below'
			APP_IP = '192.168.1.29'
      DB_IP = '102.123.2.3'

		
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
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d text='
								*${HEADER_MESSAGE}*
								${BODY_MESSAGE}
								[Application link](http://${APP_IP})
      					[Database link](http://${DB_IP})
								------------------------------
								*${VAR_TEXT}*
								*bold text*
								***italic***
								simple text
								`code example`
								[link Example](http://example.com)
								---------------------------------------
								**hello world** 
								__italic__
								```monospace```
								---------------------------------------
								<b>your text</b> — bold;
								<i>your text</i> — italics;
								<u>your text</u> — underlined;
								<s>your text</s> — strikethrough.
								'
							""")
						}	
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
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d text='
								ABORTED
								'
							""")
						}	
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
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d text='
								ABORTED
								'
							""")
						}	
					}

					
    
		}
}