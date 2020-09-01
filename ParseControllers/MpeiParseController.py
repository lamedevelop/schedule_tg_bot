from ParseController import (ParseController, re, requests, BeautifulSoup)


class MpeiParseController(ParseController):

    def _parse(self, url):
        page = requests.get(url)
        if page.status_code == 200:
            html = page.text.replace("\n", "")
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
