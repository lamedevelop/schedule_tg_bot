import os

from Controllers.CliArgsController import CliArgsController
from Controllers.DateTimeController import DateTimeController
from Controllers.Db.PostgreDbController import PostgreDbController


class DumpController:

    dump_filename_pattern = 'dump_%s.tar.bz2'

    archive_command_pattern = 'tar -czf %s %s %s'
    curl_command_pattern = 'curl -F document=@"%s" "%s"'

    api_url = 'https://api.telegram.org/bot%s/sendDocument?chat_id=%s'

    def __init__(self):
        self.config = CliArgsController.getConfig()

    def generateDump(self):
        PostgreDbController().makeDump()
        command = self.archive_command_pattern % (
            self.getDumpFilename(),
            self.getLogsPath(),
            self.config.DUMP_FILENAME
        )
        os.system(command)
        os.remove(self.config.DUMP_FILENAME)

    def sendDump(self):
        url = self.api_url % (
            self.config.MONITORING_BOT_TOKEN,
            self.config.NOTIFICATION_CHAT_ID
        )
        command = self.curl_command_pattern % (self.getDumpFilename(), url)
        os.system(command)
        os.remove(self.getDumpFilename())

    def dump(self):
        self.generateDump()
        self.sendDump()

    def getDumpFilename(self):
        dump_filename = self.dump_filename_pattern % DateTimeController.getCurrDate()
        return self.config.LOGS_FOLDER + dump_filename

    def getLogsPath(self):
        return self.config.LOGS_FOLDER + '*'
