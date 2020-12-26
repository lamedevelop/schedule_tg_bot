from Controllers.Db.SqlLiteDbController import SqlLiteDbController
from Database.Models.AbstractModel import AbstractModel


class TelegramUserModel(AbstractModel):

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

    def getByChatId(self, chat_id):
        fields = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(TelegramUserModel.fields.keys())} 
                FROM {TelegramUserModel.table_name} 
                WHERE chat_id={chat_id}'''
        )

        if len(fields) > 0 and len(fields[0]) == len(self.fields):
            for field in enumerate(self.fields):
                self.fields[field[1]] = fields[0][field[0]]

        return self

    def set(self):
        super(TelegramUserModel, self).set()

    def update(self, new_fields):
        super(TelegramUserModel, self).update(new_fields)
