import os
from datetime import datetime

from Controllers.File.FileController import FileController


class LogController:
    log_filename = 'Logs/logfile_%s.log'
    toFile = True

    def __init__(self, to_file = True):
        self.toFile = to_file

    def info(self, event: str):
        message = "INFO | " + self.getCurrDateAndTime() + " | " + event
        print(message)
        filepath = self.log_filename % self.getCurrDate()
        if self.toFile:
            FileController.writeToFile(filepath, message)

    def alert(self, event: str):
        message = "ALERT | " + self.getCurrDateAndTime() + " | " + event
        print(message)
        filepath = self.log_filename % self.getCurrDate()
        if self.toFile:
            FileController.writeToFile(filepath, message)

    def getCurrDate(self):
        return datetime.now().strftime("%d-%m-%Y")

    def getCurrDateAndTime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
