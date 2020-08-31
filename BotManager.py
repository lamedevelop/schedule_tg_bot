import config
from config import *

from WebhookServer import WebhookServer
from Bot import Bot


class BotManager:

    def __init__(self):
        pass


    def startBot(self):
        bot = Bot()


    def startServer(self):
        cherrypy.config.update({
            'server.socket_host': WEBHOOK_LISTEN,
            'server.socket_port': WEBHOOK_PORT,
            'server.ssl_module': 'builtin',
            'server.ssl_certificate': WEBHOOK_SSL_CERT,
            'server.ssl_private_key': WEBHOOK_SSL_PRIV
        })

        cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
