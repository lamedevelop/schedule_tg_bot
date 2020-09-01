from ParseController import (ParseController, re, requests)


class MstuParseController(ParseController):

    def _parse(self, url):
        page = requests.get(url)
        if page.status_code == 200:
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
                                value = re.findall(
                                    d["doublepair"], td)  # Сдвоенная
                                if not value:
                                    value = re.findall(
                                        d["singlepair"], td)  # Пара
                                value = re.findall(
                                    d["toArray"], str(value))  # [array]
                                if not value:
                                    # Если ячейка пустая
                                    value = ['', '', '', '']
                                    # value = []  # Если ячейка пустая
                                else:
                                    value = [list(x) for x in value][0]
                            stageInTD += 1
                        yield value
                    stageInTR += 1
        else:
            print("Connection error")
