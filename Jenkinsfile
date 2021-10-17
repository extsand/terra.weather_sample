// https://www.jenkins.io/doc/pipeline/tour/environment/
// jenkins snipets+
// More about telegram notifications
// https://42point.com/posts/telegram-notifications-jenkins
pipeline {
    agent any

	
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
								curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage -d chat_id=${TELEGRAM_CHAT_ID} -d parse_mode=markdown -d text='
								*${VAR_TEXT}*
								${VAR_TEXT} ${VAR_TEXT}

							 **bold**
								*italic*
								`code`
								~~strike~~
								<u>underline</u>
								<pre language="c++">code</pre>
								[text](http://example.com)
								'
							""")
						}	
					}

					
    
		}
}