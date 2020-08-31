import json

import re
import requests

from bs4 import BeautifulSoup  # https://pypi.org/project/beautifulsoup4/

from ParseControllers.ParseController import ParseController


class MpeiParseController(ParseController):

    groupoid = 10342
    start = "2020.08.31"
    url = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=%d&start=%s" % (
        groupoid, start)

    def __init__(self):
        pass

    def run(self):

        jsonOUT = getJson(parse(self.url))
        # print(jsonOUT)

        f = open('text.json', 'w', encoding='utf-8')
        for x in jsonOUT:
            f.write(x)
        f.close()

    def parse(self, link):
        link = requests.get(url)
        if link.status_code == 200:
            html = link.text.replace("\n", "")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find(
                "table", class_="mpei-galaktika-lessons-grid-tbl")

            for x in table:
                td = x.find_all("td", class_=True)
                passFirstIter = True
                for outerTD in td:
                    if passFirstIter:
                        passFirstIter = False
                        continue
                    for innerTD in re.findall(r"<.+?>(.+?)</td>", str(outerTD)):
                        if len(innerTD) > 20:
                            innerTD = re.findall(
                                r"<span.+?>(.*?)</.+?<span.+?>(.*?)</.+?<span.+?>(.*?)</.+?<span.+?>.*?</.+?<span.+?>(.*?)</span>", innerTD)
                            innerTD = [list(x) for x in innerTD][0]
                            innerTD[0], innerTD[1] = innerTD[1], innerTD[0]
                            yield innerTD
                        else:
                            if re.search(r',', innerTD):
                                innerTD = innerTD[:2].upper()
                            yield [innerTD]
        else:
            print("Connection error")

    def getJson(self, text):
        d = {
            "ПН": "Понедельник",
            "ВТ": "Вторник",
            "СР": "Среда",
            "ЧТ": "Четверг",
            "ПТ": "Пятница",
            "СБ": "Суббота"
        }
        finalDict, timeArr = {}, {}
        day, time = "", ""
        pairs = []
        for result in text:
            print(result)
            if result:
                if len(result[0]) == 2:
                    if timeArr:
                        finalDict[day] = timeArr
                        timeArr[time] = pairs
                        timeArr = {}
                        pairs = []
                    day = d[result[0]]
                elif len(result) == 1:
                    if pairs:
                        timeArr[time] = pairs
                        pairs = []
                    time = result[0]
                else:
                    pairs.append(result)
            if timeArr:
                timeArr[time] = pairs
                finalDict[day] = timeArr
        return json.dumps(finalDict, indent=4, ensure_ascii=False)
