from .gateway import TopNewsGateway


class TopNewsList:

    def __init__(self, gateway: TopNewsGateway):
        self.gateway = gateway

    def fetch_news(self, interval):
        self.contents = self.gateway.fetch(interval)
