import json

from Controllers.Log.LogController import LogController
from Controllers.File.FileController import FileController


class ParseController:

    logger = LogController()

    def writeToJsonFile(self, file_name: str, group_name: str):
        self.logger.info("Parser %s started" % self.__class__.__name__)
        json = self.getJson(self._parse(group_name))
        filepath = f'{file_name}.json'
        FileController.writeToFile(filepath, json)

    def _parse(self):
        pass

    def makeJson(self, group_name: str):
        # return json.dumps(self._parse(group_name), indent=0, ensure_ascii=False)
        return str(self._parse(group_name))

    def __str__(self):
        return ''
