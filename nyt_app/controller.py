from top_news.get_top_news import GetTopNews
from days_headlines.get_days_headlines import GetDaysHeadlines


class Controller:

    @staticmethod
    def top(app_context, interval):
        top_news = GetTopNews(app_context)
        top_news.fetch_news(interval)

    @staticmethod
    def day(app_context, day):
        todays_headlines = GetDaysHeadlines(app_context)
        todays_headlines.fetch_headlines(day)
