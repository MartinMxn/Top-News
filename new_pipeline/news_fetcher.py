import os
import sys

# import common package in parent directory
import new_pipeline.scrapers.cnn_news_scraper as cnn_news_scraper
from common.cloudAMQP_client import CloudAMQPClient


DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://klldxxwk:2E8PIJFgugNBF6WwLmXyxRin4jDcDkzt@spider.rmq.cloudamqp.com/klldxxwk"
DEDUPE_NEWS_TASK_QUEUE_NAME = "dedupe-news-scrape-news-task-queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://ugcvhlul:bfCRuVZFOK5jeqA1GyjJsDu6ml4QhyKs@caterpillar.rmq.cloudamqp.com/ugcvhlul"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

SLEEP_TIME_IN_SECONDS = 5
dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print('message is broken')
        return

    task = msg
    text = None

    # support CNN now only
    if task['source'] == 'cnn':
        print('Scraping CNN news')
        text = cnn_news_scraper.extract_news(task['url'])
    else:
        print('News source [%s] is not supported' % task['source'])

    task['text'] = text
    dedupe_news_queue_client.send_message(task)

while True:
    # fetch msg from queue
    # Handle message
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.get_message()
        if msg is not None:

            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
