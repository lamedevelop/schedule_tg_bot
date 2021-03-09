from Database.Models.GroupModel import GroupModel
from Controllers.DateTimeController import DateTimeController
from Database.ListModels.AbstractListModel import AbstractListModel


class GroupListModel(AbstractListModel):

    def getList(self, model_class=GroupModel):
        return super(GroupListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=GroupModel):
        records = super(GroupListModel, self).getListByParams(params, model_class)
        return self.getModelsList(records)

    def getListByDate(self, days_ago=1):

        time_deadline = DateTimeController.getPastTimestamp(days_ago)

        records = self.dbController.fetchQuery(
            f'''SELECT {", ".join(GroupModel.fields.keys())}
                FROM groups
                WHERE update_date<{time_deadline}'''
        )

        return self.getModelsList(records)

    @staticmethod
    def getModelsList(records: list) -> list:
        return [
            GroupModel({
                'group_id': record[0],
                'group_name': record[1],
                'university_id': record[2],
                'schedule_text': record[3],
                'schedule_url': record[4],
                'update_date': record[5]
            }) for record in records
        ]
