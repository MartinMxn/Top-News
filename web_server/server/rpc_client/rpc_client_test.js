var client = require('./rpc_client');

client.add(1, 2, function(res) {
  console.assert(res == 3);
})

client.getNewsSummariesForUser('test_user', 1, function(response) {
  console.assert(response != null);
});