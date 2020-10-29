import re
from datetime import datetime, timedelta

from Controllers.Parse.ParseController import ParseController
from Controllers.Log.LogController import LogController


class MpeiParseController(ParseController):

    logger = LogController()

    def _parse(self, group_name: str):

        day = {x: {'both': ['']} for x in [
            '09:20-10:55', '11:10-12:45', '13:45-15:20', '15:35-17:10', '17:20-18:55'
        ]}

        week = {x: day.copy() for x in [
            'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'
        ]}

        days_name = {
            'Пн': 'Понедельник',
            'Вт': 'Вторник',
            'Ср': 'Среда',
            'Чт': 'Четверг',
            'Пт': 'Пятница',
            'Сб': 'Суббота',
        }

        search_groupid_url = f'http://ts.mpei.ru/api/search?term={group_name}&type=group'

        search_groupid = self.getUrl(search_groupid_url)
        if search_groupid is None:
            return {}

        search_json = search_groupid.json()

        if search_json:
            group_id = search_json[0]['id']

            date = datetime.now()
            start = date + timedelta(days=-date.isoweekday())
            finish = start + timedelta(days=6)
            start = str(start)[:10].replace('-', '.')
            finish = str(finish)[:10].replace('-', '.')

            group_schedule_url = f'http://ts.mpei.ru/api/schedule/group/{group_id}start={start}&finish={finish}&lng=1'

            group_schedule = self.getUrl(group_schedule_url)
            if group_schedule is None:
                return {}

            group_schedule_json = group_schedule.json()

            for item in group_schedule_json:
                lect = item['lecturer']
                if re.match(r'!', lect) is None:
                    lect = ''

                both = {
                    'both': [
                        item['kindOfWork'],
                        item['discipline'],
                        item['auditorium'],
                        lect
                    ]
                }
                day_of_week = days_name[item['dayOfWeekString']]
                time = f"{item['beginLesson']}-{item['endLesson']}"
                week[day_of_week][time] = both

            return {group_name: week}

    def __str__(self):
        return '1'
