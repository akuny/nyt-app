from application_context.application_context import ApplicationContext


class GetTopNews:

    def __init__(self, app_context: ApplicationContext):
        self.app_context = app_context

    def fetch_news(self, day):
        gateway = self.app_context.get_top_news_gateway()
        presenter = self.app_context.get_top_news_presenter()

        contents = gateway.fetch(day)
        presenter.show(contents)
