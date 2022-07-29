from top_news.gateway import TopNewsGateway
from top_news.list import TopNewsList
from top_news.presenter import TopNewsPresenter
from days_headlines.gateway import DaysHeadlinesGateway
from days_headlines.list import DaysHeadlinesList
from days_headlines.presenter import DaysHeadlinesPresenter


class Controller:

    @staticmethod
    def top(interval):
        gateway = TopNewsGateway()
        top_news = TopNewsList(gateway)
        top_news.fetch_news(interval)
        presenter = TopNewsPresenter(top_news)
        presenter.show()

    @staticmethod
    def day(day):
        gateway = DaysHeadlinesGateway()
        todays_headlines = DaysHeadlinesList(gateway)
        todays_headlines.fetch_headlines(day)
        presenter = DaysHeadlinesPresenter(todays_headlines)
        presenter.show()
