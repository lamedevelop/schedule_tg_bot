from Configs.crontab import crontab as config
from Controllers.Log.LogController import LogController
from Controllers.CrontabController import CrontabController


class CronManager:

    @staticmethod
    def install():
        crontab = ""

        LogController().info("Cron installed")

        for task_name in config['tasks']:
            task = config['tasks'][task_name]
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
