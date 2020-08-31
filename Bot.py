import telebot
from telebot import types
import telegram

from Configs.tgConfig import *
from WebhookServer import WebhookServer


bot = telebot.TeleBot(BOT_TOKEN)


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


bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))


cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(bot), WEBHOOK_URL_PATH, {'/': {}})