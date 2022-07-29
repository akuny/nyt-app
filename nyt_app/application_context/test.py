from .application_context import ApplicationContext
from top_news.gateway_mock import MockTopNewsGateway
from top_news.presenter_mock import MockTopNewsPresenter
from days_headlines.gateway_mock import MockDaysHeadlinesGateway
from days_headlines.presenter_mock import MockDaysHeadlinesPresenter


class TestContext(ApplicationContext):
    def get_top_news_gateway(self):
        return MockTopNewsGateway()

    def get_top_news_presenter(self):
        return MockTopNewsPresenter()

    def get_days_headlines_gateway(self):
        return MockDaysHeadlinesGateway()

    def get_days_headlines_presenter(self):
        return MockDaysHeadlinesPresenter()
