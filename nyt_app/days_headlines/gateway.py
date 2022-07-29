from api_gateway import ApiGateway
import requests


class DaysHeadlinesGateway(ApiGateway):

    def fetch(self, day):
        url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?facet_field=day_of_week&facet=true&begin_date={day}&end_date={day}&api-key={self.key}'
        response = requests.get(url)
        return response.json()['response']['docs']
