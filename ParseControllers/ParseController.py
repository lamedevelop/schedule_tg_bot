import requests
import json
import re

from bs4 import BeautifulSoup  # https://pypi.org/project/beautifulsoup4/


class ParseController:

    NAME_DAYS = {
        "ПН": "Понедельник",
        "ВТ": "Вторник",
        "СР": "Среда",
        "ЧТ": "Четверг",
        "ПТ": "Пятница",
        "СБ": "Суббота"
    }

    def __init__(self, url):
        self.url = url

    def run(self, name: str):
        json = self._getJson(self._parse(self.url))
        f = open(f'{name}.json', 'w', encoding='utf-8')
        for x in json:
            f.write(x)
        f.close()

    def _parse(self, url):
        pass

    def _getJson(self, text):
        finalDict, timeArr = {}, {}
        day, time = "", ""
        pairs = []
        for result in text:
            if result:
                if len(result[0]) == 2:
                    if timeArr:
                        finalDict[day] = timeArr
                        timeArr = {}
                    day = self.NAME_DAYS[result[0]]
                elif len(result) == 1:
                    if pairs:
                        timeArr[time] = pairs
                        pairs = []
                    time = result[0]
                else:
                    pairs.append(
                        list(map(lambda x: x.replace("&#160;", " "), result)))
        if timeArr:
            timeArr[time] = pairs
            finalDict[day] = timeArr
        return json.dumps(finalDict, indent=4, ensure_ascii=False)
