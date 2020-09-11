import getpass
from crontab import CronTab


class CrontabController:

    @staticmethod
    def installCrontab(crontab):
        cron = CronTab(tab=crontab)
        cron.write_to_user(user=getpass.getuser())

    @staticmethod
    def enableCrontab():
        cron = CronTab(user=getpass.getuser())
        for job in cron:
            job.enable()
            cron.write()

    @staticmethod
    def diasbleCrontab():
        cron = CronTab(user=getpass.getuser())
        for job in cron:
            job.enable(False)
            cron.write()

    @staticmethod
    def removeCrontab():
        cron = CronTab(user=getpass.getuser())
        cron.remove_all()
        cron.write()
