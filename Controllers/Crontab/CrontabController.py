from crontab import CronTab
import getpass


class CrontabController:

    @staticmethod
    def installCron(command, comment=''):
        cron = CronTab(user=getpass.getuser())
        cron.new(command=command, comment=comment)
        cron.write()

    @staticmethod
    def installCrontab(crontab):
        cron = CronTab(crontab)
        cron.write()

    @staticmethod
    def updateCrontab(jobs):
        cron = CronTab(user=getpass.getuser())
        for my_job in jobs:
            for job in cron:
                if job.comment == my_job['comment']:
                    job.command = my_job['command']
                    cron.write()

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
