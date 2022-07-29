from .application_context import ApplicationContext
from .prod import ProdContext
from .test import TestContext


class ApplicationContextFactory:

    @staticmethod
    def make(type) -> ApplicationContext:
        if type == "prod":
            return ProdContext()
        if type == "test":
            return TestContext()
