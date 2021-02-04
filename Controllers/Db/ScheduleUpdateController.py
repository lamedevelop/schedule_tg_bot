from ParseManager import ParseManager
from Database.Models.GroupModel import GroupModel
from Database.ListModels.GroupListModel import GroupListModel


class ScheduleUpdateController:

    @staticmethod
    def updateGroups() -> None:
        groups = GroupListModel().getListByDate()
        for group in groups:
            ScheduleUpdateController.updateGroup(group)

    @staticmethod
    def updateGroupByName(group_name) -> None:
        groups = GroupListModel().getListByParams({'group_name': group_name})
        for group in groups:
            if group.fields['group_name'] == group_name:
                ScheduleUpdateController.updateGroup(group)

    @staticmethod
    def updateGroup(group: GroupModel) -> None:
        new_schedule = ParseManager().downloadSchedule(
            group.fields['university_id'],
            group.fields['group_name']
        )
        group.update({
            'schedule_text': new_schedule,
        })


