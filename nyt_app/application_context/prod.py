from .application_context import ApplicationContext
from top_news.gateway import TopNewsGateway
from top_news.presenter import TopNewsPresenter
from days_headlines.gateway import DaysHeadlinesGateway
from days_headlines.presenter import DaysHeadlinesPresenter


class ProdContext(ApplicationContext):
    def get_top_news_gateway(self):
        return TopNewsGateway()

    def get_top_news_presenter(self):
        return TopNewsPresenter()

    def get_days_headlines_gateway(self):
        return DaysHeadlinesGateway()

    def get_days_headlines_presenter(self):
        return DaysHeadlinesPresenter()
