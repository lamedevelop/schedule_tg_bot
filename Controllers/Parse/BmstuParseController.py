import re

from bs4 import BeautifulSoup

from Controllers.Parse.AbstractParseController import AbstractParseController


class BmstuAbstractParseController(AbstractParseController):

    university_name = 'МГТУ'

    _MAIN_URL = 'https://students.bmstu.ru'
    _SCHEDULE_LIST_URL = f'{_MAIN_URL}/schedule/list'
    _GROUP_SCHEDULE_URL = f'{_MAIN_URL}/%s'

    _re_lesson = re.compile(
        r'<i>(?P<lesson_type>.*?)</i> ' +
        r'<span>(?P<lesson_name>.*?)</span> ' +
        r'<i>(?P<study_room>.*?)</i> ' +
        r'<i>(?P<teacher>.*?)</i>'
    )

    def _parse(self, group_name: str):

        schedule_list_resp = self._get_url_response(self._SCHEDULE_LIST_URL)
        if schedule_list_resp is None:
            return {}

        html = schedule_list_resp.text.replace('\n', '')
        soup = BeautifulSoup(html, 'html.parser')
        a_tags = soup.find_all(
            'a', class_='btn btn-primary text-nowrap')

        for a_tag in a_tags:
            if a_tag.get_text().strip() == group_name:
                return self._get_group_schedule(a_tag, group_name)

        return {}

    def _get_group_schedule(self, a_tag, group_name):

        group_schedule = {}
        week_schedule = {}

        group_schedule_url = self._GROUP_SCHEDULE_URL % a_tag.get('href')
        group_schedule_response = self._get_url_response(group_schedule_url)
        if group_schedule_response is None:
            return {}

        html = group_schedule_response.text.replace('\n', '')
        soup = BeautifulSoup(html, 'html.parser')
        days_div = soup.find_all(
            'div', class_='col-md-6 hidden-sm hidden-md hidden-lg')

        for day_div in days_div:
            day_shedule = {}
            day_shedule_data = day_div.find('tbody')
            day_name = day_shedule_data.find('strong').get_text()
            _, _, *lessons_schedule = day_shedule_data.find_all('tr')

            for lesson_schedule in lessons_schedule:
                lesson_time = lesson_schedule.find(
                    'td', class_='bg-grey text-nowrap').get_text()
                formated_lesson_time = f'{lesson_time[:5]}-{lesson_time[5:]}'

                unchanging_lesson = lesson_schedule.find('td', colspan='2')

                if unchanging_lesson:
                    lesson_params = self._re_lesson.findall(
                        str(unchanging_lesson)
                        .replace('\xa0', ' ')
                        .replace('Самостоятельная работа', '')
                    )

                    prms = lesson_params[0]
                    lesson = {
                        'both': prms if tuple(filter(bool, prms)) else ['']
                    }
                else:
                    numerator = a_tag.find('td', class_='text-success')
                    denominator = a_tag.find('td', class_='text-info')
                    num_params = self._re_lesson.findall(
                        str(numerator).replace('\xa0', ' ')
                    )
                    den_params = self._re_lesson.findall(
                        str(denominator).replace('\xa0', ' ')
                    )
                    lesson = {
                        'numerator': num_params[0] if num_params else [''],
                        'denominator': den_params[0] if den_params else ['']
                    }

                day_shedule[formated_lesson_time] = lesson
            week_schedule[day_name] = day_shedule
        group_schedule[group_name] = week_schedule
        return group_schedule
