
class MetricsController:
    """
    Simple metrics controller.
    Provides basic bot metrics.
    Metrics set is extendable.
    """

    def getMetrics(self) -> str:
        """
        Metric types is extendable. Just add new
        func which will return metrics dict.

        @return: Text message with metrics in human readable format
        """
        reply = ''

        reply += self.extractMetrics(
            self.getRowCountMetrics()
        )

        return reply

    def getRowCountMetrics(self) -> dict:
        """
        @todo: create get count metods in list models
        @todo: create userMessagesListModel

        @return: Dict of count metrics
        """
        return {
            'total_users': 1,
            'total_messages': 2,
            'total_groups': 3,
        }

    def extractMetrics(self, metrics):
        text = ''

        for metric in metrics:
            text += f'*{metric}*: {str(metrics[metric])}\n'

        return text
