from command import Command
from application_context.application_context import ApplicationContext
from top_news.get_top_news import GetTopNews
from days_headlines.get_days_headlines import GetDaysHeadlines


class CommandBus:

    @staticmethod
    def handle(app_context: ApplicationContext, command: Command):
        if command.is_valid == False:
            return

        if command.type == 'top':
            top_news = GetTopNews(app_context)
            top_news.fetch_news(command.detail)

        if command.type == 'day':
            todays_headlines = GetDaysHeadlines(app_context)
            todays_headlines.fetch_headlines(command.detail)
