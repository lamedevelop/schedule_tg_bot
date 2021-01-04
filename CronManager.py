import Configs.crontab as config_provider
from Controllers.Log.LogController import LogController
from Controllers.Crontab.CrontabController import CrontabController


class CronManager:

    @staticmethod
    def install():
        crontab = ""
        config = config_provider.getCrontab()

        LogController().info("Cron installed")

        for task in config['tasks']:
            if task['is_active']:
                crontab += f"# {task['comment']}\n{task['command']}\n"

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
