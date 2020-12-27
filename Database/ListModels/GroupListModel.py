from Database.ListModels.AbstractListModel import AbstractListModel
from Database.Models.GroupModel import GroupModel


class GroupListModel(AbstractListModel):

    def getList(self, model_class=GroupModel):
        return super(GroupListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=GroupModel):
        groups = []
        records = super(GroupListModel, self).getListByParams(params, model_class)

        for record in records:
            groups.append(GroupModel({
                'group_id': record[0],
                'group_name': record[1],
                'university_id': record[2],
                'schedule_text': record[3],
                'schedule_url': record[4],
                'update_date': record[5]
            }))

        return groups
