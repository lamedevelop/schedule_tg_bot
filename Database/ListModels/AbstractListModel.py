from Controllers.SqlLiteDbController import SqlLiteDbController


class AbstractListModel:

    def getList(self, model_class):
        records = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name}'''
        )

        return self.getModelsList(records, model_class)

    def getListByParams(self, params, model_class):
        query_params = []
        for key in params:
            query_params.append(key + '="' + str(params[key]) + '"')

        records = SqlLiteDbController().fetchQuery(
            f'''SELECT {", ".join(model_class.fields.keys())} 
                FROM {model_class.table_name} 
                WHERE ''' + ' AND '.join(query_params)
        )

        return self.getModelsList(records, model_class)

    def getModelsList(self, records, model_class):
        models = []

        for record in records:
            record_dict = {
                key: record[index]
                for index, key in enumerate(model_class.fields)
            }

            models.append(model_class(record_dict))

        return models

    def count(self, model_class):
        return SqlLiteDbController().fetchQuery(
            f'''SELECT COUNT({model_class.primary_key[0]})
                FROM {model_class.table_name};'''
        )[0][0]
