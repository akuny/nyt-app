from abc import ABC, abstractmethod


class ApplicationContext(ABC):

    @abstractmethod
    def get_top_news_gateway():
        pass

    @abstractmethod
    def get_top_news_presenter():
        pass

    @abstractmethod
    def get_days_headlines_gateway():
        pass

    @abstractmethod
    def get_days_headlines_presenter():
        pass
