BOT_TOKEN = "token must be here"

#Config for web-server
WEBHOOK_HOST = ''
WEBHOOK_PORT = 80  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './name_of_file'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './name_of_file'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (BOT_TOKEN)