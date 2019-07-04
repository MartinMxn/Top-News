import utils.cloudAMQP_client as cloudAMQP_client

CLOUDAMQP_URL = "amqp://ugcvhlul:bfCRuVZFOK5jeqA1GyjJsDu6ml4QhyKs@caterpillar.rmq.cloudamqp.com/ugcvhlul"

TEST_QUEUE_NAME = "test"


def test_basic():
    client = cloudAMQP_client.CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sent_msg = {'test': 'demo'}
    client.send_message(sent_msg)
    client.sleep(10)
    received_msg = client.get_message()
    assert sent_msg == received_msg
    print("test_basic passed!")


if __name__ == "__main__":
    test_basic()