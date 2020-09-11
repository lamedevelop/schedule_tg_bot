import requests
import re
from datetime import datetime, timedelta

from Controllers.Parse.ParseController import ParseController
from Controllers.Log.LogController import LogController


class MpeiParseController(ParseController):

    logger = LogController()

    def _parse(self, group_name: str):

        day = {
            '09:20-10:55': {'both': ['']},
            '11:10-12:45': {'both': ['']},
            '13:45-15:20': {'both': ['']},
            '15:35-17:10': {'both': ['']},
            '17:20-18:55': {'both': ['']}
        }

        week = {
            'Понедельник': day.copy(),
            'Вторник': day.copy(),
            'Среда': day.copy(),
            'Четверг': day.copy(),
            'Пятница': day.copy(),
            'Суббота': day.copy(),
        }

        days_name = {
            'Пн': 'Понедельник',
            'Вт': 'Вторник',
            'Ср': 'Среда',
            'Чт': 'Четверг',
            'Пт': 'Пятница',
            'Сб': 'Суббота',
        }

        search_groupid_url = 'http://ts.mpei.ru/api/search?term=%s&type=group' % group_name

        try:
            search_groupid = requests.get(search_groupid_url)
        except requests.ConnectionError as e:
            self.logger.alert(str(e))
            return {}

        if search_groupid.status_code == 200:
            search_json = search_groupid.json()

            if len(search_json) == 1:
                group_id = search_json[0]['id']

                date = datetime.now()
                date_start = '.'.join(str(date)[:10].split('-'))
                date_finish = '.'.join(
                    str(date+timedelta(days=6))[:10].split('-'))

                group_schedule_url = 'http://ts.mpei.ru/api/schedule/group/%dstart=%s&finish=%s&lng=1' % (
                    group_id, date_start, date_finish)

                try:
                    group_schedule = requests.get(group_schedule_url)
                except requests.ConnectionError as e:
                    self.logger.alert(str(e))
                    return {}

                if group_schedule.status_code == 200:
                    group_schedule_json = group_schedule.json()

                    for item in group_schedule_json:
                        lecturer = item['lecturer']

                        both = {'both': [
                            item['kindOfWork'],
                            item['discipline'],
                            item['auditorium'],
                            lecturer if re.match(
                                r'!', lecturer) is None else ''
                        ]}
                        day_of_week = days_name[item['dayOfWeekString']]
                        time = '%s-%s' % (
                            item['beginLesson'],
                            item['endLesson']
                        )
                        week[day_of_week][time] = both

                    return {group_name: week}
        return {}

    def __str__(self):
        return '1'
