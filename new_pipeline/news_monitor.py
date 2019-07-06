# -*- coding: utf-8

import os
import redis
import sys
import hashlib  # md5hash
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import common.news_api_client as news_api_client
from common.cloudAMQP_client import CloudAMQPClient

# every 10 seconds for every loop, may consider to set a longer time
SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3 #newsexpiresin3days

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://ugcvhlul:bfCRuVZFOK5jeqA1GyjJsDu6ml4QhyKs@caterpillar.rmq.cloudamqp.com/ugcvhlul"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

NEWS_SOURCES = [
    'bbc-news',
    'cnn'
]
# connect redis_client and cloundAMQP_client
redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    num_of_new_news = 0

    # find duplicate
    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).hexdigest()

        if redis_client.get(news_digest) is None:
            num_of_new_news += 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime('%Y-%m-%d%H:%M:$SZ')

            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

        cloudAMQP_client.send_message(news)

    print("Fetched %d new news." % num_of_new_news)

    # use cloudAMQP_client.sleep keep queue heartbeat
    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)