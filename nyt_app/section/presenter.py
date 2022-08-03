class SectionPresenter:

    def show(self, news_list):
        for article in news_list:
            print('')
            print(article['title'])
            print(article['url'])
            print('')
