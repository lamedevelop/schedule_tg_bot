import json


class ParseController:

    def __init__(self):
        pass

    def run(self, name: str):
        json = self.getJson(self._parse())
        f = open(f'{name}.json', 'w', encoding='utf-8')
        for x in json:
            f.write(x)
        f.close()

    def _parse(self):
        pass

    def getJson(self, dict):
        return json.dumps(dict, indent=4, ensure_ascii=False)
