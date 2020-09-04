from MpeiParseController import MpeiParseController
from MstuParseController import MstuParseController
import time

#url1 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"
#url2 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"


def main(obj):
    start = time.time()
    obj.run("Mstu")
    end = time.time()
    total = (end - start)
    print("MSTU: %f sec" % total)


if __name__ == '__main__':
    main(MstuParseController())
    # main(MpeiParseController())
