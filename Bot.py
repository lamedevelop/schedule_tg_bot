import telebot
# from telebot import types

import telegram

import cherrypy

from Configs.tgConfig import *
from DbManager import DbManager
from TelegramViewController import TelegramViewController
from UserController import UserController


bot = telebot.TeleBot(BOT_TOKEN)

dbManager = DbManager()
viewController = TelegramViewController()
userController = UserController()


# class WebhookServer(object):
#     @cherrypy.expose
#     def index(self):
#         if 'content-length' in cherrypy.request.headers and \
#                 'content-type' in cherrypy.request.headers and \
#                 cherrypy.request.headers['content-type'] == 'application/json':
#
#             length = int(cherrypy.request.headers['content-length'])
#             json_string = cherrypy.request.body.read(length).decode("utf-8")
#             update = telebot.types.Update.de_json(json_string)
#
#             bot.process_new_updates([update])
#             return ''
#         else:
#             raise cherrypy.HTTPError(403)


@bot.message_handler(commands=["start"])
def chooseUniversity(message):
    userController.CURR_STATUS = UserController().DEFAULT_STATUS

    userInfo = {
        'user_id': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
    }

    dbManager.addUser(userInfo)

    startMsg = viewController.getStartMsg()
    markup = viewController.getUniversityKeyboardMarkup()
    bot.send_message(
        message.chat.id,
        startMsg.format(message.from_user.first_name),
        reply_markup=markup,
        parse_mode="markdown"
    )


@bot.message_handler(commands=["help"])
def sendHelp(message):
    bot.send_message(
        message.chat.id, 
        'Default *help*', 
        parse_mode="markdown"
    )


@bot.message_handler(func=lambda message: True, content_types=["text"])
def main(message):
    replyMsg = "default reply"

    universities = DbManager().getUniversities()
    for university in universities:
        if userController.CURR_STATUS == UserController().DEFAULT_STATUS and message == university[0]:

            universityId = DbManager().getUniversityIdByName(message)

            userController.CURR_STATUS = UserController().UNIVERSITY_CHOSEN
        else:
            replyMsg = "University already chosen" \
                       "If you want to chose another one type /start"


    bot.send_message(message.chat.id, replyMsg, parse_mode="markdown")
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBSjVfUVrzol8Zw2y2gZUGYZxVd-jRHAACrAADaJpdDJxjOnTSw630GwQ')


bot.remove_webhook()
bot.polling()
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))
#
#
# cherrypy.config.update({
#     'server.socket_host': WEBHOOK_LISTEN,
#     'server.socket_port': WEBHOOK_PORT,
#     'server.ssl_module': 'builtin',
#     'server.ssl_certificate': WEBHOOK_SSL_CERT,
#     'server.ssl_private_key': WEBHOOK_SSL_PRIV
# })
#
# cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
