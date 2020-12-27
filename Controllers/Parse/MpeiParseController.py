import re
from datetime import datetime, timedelta

from Controllers.Parse.ParseController import ParseController
from Controllers.Log.LogController import LogController


class MpeiParseController(ParseController):

    logger = LogController()

    days = {
        'Пн': 'Понедельник',
        'Вт': 'Вторник',
        'Ср': 'Среда',
        'Чт': 'Четверг',
        'Пт': 'Пятница',
        'Сб': 'Суббота',
    }

    get_group_url_pattern = f'http://ts.mpei.ru/api/search?term=%s&type=group'
    get_schedule_url_pattern = f'http://ts.mpei.ru/api/schedule/group/%s?start=%s&finish=%s&lng=1'

    def _parse(self, group_name: str):
        week = self.getDefaultWeek()

        group_id = self._getUrl(self.get_group_url_pattern % group_name)
        if group_id is None:
            return {}

        search_json = group_id.json()

        if search_json:
            group_id = search_json[0]['id']

            date = datetime.now()
            start = date + timedelta(days=-date.isoweekday())
            finish = start + timedelta(days=6)

            group_schedule = self._getUrl(
                self.get_schedule_url_pattern % (
                    group_id,
                    start.strftime("%y.%m.%d"),
                    finish.strftime("%y.%m.%d")
                )
            )

            if group_schedule is None:
                return {}

            group_schedule_json = group_schedule.json()
            
            for item in group_schedule_json:
                lect = item['lecturer']
                if re.match(r'!', lect) is not None:
                    lect = ''

                both = {
                    'both': [
                        item['kindOfWork'],
                        item['discipline'],
                        item['auditorium'],
                        lect
                    ]
                }
                day_of_week = self.days[item['dayOfWeekString']]
                time = f"{item['beginLesson']}-{item['endLesson']}"
                week[day_of_week][time] = both

            return {group_name: week}

    @staticmethod
    def getDefaultWeek():
        day = {x: {'both': ['']} for x in [
            '09:20-10:55', '11:10-12:45', '13:45-15:20', '15:35-17:10', '17:20-18:55'
        ]}

        return {x: day.copy() for x in [
            'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'
        ]}

    def __str__(self):
        return '1'
