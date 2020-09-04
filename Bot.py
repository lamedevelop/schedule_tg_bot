import telebot
# from telebot import types

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
    dbManager.addTgUser(userInfo)

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
    userController.CURR_STATUS = userController.getCurrStatus(message.from_user.id)

    if userController.CURR_STATUS == userController.DEFAULT_STATUS:
        universities = dbManager.getUniversities()

        for university in universities:
            if message.text == university[0]:
                universityId = dbManager.getUniversityIdByName(message.text)[0][0]
                dbManager.updateTgUser(message.from_user.id, "university_id", universityId)
                userController.CURR_STATUS = userController.UNIVERSITY_CHOSEN

                bot.send_message(
                    message.chat.id,
                    viewController.getUniversitySpecifiedMsg(),
                    reply_markup=viewController.getGroupKeyboardMarkup(universityId),
                    parse_mode="markdown"
                )

    elif userController.CURR_STATUS == userController.UNIVERSITY_CHOSEN:
        universityId = userController.getUserUniversityId(message.from_user.id)
        groups = dbManager.getGroupsByUniversityId(universityId)


        print(
            "userController.CURR_STATUS: ", userController.CURR_STATUS,
            "\nuniversityId: ", universityId,
            "\ngroups: ", groups,
        )

        for group in groups:
            if message == group[1]:
                groupId = group[0]
                dbManager.updateTgUser(message.from_user.id, "group_id", groupId)
                userController.CURR_STATUS = userController.GROUP_CHOSEN

                bot.send_message(
                    message.chat.id,
                    viewController.getGroupSpecifiedMsg(),
                    reply_markup=viewController.getScheduleKeyboardMarkup(),
                    parse_mode="markdown"
                )

    elif userController.CURR_STATUS == userController.GROUP_CHOSEN:
        if message == "monday":
            bot.send_message(message.chat.id, "monday", parse_mode="markdown")
        if message == "tuesday":
            bot.send_message(message.chat.id, "tuesday", parse_mode="markdown")
        if message == "wednesday":
            bot.send_message(message.chat.id, "wednesday", parse_mode="markdown")
        if message == "thursday":
            bot.send_message(message.chat.id, "thursday", parse_mode="markdown")
        if message == "friday":
            bot.send_message(message.chat.id, "friday", parse_mode="markdown")
        if message == "saturday":
            bot.send_message(message.chat.id, "saturday", parse_mode="markdown")


bot.remove_webhook()


try:
    bot.polling()
except Exception as e:
    print('Error while polling: {}'.format(e))

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
