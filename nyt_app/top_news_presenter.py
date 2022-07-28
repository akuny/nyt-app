import math
from top_news_list import TopNewsList


class TopNewsPresenter:

    def __init__(self, top_news_list: TopNewsList):
        self.top_news_list = top_news_list

    def show(self):
        for article in self.top_news_list.contents:
            print('')
            print(article['title'])
            print(article['url'])
            print('')
