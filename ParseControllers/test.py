from MpeiParseController import MpeiParseController
from MstuParseController import MstuParseController

#url1 = "https://students.bmstu.ru/schedule/d2e34cf6-4aee-11e9-b081-005056960017"
url1 = "https://students.bmstu.ru/schedule/201c396c-8610-11ea-959d-005056960017"
#url2 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"
url2 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"

class_Mstu = MstuParseController(url1).run("Mstu")
class_Mpei = MpeiParseController(url2).run("Mpei")
