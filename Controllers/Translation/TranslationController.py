import Controllers.Translation.MessagesTranslation.ru as ru
import Controllers.Translation.MessagesTranslation.en as en


class TranslationController:

    ENTER_UNIVERSITY = 1
    FIRST_ENTER_GROUP = 2
    CHANGE_GROUP = 3
    SCHEDULE_WAS_FOUND = 4
    SCHEDULE_DOWNLOADED = 5
    SCHEDULE_WAS_NOT_FOUND = 6
    HELP = 7
    WEEK_DAYS = 8
    WEEK_DAYS_SHORT = 9

    messages = {
        'ru': {
            ENTER_UNIVERSITY:       ru.ENTER_UNIVERSITY,
            FIRST_ENTER_GROUP:      ru.FIRST_ENTER_GROUP,
            CHANGE_GROUP:           ru.CHANGE_GROUP,
            SCHEDULE_WAS_FOUND:     ru.SCHEDULE_WAS_FOUND,
            SCHEDULE_DOWNLOADED:    ru.SCHEDULE_DOWNLOADED,
            SCHEDULE_WAS_NOT_FOUND: ru.SCHEDULE_WAS_NOT_FOUND,
            HELP:                   ru.HELP,
            WEEK_DAYS:              ru.WEEK_DAYS,
            WEEK_DAYS_SHORT:        ru.WEEK_DAYS_SHORT,
        },

        'en': {
            ENTER_UNIVERSITY:       en.ENTER_UNIVERSITY,
            FIRST_ENTER_GROUP:      en.FIRST_ENTER_GROUP,
            CHANGE_GROUP:           en.CHANGE_GROUP,
            SCHEDULE_WAS_FOUND:     en.SCHEDULE_WAS_FOUND,
            SCHEDULE_DOWNLOADED:    en.SCHEDULE_DOWNLOADED,
            SCHEDULE_WAS_NOT_FOUND: en.SCHEDULE_WAS_NOT_FOUND,
            HELP:                   en.HELP,
            WEEK_DAYS:              en.WEEK_DAYS,
            WEEK_DAYS_SHORT:        en.WEEK_DAYS_SHORT,
        }
    }

    def getMessage(self, language, index):
        # currently we not sure if english language code is en
        # and we can't expect this right now, so we left this here
        # todo: fix language tags
        if language != 'ru':
            language = 'en'
        return self.messages[language][index]
