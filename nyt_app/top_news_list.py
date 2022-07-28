from top_news_gateway import TopNewsGateway


class TopNewsList:

    def __init__(self, news_gateway: TopNewsGateway):
        self.news_gateway = news_gateway

    def fetch_news(self, interval):
        self.contents = self.news_gateway.fetch(self.parse_interval(interval))

    def parse_interval(self, interval):
        if interval == 'day':
            return 1
        elif interval == 'week':
            return 7
        elif interval == 'month':
            return 30
        else:
            return 1
