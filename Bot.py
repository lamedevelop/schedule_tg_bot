import telebot
from telebot import types

import telegram

import cherrypy

from Configs.tgConfig import *


bot = telebot.TeleBot(BOT_TOKEN)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                'content-type' in cherrypy.request.headers and \
                cherrypy.request.headers['content-type'] == 'application/json':

            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)

            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=["start"])
def keyboard (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/help')
    bot.send_message(message.chat.id, "Default start", reply_markup=markup)


@bot.message_handler(commands=["help"])
def sendHelp(message):
    bot.send_message(
        message.chat.id, 
        'Default *help*', 
        parse_mode=telegram.ParseMode.MARKDOWN
    )


@bot.message_handler(func=lambda message: True, content_types=["text"])
def main(message):
    bot.send_message(message.chat.id, message.text, parse_mode=telegram.ParseMode.MARKDOWN)


bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))


cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})