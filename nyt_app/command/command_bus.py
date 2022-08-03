from .command import Command
from application_context.application_context import ApplicationContext
from popular_news.get_popular_news import GetPopularNews
from days_headlines.get_days_headlines import GetDaysHeadlines
from section.get_section_news import GetSection

class CommandBus:

    @staticmethod
    def handle(app_context: ApplicationContext, command: Command):
        if command.is_valid == False:
            return

        if command.type == 'popular':
            top_news = GetPopularNews(app_context)
            top_news.fetch_news(command.detail)

        if command.type == 'day':
            todays_headlines = GetDaysHeadlines(app_context)
            todays_headlines.fetch_headlines(command.detail)

        if command.type == 'section':
            todays_headlines = GetSection(app_context)
            todays_headlines.fetch_section(command.detail)
