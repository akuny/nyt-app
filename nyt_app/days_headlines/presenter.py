class DaysHeadlinesPresenter:

    def show(self, news_list):
        for doc in news_list:
            print('')
            print(doc['headline']['main'])
            print(doc['web_url'])
            print('')
