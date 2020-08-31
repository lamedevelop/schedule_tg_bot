import json

import re
import requests

from ParseController import ParseController


class BaumanParseController(ParseController):


    #url = 'https://students.bmstu.ru/schedule/201c396c-8610-11ea-959d-005056960017'
    url = 'https://students.bmstu.ru/schedule/d2e34cf6-4aee-11e9-b081-005056960017'


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
        try:
            page = requests.get(link)
        except:
            print("Connection error")
            return

        d = {
            "div": r'<div class=\"col-md-6 hidden-xs\">(.+?)</div>',
            "tr": r'<tr(.+?)</tr>',
            "td": r'<td(.+?)</td>',
            "day": r'<strong>(.+?)</strong>',
            "time": r'class=\"bg-grey text-nowrap\">(.+?)$',
            "doublepair": r'colspan=\"2\">(.*?)$',
            "singlepair": r'class=\".+?\">(.+?)$',
            "toArray": r'<i>(.*?)</i> <span>(.*?)</span> <i>(.*?)</i> <i>(.*?)</i>'
        }

        for div in re.findall(d["div"], page.text.replace("\n", "")):
            stageInTR = 1
            for tr in re.findall(d["tr"], div):
                stageInTD = 1
                for td in re.findall(d["td"], tr):
                    value = []
                    if stageInTR == 1:
                        value = re.findall(d["day"], td)  # День недели
                    elif stageInTR > 2:
                        if stageInTD == 1:
                            value = re.findall(d["time"], td)  # Время пары
                        else:
                            value = re.findall(d["doublepair"], td)  # Сдвоенная
                            if not value:
                                value = re.findall(d["singlepair"], td)  # Пара
                            value = re.findall(d["toArray"], str(value))  # [array]
                            if not value:
                                value = ['', '', '', '']  # Если ячейка пустая
                                #value = []  # Если ячейка пустая
                            else:
                                value = [list(x) for x in value][0]
                        stageInTD += 1
                    yield value
                stageInTR += 1


    def getJson(self, webpage):
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
        for result in webpage:
            if result:
                if len(result[0]) == 2:
                    if timeArr:
                        finalDict[day] = timeArr
                        timeArr = {}
                    day = d[result[0]]
                elif len(result) == 1:
                    if pairs:
                        timeArr[time] = pairs
                        pairs = []
                    time = result[0]
                else:
                    pairs.append(
                        list(map(lambda x: x.replace("&#160;", " "), result)))
        return json.dumps(finalDict, indent=4, ensure_ascii=False)

