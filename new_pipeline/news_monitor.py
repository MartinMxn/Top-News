import os
import redis
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))


import common.news_api_client
from common.cloudAMQP_client import CloudAMQPClient


