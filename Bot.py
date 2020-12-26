from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from Configs.tgConfig import *
from DbManager import DbManager
from Controllers.View.TelegramViewController import TelegramViewController
from Controllers.User.UserController import UserController

from Controllers.Log.LogController import LogController
from MonitoringAlertManager import MonitoringAlertManager

from ParseManager import ParseManager


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dbManager = DbManager()
parseManager = ParseManager()

viewController = TelegramViewController()
userController = UserController()

logger = LogController()
notificator = MonitoringAlertManager()


@dp.message_handler(commands=["start", "changeuniversity"])
async def chooseUniversity(message):
    userInfo = {
        'chat_id': message.chat.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
        'language_code': message.from_user.language_code,
        'is_alive': True
    }

    if not dbManager.checkUserExist(userInfo['chat_id']):
        dbManager.addTgUser(userInfo)

        log_msg = "Bot was started by the user id: {}, name: {}, username: {}".format(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.username
        )
        notificator.notify(log_msg, MonitoringAlertManager.INFO_LEVEL)
        logger.info(log_msg)
    else:
        # probably reinstalled
        # todo: add handler in user activity tracking task
        dbManager.updateTgUser(
            message.from_user.id,
            {
                "is_alive": "1",
                "university_id": '',
                "group_id": '',
            }
        )

        log_msg = "User {} restarted the bot".format(userInfo.get("username"))
        notificator.notify(log_msg, MonitoringAlertManager.INFO_LEVEL)
        logger.info(log_msg)

    await send_message_custom(
        message,
        'Привет *{}*!\nВыбери свой *университет*'.format(message.from_user.first_name),
        reply_markup=viewController.getUniversityKeyboardMarkup()
    )


@dp.message_handler(commands=["changegroup"])
async def sendHelp(message):
    dbManager.updateTgUser(
        message.from_user.id,
        {"group_id": "NULL"}
    )

    await send_message_custom(
        message,
        'Введи новую *группу* русскими буквами\n'
        'Например так: *а-12м-20* или *иу3-13б*',
        reply_markup=viewController.removeKeyboardMarkup()
    )


@dp.message_handler(commands=["help"])
async def sendHelp(message):
    await send_message_custom(
        message,
        '''
Начало использования
/start

Для смены *университета*
/changeuniversity

Для смены *группы*
/changegroup

Получить это сообщение
/help

Номер группы вводится *русскими буквами*, например так:
ИУ3-13б
А-12м-20

Контакты для связи:
@kekmarakek и @grit4in
        '''
    )


@dp.message_handler()
async def main(message):
    CURR_STATUS = userController.getCurrStatus(message.from_user.id)

    dbManager.writeUserMessage({
        'chat_id': message.from_user.id,
        'user_status': CURR_STATUS,
        'message': message.text
    })

    if CURR_STATUS == userController.DEFAULT_STATUS:
        universities = dbManager.getUniversities()

        for university in universities:
            if message.text == university['university_name']:
                dbManager.updateTgUser(
                    message.from_user.id,
                    {"university_id": university['university_id']}
                )

                await send_message_custom(
                    message,
                    'Университет *выбран*\n'
                    'Введи номер группы, *русскими буквами*\n'
                    'Например так: *а-12м-20* или *иу3-13б*',
                    reply_markup=viewController.removeKeyboardMarkup()
                )
                break

    elif CURR_STATUS == userController.UNIVERSITY_CHOSEN:
        universityId = userController.getUserUniversityId(message.from_user.id)
        userGroupName = parseManager.filterGroup(message.text)
        group = dbManager.getGroup({
            'group_name': userGroupName,
            'university_id': universityId
        })

        if bool(group):
            groupId = group['group_id']
            dbManager.updateTgUser(
                message.from_user.id,
                {"group_id": groupId}
            )
            await send_message_custom(
                message,
                "Группа *найдена*!\nВыбери день, чтобы узнать *расписание*",
                reply_markup=viewController.getScheduleKeyboardMarkup()
            )

        else:
            jsonSchedule = parseManager.getJson(universityId, userGroupName)
            if len(jsonSchedule) > 2:
                groupInfo = {
                    "group_name": userGroupName,
                    "university_id": universityId,
                    "schedule_text": jsonSchedule,
                    "schedule_url": "default url"
                }

                groupId = dbManager.addGroup(groupInfo)
                dbManager.updateTgUser(
                    message.from_user.id,
                    {"group_id": groupId}
                )

                await send_message_custom(
                    message,
                    "Расписание *успешно загружено*!\nВыбери день, чтобы узнать *расписание*",
                    reply_markup=viewController.getScheduleKeyboardMarkup()
                )
            else:
                await send_message_custom(
                    message,
                    "Группа *не найдена*!\nПопробуйте другую группу"
                )

    elif CURR_STATUS == userController.GROUP_CHOSEN:
        if message.text in [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота"
        ]:
            userGroupId = userController.getUserGroupId(message.from_user.id)
            groupJsonText = dbManager.getScheduleByGroupId(userGroupId)
            userChoice = TelegramViewController.removeLookHereFilter(message.text)

            await send_message_custom(
                message,
                parseManager.getDaySchedule(userChoice, groupJsonText),
                reply_markup=viewController.getScheduleKeyboardMarkup()
            )


async def send_message_custom(
    message,
    text: str,
    reply_markup=None,
    parse_mode="markdown"
):
    try:
        await bot.send_message(
            message.chat.id,
            text,
            reply_markup=reply_markup,
            parse_mode=parse_mode
        )

    except Exception as e:
        if "bot was blocked by the user" in str(e):
            dbManager.updateTgUser(
                message.from_user.id,
                {"is_alive": "0"}
            )

            error_message = 'Send message error: user {} blocked the bot'.format(message.from_user.id)
            notificator.notify(error_message, notificator.WARNING_LEVEL)
            logger.alert(error_message)
        else:
            error_message = 'Send message error with user {}: {}'.format(message.from_user.id, e)
            notificator.notify(error_message, notificator.DISASTER_LEVEL)
            logger.alert(error_message)


try:
    notificator.notify("Polling started", notificator.INFO_LEVEL)
    logger.info("Polling started")

    executor.start_polling(dp)

    notificator.notify("Polling stopped manually", notificator.WARNING_LEVEL)
    logger.info("Polling stopped manually")
except Exception as e:
    notificator.notify('Error while polling: {}'.format(e), notificator.DISASTER_LEVEL)
    logger.alert('Error while polling: {}'.format(e))
