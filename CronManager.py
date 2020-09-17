import Configs.crontab as config_provider
from Controllers.Crontab.CrontabController import CrontabController

from Controllers.Log.LogController import LogController


# todo: include running of this manager to the final startup script
class CronManager:

    @staticmethod
    def install():
        crontab = ""
        config = config_provider.getCrontab()

        LogController().info("Cron installed")

        for task in config['tasks']:
            if task['is_active']:
                crontab += task['command'] + "\t# " + task['comment'] + "\n"

        CrontabController.installCrontab(crontab)

    @staticmethod
    def enable():
        LogController().info("Cron enabled")
        CrontabController.enableCrontab()

    @staticmethod
    def disable():
        LogController().info("Cron disabled")
        CrontabController.disableCrontab()

    @staticmethod
    def erase():
        LogController().info("Cron erased")
        CrontabController.removeCrontab()
