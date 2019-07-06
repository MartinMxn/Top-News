import new_pipeline.scrapers.cnn_news_scraper as scraper


EXPECTED_STRING = "Santiago is charged with using and carrying a firearm during and in relation to a crime of violence"
CNN_NEWS_URL = "http://edition.cnn.com/2017/01/17/us/fort-lauderdale-shooter-isis-claim/index.html"


def test_basic():
    news = scraper.extract_news(CNN_NEWS_URL)

    assert EXPECTED_STRING in news
    print('test passed')


if __name__ == '__main__':
    test_basic()