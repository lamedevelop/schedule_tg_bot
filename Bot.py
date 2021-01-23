import os

from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from DbManager import DbManager
from ParseManager import ParseManager
from AlertManager import AlertManager

from Controllers.UserController import UserController
from Controllers.Log.LogController import LogController
from Controllers.CliArgsController import CliArgsController
from Controllers.TelegramViewController import TelegramViewController
from Controllers.Translation.TranslationController import TranslationController


configImporter = CliArgsController()
configImporter.parseArgs()
config = configImporter.getConfig()

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

parser = ParseManager()
dbManager = DbManager()
alertManager = AlertManager()

logger = LogController()
userController = UserController()
viewController = TelegramViewController()
messageGenerator = TranslationController()


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
        alertManager.notify(log_msg, AlertManager.INFO_LEVEL)
        logger.info(log_msg)
    else:
        # probably reinstalled
        # todo: add handler in user activity tracking task SB-61
        dbManager.updateTgUser(
            message.from_user.id,
            {
                "is_alive": True,
                "university_id": '',
                "group_id": '',
            }
        )

        log_msg = "User {} restarted the bot".format(userInfo.get("chat_id"))
        alertManager.notify(log_msg, AlertManager.INFO_LEVEL)
        logger.info(log_msg)

    await send_message_custom(
        message,
        messageGenerator.getMessage(
            message.from_user.language_code,
            messageGenerator.ENTER_UNIVERSITY
        ).format(message.from_user.first_name),
        reply_markup=viewController.getUniversityKeyboardMarkup()
    )


@dp.message_handler(commands=["changegroup"])
async def sendHelp(message):
    dbManager.updateTgUser(
        message.from_user.id,
        {"group_id": ''}
    )

    await send_message_custom(
        message,
        messageGenerator.getMessage(
            message.from_user.language_code,
            messageGenerator.CHANGE_GROUP
        ),
        reply_markup=viewController.removeKeyboardMarkup()
    )


@dp.message_handler(commands=["help"])
async def sendHelp(message):
    await send_message_custom(
        message,
        messageGenerator.getMessage(
            message.from_user.language_code,
            messageGenerator.HELP
        ),
    )


@dp.message_handler()
async def main(message):
    CURR_STATUS = userController.getCurrStatus(message.from_user.id)
    lang = message.from_user.language_code

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
                    messageGenerator.getMessage(
                        lang,
                        messageGenerator.FIRST_ENTER_GROUP
                    ),
                    reply_markup=viewController.removeKeyboardMarkup()
                )
                break

    elif CURR_STATUS == userController.UNIVERSITY_CHOSEN:
        universityId = userController.getUserUniversityId(message.from_user.id)
        userGroupName = parser.filterGroup(message.text)
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
                messageGenerator.getMessage(
                    lang,
                    messageGenerator.SCHEDULE_WAS_FOUND
                ),
                reply_markup=viewController.getScheduleKeyboardMarkup(lang)
            )

        else:
            jsonSchedule = parser.downloadSchedule(universityId, userGroupName)
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
                    messageGenerator.getMessage(
                        lang,
                        messageGenerator.SCHEDULE_DOWNLOADED
                    ),
                    reply_markup=viewController.getScheduleKeyboardMarkup(lang)
                )
            else:
                await send_message_custom(
                    message,
                    messageGenerator.getMessage(
                        lang,
                        messageGenerator.SCHEDULE_WAS_NOT_FOUND
                    ).format(message.from_user.first_name),
                )

    elif CURR_STATUS == userController.GROUP_CHOSEN:
        userChoice = TelegramViewController.removeFilters(message.text)

        if viewController.isDayOfWeek(userChoice):
            userGroupId = userController.getUserGroupId(message.from_user.id)
            groupJsonText = dbManager.getScheduleByGroupId(userGroupId)

            await send_message_custom(
                message,
                parser.getDaySchedule(userChoice, groupJsonText),
                reply_markup=viewController.getScheduleKeyboardMarkup(lang)
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
                {"is_alive": False}
            )

            error_message = 'Send message error: user {} blocked the bot'.format(message.from_user.id)
            alertManager.notify(error_message, alertManager.WARNING_LEVEL)
            logger.alert(error_message)
        else:
            error_message = 'Send message error with user {}: {}'.format(message.from_user.id, e)
            alertManager.notify(error_message, alertManager.DISASTER_LEVEL)
            logger.alert(error_message)


try:
    alertManager.notify("Polling started", alertManager.INFO_LEVEL)
    logger.info("Polling started")

    executor.start_polling(dp)

    alertManager.notify("Polling stopped manually", alertManager.WARNING_LEVEL)
    logger.info("Polling stopped manually")
except Exception as e:
    alertManager.notify('Error while polling: {}'.format(e), alertManager.DISASTER_LEVEL)
    logger.alert('Error while polling: {}'.format(e))
