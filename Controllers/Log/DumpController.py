import os

from Configs.db import dbFilename
from Controllers.Date.DateTimeController import DateTimeController
from Configs.tgConfig import MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID


class DumpController:

    dump_filename_pattern = '/usr/src/app/Logs/dump_%s.tar.bz2'

    logs_dir = '/usr/src/app/Logs/*'

    archive_command_pattern = 'tar -czf %s %s %s'
    curl_command_pattern = 'curl -F document=@"%s" "%s"'

    api_url = 'https://api.telegram.org/bot%s/sendDocument?chat_id=%s'

    dump_file = ''

    def generateDump(self):
        self.dump_file = self.dump_filename_pattern % DateTimeController.getCurrDate()
        command = self.archive_command_pattern % (self.dump_file, self.logs_dir, dbFilename)
        os.system(command)

    def sendDump(self):
        url = self.api_url % (MONITORING_BOT_TOKEN, NOTIFICATION_CHAT_ID)
        command = self.curl_command_pattern % (self.dump_file, url)
        os.system(command)
        os.remove(self.dump_file)

    def dump(self):
        self.generateDump()
        self.sendDump()
