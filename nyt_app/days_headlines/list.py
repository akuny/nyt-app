from .gateway import DaysHeadlinesGateway


class DaysHeadlinesList:

    def __init__(self, gateway: DaysHeadlinesGateway):
        self.gateway = gateway

    def fetch_headlines(self, day):
        self.contents = self.gateway.fetch(day)
