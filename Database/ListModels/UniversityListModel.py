from Database.ListModels.AbstractListModel import AbstractListModel
from Database.Models.UniversityModel import UniversityModel


class UniversityListModel(AbstractListModel):

    def getList(self, model_class=UniversityModel):
        return super(UniversityListModel, self).getList(model_class)

    def getListByParams(self, params, model_class=UniversityModel):
        return super(UniversityListModel, self).getListByParams(params, model_class)
