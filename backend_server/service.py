from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import os
import sys
import json
from bson.json_util import dumps
import backend_server.operations as operations
SERVER_HOST = 'localhost'
SERVER_PORT = 4040

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import common.mongodb_client as mongodb_client


# Test function
def add(a, b):
    print ("add is called with %d and %d" % (a, b))
    return a + b


# Get news summaries for a user
def getNewsSummariesForUser(user_id, page_num):
    print("get_news_summaries_for_user is called with %s and %s" % (user_id, page_num))
    return operations.getNewsSummariesForUser(user_id, page_num)


# register all server function
RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(getNewsSummariesForUser, 'getNewsSummariesForUser')


print("Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT))
RPC_SERVER.serve_forever()
