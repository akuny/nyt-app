from .application_context import ApplicationContext
from popular_news.gateway_mock import MockPopularNewsGateway
from popular_news.presenter_mock import MockPopularNewsPresenter
from days_headlines.gateway_mock import MockDaysHeadlinesGateway
from days_headlines.presenter_mock import MockDaysHeadlinesPresenter


class TestContext(ApplicationContext):
    def get_popular_news_gateway(self):
        return MockPopularNewsGateway()

    def get_popular_news_presenter(self):
        return MockPopularNewsPresenter()

    def get_days_headlines_gateway(self):
        return MockDaysHeadlinesGateway()

    def get_days_headlines_presenter(self):
        return MockDaysHeadlinesPresenter()
