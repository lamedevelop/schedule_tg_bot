from ParseController import ParseController

from bs4 import BeautifulSoup  # https://pypi.org/project/beautifulsoup4/
import requests
import threading
import re


class BmstuParseController(ParseController):

    SCHEDULE_LIST_URL = 'https://students.bmstu.ru/schedule/list'
    MAX_TREADS = 30

    def _parse(self):
        get_list = requests.get(self.SCHEDULE_LIST_URL)
        if get_list.status_code == 200:
            html_list = get_list.text.replace('\n', '')
            soup_list = BeautifulSoup(html_list, 'html.parser')
            a_tags = soup_list.find_all(
                'a', class_='btn btn-sm btn-default text-nowrap')
            group_schedule_dict = {}
            active_threads = []
            for i, a in enumerate(a_tags):
                t = threading.Thread(target=self._parseTask, args=(
                    a, group_schedule_dict))
                t.start()
                active_threads.append(t)
                thread_count = threading.active_count()
                if thread_count > self.MAX_TREADS:
                    t.join()
            for t in active_threads:
                t.join()
            return group_schedule_dict
        else:
            return {}

    def _parseTask(self, item, dict):
        group_name = item.get_text().strip()
        group_schedule_url = 'https://students.bmstu.ru/%s' % item.get('href')
        get_group_schedule = requests.get(group_schedule_url)
        if get_group_schedule.status_code == 200:
            days = {}
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
                        subject = {}
                        subject_patt = re.compile(
                            r'<i>(.*?)</i> <span>(.*?)</span> <i>(.*?)</i> <i>(.*?)</i>')
                        if both:
                            both_turple = subject_patt.findall(
                                str(both).replace('\xa0', ' '))
                            subject = {'both': [list(x)
                                                for x in both_turple][0]}
                        else:
                            numerator = item.find('td', class_='text-success')
                            denominator = item.find('td', class_='text-info')
                            numerator_turple = subject_patt.findall(
                                str(numerator).replace('\xa0', ' '))
                            denominator_turple = subject_patt.findall(
                                str(denominator).replace('\xa0', ' '))
                            subject = {
                                'numerator': [list(x) for x in numerator_turple][0] if numerator_turple else [''],
                                'denominator': [list(x) for x in denominator_turple][0] if denominator_turple else ['']
                            }
                        day[curr_time] = subject
                days[day_name] = day
            dict[group_name] = days
        else:
            group_schedule_dict[group_name] = {}
