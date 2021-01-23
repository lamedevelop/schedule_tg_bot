from Configs.crontab import crontab as config
from Controllers.Log.LogController import LogController
from Controllers.CrontabController import CrontabController


class CronManager:

    @staticmethod
    def install():
        """Install crontab from config file."""
        crontab = ""
        LogController().info("Cron installed")

        for task_name in config['tasks']:
            task = config['tasks'][task_name]
            if task['is_active']:
                crontab += f"# {task['comment']}\n{task['command']}\n"

        CrontabController.installCrontab(crontab)

    @staticmethod
    def enable():
        """Uncomment all existing records in crontab."""
        LogController().info("Cron enabled")
        CrontabController.enableCrontab()

    @staticmethod
    def disable():
        """Comments every record in crontab."""
        LogController().info("Cron disabled")
        CrontabController.disableCrontab()

    @staticmethod
    def erase():
        """Remove all records from crontab."""
        LogController().info("Cron erased")
        CrontabController.removeCrontab()
