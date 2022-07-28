from top_news_list import TopNewsList
from top_news_presenter import TopNewsPresenter
from top_news_gateway import TopNewsGateway


class Controller:

    @staticmethod
    def top(interval):
        gateway = TopNewsGateway
        top_news = TopNewsList(gateway)
        top_news.fetch_news(interval)
        presenter = TopNewsPresenter(top_news)
        presenter.show()
