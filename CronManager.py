import Configs.crontab as config_provider
from Controllers.Crontab.CrontabController import CrontabController


# todo: include running of this manager to the final startup script
class CronManager:

    @staticmethod
    def installCrontab():
        crontab = ""
        config = config_provider.getCrontab()

        for task in config['tasks']:
            if task['is_active']:
                crontab += task['command'] + "\t# " + task['comment'] + "\n"

        CrontabController.installCrontab(crontab)

    @staticmethod
    def enableCrontab():
        CrontabController.enableCrontab()

    @staticmethod
    def disableCrontab():
        CrontabController.diasbleCrontab()

    @staticmethod
    def removeCrontab():
        CrontabController.removeCrontab()
