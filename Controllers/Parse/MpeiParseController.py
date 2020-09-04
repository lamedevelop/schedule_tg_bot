from Controllers.Parse.ParseController import ParseController

import requests
import json


class MpeiParseController(ParseController):

    def __init__(self, group_name: str, date: str):
        self.group_name = group_name
        self.date = date

    def _parse(self):

        day = {
            '09:20-10:55': {'both': ['']}, '11:10-12:45': {'both': ['']},
            '13:45-15:20': {'both': ['']}, '15:35-17:10': {'both': ['']},
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

        search_groupid_url = 'http://ts.mpei.ru/api/search?term=%s&type=group' % self.group_name
        search_groupid = requests.get(search_groupid_url)
        if search_groupid.status_code == 200:
            search_json = search_groupid.json()
            if len(search_json) == 1:
                group_id = search_json[0]['id']
                group_schedule_url = 'http://ts.mpei.ru/api/schedule/group/%d?start=%s&lng=1' % (
                    group_id, self.date)
                group_schedule = requests.get(group_schedule_url)
                if group_schedule.status_code == 200:
                    group_schedule_json = group_schedule.json()
                    for item in group_schedule_json:
                        both = {'both': [
                            item['kindOfWork'], item['discipline'], item['auditorium'], item['lecturer']]}
                        day_of_week = days_name[item['dayOfWeekString']]
                        time = '%s-%s' % (item['beginLesson'],
                                          item['endLesson'])
                        week[day_of_week][time] = both
                    return {self.group_name: week}
        return {}
