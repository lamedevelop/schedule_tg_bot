from Controllers.CliController import CliController
from Controllers.FileController import FileController
from Controllers.DateTimeController import DateTimeController


class LogController:

    log_name_pattern = 'logfile_%s.log'

    def __init__(self, to_file=True):
        self.toFile = to_file
        self.config = CliController().getConfig()

    def info(self, event: str):
        message = "INFO | " + DateTimeController.getCurrDateAndTime() + " | " + event
        self.writeLog(message)

    def alert(self, event: str):
        message = "ALERT | " + DateTimeController.getCurrDateAndTime() + " | " + event
        self.writeLog(message)

    def writeLog(self, message):
        print(message)
        if self.toFile:
            FileController.writeToFile(self.getLogFilename(), message)

    def getLogFilename(self):
        return self.config.LOGS_FOLDER + self.log_name_pattern % DateTimeController.getCurrDate()
