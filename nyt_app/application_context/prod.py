from .application_context import ApplicationContext
from popular_news.gateway import PopularNewsGateway
from popular_news.presenter import PopularNewsPresenter
from days_headlines.gateway import DaysHeadlinesGateway
from days_headlines.presenter import DaysHeadlinesPresenter
from section.gateway import SectionGateway
from section.presenter import SectionPresenter

class ProdContext(ApplicationContext):
    def get_popular_news_gateway(self):
        return PopularNewsGateway()

    def get_popular_news_presenter(self):
        return PopularNewsPresenter()

    def get_days_headlines_gateway(self):
        return DaysHeadlinesGateway()

    def get_days_headlines_presenter(self):
        return DaysHeadlinesPresenter()

    def get_section_gateway(self):
        return SectionGateway()

    def get_section_presenter(self):
        return SectionPresenter()
