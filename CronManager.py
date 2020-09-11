import Configs.crontab as config_provider
from Controllers.Crontab.CrontabController import CrontabController


class CronManager:

    @staticmethod
    def installCrons():
        # config = config_provider.getCrontab()
        CrontabController.installCron("* * * * * echo hello", "Hello world output")

    @staticmethod
    def removeCrontab():
        CrontabController.removeCrontab()

    # @staticmethod
    # def deleteCrons():
    #     config = config_provider.getCrontab()
    #
    # @staticmethod
    # def installCrons():
    #     config = config_provider.getCrontab()
