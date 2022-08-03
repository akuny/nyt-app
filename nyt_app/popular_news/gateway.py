from api_gateway import ApiGateway
import requests


class PopularNewsGateway(ApiGateway):

    def fetch(self, interval):
        url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/{self.parse_interval(interval)}.json?api-key={self.key}'
        response = requests.get(url)
        return response.json()['results']

    def parse_interval(self, interval):
        if interval == 'day':
            return 1
        elif interval == 'week':
            return 7
        elif interval == 'month':
            return 30
        else:
            return 1
