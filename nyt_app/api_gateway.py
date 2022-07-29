from decouple import config


class ApiGateway:
    def __init__(self):
        self.key = config('API_KEY')
