import telebot
# from telebot import types

from Configs.tgConfig import *
from DbManager import DbManager
from Controllers.View.TelegramViewController import TelegramViewController
from Controllers.User.UserController import UserController

from Controllers.Log.LogController import LogController
from NotificationManager import NotificationManager

from ParseManager import ParseManager

bot = telebot.TeleBot(BOT_TOKEN)

dbManager = DbManager()
parseManager = ParseManager()

viewController = TelegramViewController()
userController = UserController()

logger = LogController()
notificator = NotificationManager()


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


@bot.message_handler(commands=["start", "changeuniversity"])
def chooseUniversity(message):
    userInfo = {
        'user_id': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
    }
    dbManager.addTgUser(userInfo)
    dbManager.updateTgUser(message.from_user.id, "university_id", "NULL")
    dbManager.updateTgUser(message.from_user.id, "group_id", "NULL")

    log_msg = "Bot was started by the user id: {}, name: {}, username: {}".format(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.username
    )
    notificator.notify(log_msg, NotificationManager.INFO_LEVEL)
    logger.info(log_msg)

    bot.send_message(
        message.chat.id,
        'Привет *{}*!\nВыбери свой *университет*'.format(
            message.from_user.first_name),
        reply_markup=viewController.getUniversityKeyboardMarkup(),
        parse_mode="markdown"
    )


@bot.message_handler(commands=["changegroup"])
def sendHelp(message):
    dbManager.updateTgUser(message.from_user.id, "group_id", "NULL")
    bot.send_message(
        message.chat.id,
        'Введи новую *группу*',
        reply_markup=viewController.removeKeyboardMarkup(),
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
                    "Университет *выбран*\nВведи группу, используя русские буквы",
                    reply_markup=viewController.removeKeyboardMarkup(),
                    parse_mode="markdown",
                )
                break

    elif userController.CURR_STATUS == userController.UNIVERSITY_CHOSEN:
        universityId = userController.getUserUniversityId(message.from_user.id)
        groups = dbManager.getGroupsByUniversityId(universityId)
        userGroupName = message.text.lower()

        isGroupFound = False
        for group in groups:
            if userGroupName == group[1]:
                groupId = group[0]
                dbManager.updateTgUser(
                    message.from_user.id, "group_id", groupId)

                isGroupFound = True
                bot.send_message(
                    message.chat.id,
                    "Группа *найдена*!\nВыбери день, чтобы узнать *расписание*",
                    reply_markup=viewController.getScheduleKeyboardMarkup(),
                    parse_mode="markdown"
                )
                break

        if not isGroupFound:
            json_text = parseManager.getJson(universityId, userGroupName)
            if len(json_text) > 2:
                groupInfo = {
                    "group_name": userGroupName,
                    "university_id": universityId,
                    "schedule_text": json_text,
                    "schedule_url": "default url"
                }

                dbManager.addGroup(groupInfo)
                groupId = dbManager.getGroupId(groupInfo)
                dbManager.updateTgUser(
                    message.from_user.id,
                    "group_id",
                    groupId
                )

                bot.send_message(
                    message.chat.id,
                    "Расписание *успешно загружено*!\nВыбери день, чтобы узнать *расписание*",
                    reply_markup=viewController.getScheduleKeyboardMarkup(),
                    parse_mode="markdown"
                )
            else:
                bot.send_message(
                    message.chat.id,
                    "Группа *не найдена*!\nПопробуйте другую группу",
                    parse_mode="markdown"
                )

    elif userController.CURR_STATUS == userController.GROUP_CHOSEN:
        userGroupId = userController.getUserGroupId(message.from_user.id)
        groupJsonText = dbManager.getGroupJsonById(userGroupId)

        if message.text == "Понедельник" \
                or message.text == "Вторник" \
                or message.text == "Среда" \
                or message.text == "Четверг" \
                or message.text == "Пятница" \
                or message.text == "Суббота":
            bot.send_message(
                message.chat.id,
                parseManager.getDaySchedule(message.text, groupJsonText),
                parse_mode="markdown"
            )

        # todo: write rest messages to the db


bot.remove_webhook()


try:
    notificator.notify("Polling started", notificator.INFO_LEVEL)
    logger.info("Polling started")

    bot.polling()

    notificator.notify("Polling stopped manually", notificator.WARNING_LEVEL)
    logger.info("Polling stopped manually")
except Exception as e:
    notificator.notify('Error while polling: {}'.format(e), notificator.DISASTER_LEVEL)
    logger.alert('Error while polling: {}'.format(e))

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
