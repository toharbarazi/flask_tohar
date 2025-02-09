pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // משלב את הקוד מריפוזיטוריית Git
                git 'https://github.com/toharbarazi/flask_tohar.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // התקנת כל התלויות ב-virtualenv
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // הרצת בדיקות
                script {
                    // אם יש לך קבצי בדיקה, הריצה תעשה כאן
                    sh '. venv/bin/activate && pytest tests/'
                }
            }
        }

        stage('Deploy') {
            steps {
                // פריסה (אפשר להשאיר ריקה אם אין צורך)
                echo 'Deploying application...'
            }
        }
    }
}

