class TopNewsPresenter:

    def __init__(self, news_list):
        self.news_list = news_list

    def show(self):
        for article in self.news_list.contents:
            print('')
            print(article['title'])
            print(article['url'])
            print('')
