from Database.ListModels.AbstractListModel import AbstractListModel
from Database.Models.GroupModel import GroupModel

from Controllers.Db.SqlLiteDbController import SqlLiteDbController
from Controllers.Date.DateTimeController import DateTimeController


class GroupListModel(AbstractListModel):

    def getList(self, model_class=GroupModel):
        return super(GroupListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=GroupModel):
        records = super(GroupListModel, self).getListByParams(
            params, model_class)
        return self._GroupModelList(records)

    def getListByDate(self, days_ago=7, model_class=GroupModel):

        time_deadline = DateTimeController.getDateDifference(days_ago)

        records = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())}
                FROM groups
                WHERE update_date<{time_deadline}'''
        )

        return self._GroupModelList(records)

    def _GroupModelList(records: list) -> list:
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
