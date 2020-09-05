import json

from Controllers.Log.LogController import LogController
from Controllers.File.FileController import FileController


class ParseController:

    logger = LogController()

    def __init__(self):
        pass

    def run(self, name: str):
        self.logger.info("Parser %s started" % self.__class__.__name__)
        json = self.getJson(self._parse())
        filepath = f'{name}.json'
        FileController.writeToFile(filepath, json)

    def _parse(self):
        pass

    def getJson(self, dict):
        return json.dumps(dict, indent=4, ensure_ascii=False)
