import psutil

from Database.ListModels.GroupListModel import GroupListModel
from Database.ListModels.UserMessageListModel import UserMessageListModel
from Database.ListModels.TelegramUserListModel import TelegramUserListModel


class MetricsController:
    """
    Simple metrics controller.
    Provides basic bot metrics.
    Metrics set is extendable.
    """

    delimeter = 1024 ** 3

    def getMetrics(self) -> str:
        """
        Metric types is extendable. Just add new
        func which will return metrics dict.

        @return: Text message with metrics in human readable format
        """
        reply = '---\n'

        reply += self.extractMetrics(
            self.getRowCountMetrics()
        )

        reply += '---\n'

        reply += self.extractMetrics(
            self.getServerStatusMetrics()
        )

        reply += '---'

        return reply

    def getRowCountMetrics(self) -> dict:
        """
        @return: Dict of count metrics
        """
        return {
            'total_users': TelegramUserListModel().count(),
            'total_messages': UserMessageListModel().count(),
            'total_groups': GroupListModel().count(),
        }

    def getServerStatusMetrics(self):
        return {
            'load_avg': psutil.getloadavg(),
            'cpu_usage (%)': psutil.cpu_percent(),
            'ram_usage (%)': psutil.virtual_memory().percent,
            'disk_usage (%)': psutil.disk_usage('/').percent,
            'disk_used (Gb)': psutil.disk_usage('/').used / self.delimeter,
            'disk_total (Gb)': psutil.disk_usage('/').total / self.delimeter,
        }

    def extractMetrics(self, metrics):
        text = ''

        for metric in metrics:
            text += f'*{metric}*: {str(metrics[metric])}\n'

        return text
