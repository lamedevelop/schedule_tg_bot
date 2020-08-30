  #!/usr/bin/python3.6
# -*- coding: utf-8 -*-


import config
from config import *


class WebServerManager:


    def __init__(self):
        self.raiseServer(self)


    def raiseServer(self):
		# Settings for cherrypy web-server

		cherrypy.config.update({
		    'server.socket_host': WEBHOOK_LISTEN,
		    'server.socket_port': WEBHOOK_PORT,
		    'server.ssl_module': 'builtin',
		    'server.ssl_certificate': WEBHOOK_SSL_CERT,
		    'server.ssl_private_key': WEBHOOK_SSL_PRIV
		})

		cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})