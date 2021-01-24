from Controllers.Db.PostgreDbController import PostgreDbController


class AbstractListModel:

    def getList(self, model_class):
        models = []

        records = PostgreDbController().fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name}'''
        )

        for record in records:
            record_dict = {
                key: record[index]
                for index, key in enumerate(model_class.fields)
            }

            models.append(model_class(record_dict))

        return models

    def getListByParams(self, params, model_class):
        query_params = []
        for key in params:
            query_params.append(key + "='" + str(params[key]) + "'")

        fields = PostgreDbController().fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name} 
                WHERE ''' + ' AND '.join(query_params)
        )

        return fields
