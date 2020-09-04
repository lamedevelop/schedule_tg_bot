from datetime import datetime


class LogController:
    log_filename = 'Logs/logfile_%s.txt'
    toFile = True

    def __init__(self, to_file=True):
        self.toFile = to_file

    def info(self, event):
        message = "INFO | " + self.getCurrDateAndTime() + " | " + event
        print(message)
        if self.toFile:
            self.writeToFile(message)

    def alert(self, event):
        message = "ALERT | " + self.getCurrDateAndTime() + " | " + event
        print(message)
        if self.toFile:
            self.writeToFile(message)

    def getCurrDate(self):
        return datetime.now().strftime("%d_%m_%Y")

    def getCurrDateAndTime(self):
        return datetime.now().strftime("%d_%m_%Y-%H:%M:%S")

    def writeToFile(self, message):
        with open(self.log_filename % self.getCurrDate(), 'a') as file:
            file.write(message + '\n')
