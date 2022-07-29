class DaysHeadlinesPresenter:

    def __init__(self, news_list):
        self.news_list = news_list

    def show(self):
        for doc in self.news_list.contents:
            print('')
            print(doc['headline']['main'])
            print(doc['web_url'])
            print('')
