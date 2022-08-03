from api_gateway import ApiGateway
import requests


class SectionGateway(ApiGateway):

    def fetch(self, section):
        url = f'https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={self.key}'
        response = requests.get(url)
        return response.json()['results']
