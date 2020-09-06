from Controllers.File.FileController import FileController
from Controllers.Date.DateTimeController import DateTimeController


class LogController:
    log_filename = 'Logs/logfile_%s.log'
    toFile = True

    def __init__(self, to_file = True):
        self.toFile = to_file

    def info(self, event: str):
        message = "INFO | " + DateTimeController.getCurrDateAndTime() + " | " + event
        print(message)
        filepath = self.log_filename % DateTimeController.getCurrDate()
        if self.toFile:
            FileController.writeToFile(filepath, message)

    def alert(self, event: str):
        message = "ALERT | " + DateTimeController.getCurrDateAndTime() + " | " + event
        print(message)
        filepath = self.log_filename % DateTimeController.getCurrDate()
        if self.toFile:
            FileController.writeToFile(filepath, message)
