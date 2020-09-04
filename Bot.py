import telebot
# from telebot import types

from Configs.tgConfig import *
from DbManager import DbManager
from Controllers.App.TelegramViewController import TelegramViewController
from Controllers.User.UserController import UserController


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
    userInfo = {
        'user_id': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
    }
    dbManager.addTgUser(userInfo)

    bot.send_message(
        message.chat.id,
        'Hello *{}*!\nIt\'s telegram schedule bot\nChoose your *university*'.format(message.from_user.first_name),
        reply_markup=viewController.getUniversityKeyboardMarkup(),
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
    dbManager.writeUserMessage(message.from_user.id, message.text)

    if userController.CURR_STATUS == userController.DEFAULT_STATUS:
        universities = dbManager.getUniversities()

        for university in universities:
            if message.text == university[0]:
                universityId = dbManager.getUniversityIdByName(message.text)[0][0]
                dbManager.updateTgUser(message.from_user.id, "university_id", universityId)

                bot.send_message(
                    message.chat.id,
                    "University *successfully specified*\nEnter your group",
                    reply_markup=viewController.getGroupKeyboardMarkup(universityId),
                    parse_mode="markdown"
                )

    if userController.CURR_STATUS == userController.UNIVERSITY_CHOSEN:
        universityId = userController.getUserUniversityId(message.from_user.id)
        groups = dbManager.getGroupsByUniversityId(universityId)
        userGroupName = message.text

        for group in groups:
            if userGroupName == group[1]:
                groupId = group[0]
                dbManager.updateTgUser(message.from_user.id, "group_id", groupId)

                bot.send_message(
                    message.chat.id,
                    "Group *successfully specified*\nChose day to get your *schedule*",
                    reply_markup=viewController.getScheduleKeyboardMarkup(),
                    parse_mode="markdown"
                )
            else:
                # run parser for this group here
                # scheduleUrl = parse...
                # schedule = parse...

                groupInfo = {
                    "group_name": userGroupName.lower(),
                    "university_id": universityId,
                    "schedule_text": "default schedule",
                    "schedule_url": "default url"
                }

                groupId = dbManager.getGroupId(groupInfo)
                dbManager.updateTgUser(message.from_user.id, "group_id", groupId)

                bot.send_message(
                    message.chat.id,
                    "Group *successfully added*\nChose day to get your *schedule*",
                    reply_markup=viewController.getScheduleKeyboardMarkup(),
                    parse_mode="markdown"
                )


    if userController.CURR_STATUS == userController.GROUP_CHOSEN:

        # todo: Implement schedule choose from db
        if message.text == "monday":
            bot.send_message(message.chat.id, "monday", parse_mode="markdown")
        if message.text == "tuesday":
            bot.send_message(message.chat.id, "tuesday", parse_mode="markdown")
        if message.text == "wednesday":
            bot.send_message(message.chat.id, "wednesday", parse_mode="markdown")
        if message.text == "thursday":
            bot.send_message(message.chat.id, "thursday", parse_mode="markdown")
        if message.text == "friday":
            bot.send_message(message.chat.id, "friday", parse_mode="markdown")
        if message.text == "saturday":
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
