import psutil


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
        reply = ''

        reply += 'DB content metrics:\n'
        reply += self.extractMetrics(
            self.getRowCountMetrics()
        )

        reply += '\nServer status metrics:\n'
        reply += self.extractMetrics(
            self.getServerStatusMetrics()
        )

        return reply

    def getRowCountMetrics(self) -> dict:
        """
        @todo: create get count metods in list models
        @todo: create userMessagesListModel

        @return: Dict of count metrics
        """
        return {
            '1': '::::::',
            'total_users': 1,
            'total_messages': 2,
            'total_groups': 3,
        }

    def getServerStatusMetrics(self):
        return {
            '1': '::::::',
            'load_avg': psutil.getloadavg(),
            'cpu_usage (%)': psutil.cpu_percent(),
            'ram_usage (%)': psutil.virtual_memory().percent,
            '2': '::::::',
            'disk_usage (%)': psutil.disk_usage('/').percent,
            'disk_used (Gb)': psutil.disk_usage('/').used / self.delimeter,
            'disk_total (Gb)': psutil.disk_usage('/').total / self.delimeter,
            # 'disk_io_counters': psutil.disk_io_counters(perdisk=False),
            '3': '::::::',
            # 'temp': psutil.sensors_temperatures(),
            # 'fans': psutil.sensors_fans(),
            'users': psutil.users(),
        }

    def extractMetrics(self, metrics):
        text = ''

        for metric in metrics:
            text += f'*{metric}*: {str(metrics[metric])}\n'

        return text
