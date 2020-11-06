from Database.Models.DbModel import DbModel


class UserMessageModel(DbModel):

    table_name = 'userMessages'

    primary_key = ['message_id']

    fields = {
        primary_key[0]: '',
        'user_id': '',
        'user_status': '',
        'message': '',
        'creation_date': ''
    }

    def get(self, primary_key):
        return super(UserMessageModel, self).get(primary_key)

    def set(self):
        super(UserMessageModel, self).set()

    def update(self, new_fields):
        super(UserMessageModel, self).update(new_fields)
