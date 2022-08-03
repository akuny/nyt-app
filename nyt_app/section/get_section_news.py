from application_context.application_context import ApplicationContext


class GetSection:

    def __init__(self, app_context: ApplicationContext):
        self.app_context = app_context

    def fetch_section(self, day):
        gateway = self.app_context.get_section_gateway()
        presenter = self.app_context.get_section_presenter()

        contents = gateway.fetch(day)
        presenter.show(contents)
