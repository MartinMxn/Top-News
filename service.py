from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

SERVER_HOST = 'localhost'
SERVER_PORT = 4040


def add(a, b):
    print ("add is called with %d and %d" % (a, b))
    return a + b


# register all server function
RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')

print ("Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT))
RPC_SERVER.serve_forever()
