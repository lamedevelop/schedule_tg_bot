from Database.ListModels.AbstractListModel import AbstractListModel
from Database.Models.TelegramUserModel import TelegramUserModel


class TelegramUserListModel(AbstractListModel):

    def getList(self, model_class=TelegramUserModel):
        return super(TelegramUserListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=TelegramUserModel):
        return super(TelegramUserListModel, self).getListByParams(params, model_class)
