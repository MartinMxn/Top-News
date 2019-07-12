import backend_server.operations as operations
import common.mongodb_client as mongodb_client
from common.cloudAMQP_client import CloudAMQPClient

LOG_CLICKS_TASK_QUEUE_URL = "amqp://lznzxucj:TMLwAMQoQ8MHAL_Srf76wLyo1fGsCdP2@woodpecker.rmq.cloudamqp.com/lznzxucj"
LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"
cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def test_getNewsSummariesForUser_basic():
    news = operations.getNewsSummariesForUser('test', 1)
    assert len(news) > 0
    print('test_getNewsSummariesForUser_basic passed')

def test_getNewsSummariesForUser_pagination():
    news_page_1 = operations.getNewsSummariesForUser('test', 1)
    news_page_2 = operations.getNewsSummariesForUser('test', 2)

    assert len(news_page_1) > 0
    assert len(news_page_2) > 0

    digests_page_1_set = set([news['digest'] for news in news_page_1])
    digests_page_2_set = set([news['digest'] for news in news_page_2])

    assert len(digests_page_1_set.intersection(digests_page_2_set)) == 0

    print('test_getNewsSummariesForUser_pagination passed!')

def test_logNewsClickForUser_basic():
    db = mongodb_client.get_db()
    # clean the db, make sure the later test operation is test itself
    db[operations.CLICK_LOGS_TABLE_NAME].delete_many({"userId": "test"})

    operations.logNewsClickForUser('test', 'test_news')

    record = list(db[operations.CLICK_LOGS_TABLE_NAME].find().sort([('timestamp', -1)]).limit(1))[0]

    assert record is not None
    assert record['userId'] == 'test'
    assert record['newsId'] == 'test_news'
    assert record['timestamp'] is not None

    db[operations.CLICK_LOGS_TABLE_NAME].delete_many({"userId": "test"})

    # Verify the message has been sent to queue
    msg = cloudAMQP_client.get_message()
    assert msg is not None
    assert msg['userId'] == 'test'
    assert msg['newsId'] == 'test_news'
    assert msg['timestamp'] is not None


if __name__ == "__main__":
    test_getNewsSummariesForUser_basic()
    test_getNewsSummariesForUser_pagination()
    test_logNewsClickForUser_basic()