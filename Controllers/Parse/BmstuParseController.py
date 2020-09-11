import re
import requests
from bs4 import BeautifulSoup  # https://pypi.org/project/beautifulsoup4/

from Controllers.Parse.ParseController import ParseController
from Controllers.Log.LogController import LogController


class BmstuParseController(ParseController):

    logger = LogController()
    SCHEDULE_LIST_URL = 'https://students.bmstu.ru/schedule/list'

    def _parse(self, group_name: str):

        try:
            get_list = requests.get(self.SCHEDULE_LIST_URL)
        except requests.ConnectionError as e:
            logger.alert(e)
            return {}

        if get_list.status_code == 200:
            html_list = get_list.text.replace('\n', '')
            soup_list = BeautifulSoup(html_list, 'html.parser')
            a_tags = soup_list.find_all(
                'a', class_='btn btn-sm btn-default text-nowrap')
            group_schedule_dict = {}

            for i, item in enumerate(a_tags):
                if item.get_text().strip() == group_name:
                    self._parseTask(item, group_schedule_dict)
                    break
            return group_schedule_dict
        else:
            return {}

    def _parseTask(self, item, group_schedule_dict):
        group_name = item.get_text().strip()
        group_schedule_url = 'https://students.bmstu.ru/%s' % item.get('href')

        try:
            get_group_schedule = requests.get(group_schedule_url)
        except requests.ConnectionError as e:
            logger.alert(e)
            return {}

        if get_group_schedule.status_code == 200:
            week = {}
            html_group = get_group_schedule.text.replace('\n', '')
            soup_group = BeautifulSoup(html_group, 'html.parser')
            day_div = soup_group.find_all(
                'div', class_='col-md-6 hidden-sm hidden-md hidden-lg')

            for div in day_div:
                day = {}
                day_shedule = div.find('tbody')
                day_name = day_shedule.find('strong').get_text()
                time_and_subject = day_shedule.find_all('tr')

                for index, item in enumerate(time_and_subject):
                    if index > 1:
                        curr_time = item.find(
                            'td', class_='bg-grey text-nowrap').get_text()
                        time_groups = re.match(r'(.{5})(.{5})', curr_time)
                        curr_time = f'{time_groups.group(1)}-{time_groups.group(2)}'

                        both = item.find('td', colspan='2')
                        subject_patt = re.compile(
                            r'<i>(.*?)</i> <span>(.*?)</span> <i>(.*?)</i> <i>(.*?)</i>')

                        if both:
                            both_turple = subject_patt.findall(
                                str(both).replace('\xa0', ' ').replace('Самостоятельная работа', '')
                            )
                            both_schedule = [list(x) for x in both_turple][0]

                            subject = {
                                'both': both_schedule if list(
                                    filter(lambda x: bool(x), both_schedule)
                                ) else ['']
                            }
                        else:
                            numerator = item.find('td', class_='text-success')
                            denominator = item.find('td', class_='text-info')
                            numerator_turple = subject_patt.findall(
                                str(numerator).replace('\xa0', ' ')
                            )
                            denominator_turple = subject_patt.findall(
                                str(denominator).replace('\xa0', ' ')
                            )
                            subject = {
                                'numerator': [list(x) for x in numerator_turple][0] if numerator_turple else [''],
                                'denominator': [list(x) for x in denominator_turple][0] if denominator_turple else ['']
                            }

                        day[curr_time] = subject
                week[day_name] = day
            group_schedule_dict[group_name] = week
        else:
            group_schedule_dict[group_name] = {}

    def __str__(self):
        return '2'
