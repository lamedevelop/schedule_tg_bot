import os


class FileController:

    @staticmethod
    def _createPath(filepath):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as error:
            print("Error while creating path to log file", error)

    @staticmethod
    def writeToFile(filepath, message):
        if not os.path.exists(os.path.dirname(filepath)):
            FileController._createPath(filepath)

        if isinstance(message, str):
            FileController._writeString(filepath, message)
        elif isinstance(message, list):
            FileController._writeArray(filepath, message)

    @staticmethod
    def _writeString(filepath, message: str):
        with open(filepath, 'a') as file:
            file.write(message + '\n')

    @staticmethod
    def _writeArray(filepath, message: list):
        with open(filepath, 'a') as file:
            for x in message:
                file.write(x)
