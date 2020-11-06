from Database.Models.DbModel import DbModel


class TelegramUserModel(DbModel):

    table_name = 'telegramUsers'

    primary_key = ['user_id']

    fields = {
        primary_key[0]: '',
        'chat_id': '',
        'first_name': '',
        'last_name': '',
        'username': '',
        'language_code': '',
        'is_bot': '',
        'is_alive': '',
        'registration_date': '',
        'university_id': '',
        'group_id': ''
    }

    def get(self, primary_key):
        return super(TelegramUserModel, self).get(primary_key)

    def set(self):
        super(TelegramUserModel, self).set()

    def update(self, new_fields):
        super(TelegramUserModel, self).update(new_fields)
