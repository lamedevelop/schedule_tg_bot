import Controllers.Translation.MessagesTranslation.ru as ru
import Controllers.Translation.MessagesTranslation.en as en


class TranslationController:

    ENTER_UNIVERSITY = 1
    FIRST_ENTER_GROUP = 2
    CHANGE_GROUP = 3
    SCHEDULE_WAS_FOUND = 4
    SCHEDULE_DOWNLOADED = 5
    SCHEDULE_WAS_NOT_FOUND = 6
    UNDEFINED_MESSAGE = 7
    HELP = 8
    ADMIN_HELP = 9
    WEEK_DAYS = 10
    WEEK_DAYS_SHORT = 11

    messages = {
        'ru': {
            ENTER_UNIVERSITY:       ru.ENTER_UNIVERSITY,
            FIRST_ENTER_GROUP:      ru.FIRST_ENTER_GROUP,
            CHANGE_GROUP:           ru.CHANGE_GROUP,
            SCHEDULE_WAS_FOUND:     ru.SCHEDULE_WAS_FOUND,
            SCHEDULE_DOWNLOADED:    ru.SCHEDULE_DOWNLOADED,
            SCHEDULE_WAS_NOT_FOUND: ru.SCHEDULE_WAS_NOT_FOUND,
            UNDEFINED_MESSAGE:      ru.UNDEFINED_MESSAGE,
            HELP:                   ru.HELP,
            ADMIN_HELP:             en.ADMIN_HELP,
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
            UNDEFINED_MESSAGE:      en.UNDEFINED_MESSAGE,
            HELP:                   en.HELP,
            ADMIN_HELP:             en.ADMIN_HELP,
            WEEK_DAYS:              en.WEEK_DAYS,
            WEEK_DAYS_SHORT:        en.WEEK_DAYS_SHORT,
        }
    }

    def getMessage(self, language: str, index: int) -> str or list:
        """Get message to reply in correct language.

        @param language User language.
        @param index Reply message id.

        @todo fix language tags
        """

        if language != 'ru':
            language = 'en'
        return self.messages[language][index]
