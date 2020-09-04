from MpeiParseController import MpeiParseController
from BmstuParseController import BmstuParseController
import time

#url1 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"
#url2 = "https://mpei.ru/Education/timetable/Pages/table.aspx?groupoid=10342&start=2020.08.31"


def main(obj):
    start = time.time()
    obj.run("result")
    end = time.time()
    total = (end - start)
    print("finished in: %f sec" % total)


if __name__ == '__main__':
    # main(BmstuParseController())
    main(MpeiParseController('А-06м-20', '2020.08.31'))
