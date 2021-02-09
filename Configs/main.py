# Bot
# Configure your own telegram token for your bot,
# your monitoring bot and also your monitoring chat,
# monitoring bot will send notifications there.
BOT_TOKEN = "token must be here"
MONITORING_BOT_TOKEN = "monitoring bot token must be here"
NOTIFICATION_CHAT_ID = -000000000

# Db
# SqlLite db filename
DB_FILENAME = '/usr/src/app/sqlite.db'

# Postgre db config
POSTGRES_DB = 'database'
POSTGRES_USERNAME = 'postgres'
POSTGRES_PASSWORD = 'secret'
POSTGRES_HOST = 'postgresql_domain'
POSTGRES_PORT = '5432'
POSTGRES_CONN_TIMEOUT = 5

# Maria db config
MARIA_DB = 'database'
MARIA_USERNAME = 'maria'
MARIA_PASSWORD = 'secret'
MARIA_HOST = 'localhost'
MARIA_PORT = '3306'
MARIA_CONN_TIMEOUT = 2

# Home project directory
PROJECT_PATH = '/usr/src/app/'

# Logging
# Main logging folder.
LOGS_FOLDER = '/usr/src/app/Logs/'
DUMP_FILENAME = '/usr/src/app/Logs/dump.sql'

# Mail
# Sender credentials.
MAIL_PORT = 465
MAIL_SMTP_SERVER = "smtp.mail.com"
MAIL_SENDER = "your@mail.com"
MAIL_PASSWORD = "mail_password"
MAIL_RECEIVERS = ["receiver1@mail.com", "receiver2@mail.com"]
