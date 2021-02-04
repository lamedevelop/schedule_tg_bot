
class AdminCommandsController:
    """
    AdminCommandsController(
        bot,
        dispatcher,
        config,
        dbManager,
        parser
    )

    All arguments are required.
    Class is a command extension for the tg bot.
    Pattern that was applied here could be used in further
    for additionally extending bot commands pack.
    """

    def __init__(self, bot, dispatcher, config, dbManager, parser):
        self.bot = bot
        self.dp = dispatcher
        self.init_methods()
        self.config = config
        self.dbManager = dbManager
        self.parser = parser

    def init_methods(self):
        @self.dp.message_handler(commands=["update_group"])
        async def updateGroup(message):
            if message.from_user.id in self.config.BOT_ADMINS:
                argument = message.get_args()

                if not argument:
                    await self.bot.send_message(
                        message.chat.id,
                        'Group not found',
                    )

                else:
                    self.dbManager.updateGroup(
                        self.parser.filterGroup(argument)
                    )
                    await self.bot.send_message(
                        message.chat.id,
                        'Group was updated',
                    )
            else:
                await self.bot.send_message(
                    message.chat.id,
                    'undefined command, please use the keyboard'
                )