from Controllers.FileController import FileController
from Controllers.CliArgsController import CliArgsController
from Controllers.DateTimeController import DateTimeController


class LogController:

    log_name_pattern = 'logfile_%s.log'

    def __init__(self, to_file=True):
        self.toFile = to_file
        self.config = CliArgsController.getConfig()

    def info(self, event: str):
        """Write log with info severity.

        @param event Occurred event description.
        """
        message = "INFO | " + DateTimeController.getCurrDateAndTime() + " | " + event
        self.writeLog(message)

    def alert(self, event: str):
        """Write log with alert severity.

        @param event Occurred error description.
        """
        message = "ALERT | " + DateTimeController.getCurrDateAndTime() + " | " + event
        self.writeLog(message)

    def writeLog(self, message):
        print(message)
        if self.toFile:
            FileController.writeToFile(self.getLogFilename(), message)

    def getLogFilename(self):
        """Construct log filename by pattern and date."""
        return self.config.LOGS_FOLDER + self.log_name_pattern % DateTimeController.getCurrDate()
