class LogController:
    log_filename = '../../logfile.txt'
    toFile = True

    def __init__(self, to_file=True):
        self.toFile = to_file

    def info(self, event):
        message = "INFO | " + self.getCurrDate() + event
        print(message)
        if self.toFile:
            self.writeToFile(self, message)

    def alert(self, event):
        message = "ALERT | " + self.getCurrDate() + event
        print(message)
        if self.toFile:
            self.writeToFile(self, message)

    def getCurrDate(self):
        return ""

    def writeToFile(self, message):
        with open(self.log_filename, 'a') as file:
            file.write(message + '\n')
