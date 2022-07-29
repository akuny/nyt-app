from application_context.application_context import ApplicationContext


class GetDaysHeadlines:

    def __init__(self, app_context: ApplicationContext):
        self.app_context = app_context

    def fetch_headlines(self, day):
        gateway = self.app_context.get_days_headlines_gateway()
        presenter = self.app_context.get_days_headlines_presenter()

        contents = gateway.fetch(day)
        presenter.show(contents)
