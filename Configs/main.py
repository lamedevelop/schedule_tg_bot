import os

# Bot
# Configure your own telegram token for your bot,
# your monitoring bot and also your monitoring chat,
# monitoring bot will send notifications there.
BOT_TOKEN = os.environ['BOT_TOKEN']
MONITORING_BOT_TOKEN = os.environ['MONITORING_BOT_TOKEN']
NOTIFICATION_CHAT_ID = os.environ['NOTIFICATION_CHAT_ID']

# Db
# SqlLite db filename
DB_FILENAME = os.environ['DB_FILENAME']

# Maria db config
MARIA_DB = os.environ['MARIA_DB']
MARIA_USERNAME = os.environ['MARIA_USERNAME']
MARIA_PASSWORD = os.environ['MARIA_PASSWORD']
MARIA_HOST = os.environ['MARIA_HOST']
MARIA_PORT = os.environ['MARIA_PORT']
MARIA_CONN_TIMEOUT = os.environ['MARIA_CONN_TIMEOUT']

# Home project directory
PROJECT_PATH = os.environ['PROJECT_PATH']

# Logging
# Main logging folder.
LOGS_FOLDER = os.environ['LOGS_FOLDER']
DUMP_FILENAME = os.environ['DUMP_FILENAME']

# Mail
# Sender credentials.
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_SMTP_SERVER = os.environ['MAIL_SMTP_SERVER']
MAIL_SENDER = os.environ['MAIL_SENDER']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
MAIL_RECEIVERS = tuple(
    map(lambda x: x.strip(), os.environ['MAIL_RECEIVERS'].split(','))
)