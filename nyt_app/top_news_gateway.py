from decouple import config
import requests


class TopNewsGateway:

    @staticmethod
    def fetch(interval):
        key = config('API_KEY')
        url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/{interval}.json?api-key={key}'
        response = requests.get(url)
        return response.json()['results']
