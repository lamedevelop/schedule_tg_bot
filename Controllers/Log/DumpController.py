import os

from Controllers.Date.DateTimeController import DateTimeController
from Configs.main import DB_FILENAME, MONITORING_BOT_TOKEN, \
                            NOTIFICATION_CHAT_ID, LOGS_FOLDER


class DumpController:

    dump_filename_pattern = 'dump_%s.tar.bz2'

    archive_command_pattern = 'tar -czf %s %s %s'
    curl_command_pattern = 'curl -F document=@"%s" "%s"'

    api_url = 'https://api.telegram.org/bot%s/sendDocument?chat_id=%s'

    def generateDump(self):
        command = self.archive_command_pattern % (
            self.getDumpFilename(),
            self.getLogsPath(),
            DB_FILENAME
        )
        os.system(command)

    def sendDump(self):
        url = self.api_url % (MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID)
        command = self.curl_command_pattern % (self.getDumpFilename(), url)
        os.system(command)
        os.remove(self.getDumpFilename())

    def dump(self):
        self.generateDump()
        self.sendDump()

    def getDumpFilename(self):
        dump_filename = self.dump_filename_pattern % DateTimeController.getCurrDate()
        return LOGS_FOLDER + dump_filename

    @staticmethod
    def getLogsPath():
        return LOGS_FOLDER + '*'
