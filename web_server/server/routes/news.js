var express = require('express');
var rpc_client = require('../rpc_client/rpc_client');
var router = express.Router();

router.get('/', function(req, res, next) {
  news = [
    {
      'url': 'http://us.cnn.com/',
      'title': "sdsadsadasd",
      'source': 'cnn',
      'urlToImage': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562087066613&di=1e6882c26ca810e945de145a9894d15a&imgtype=0&src=http%3A%2F%2Fpic25.nipic.com%2F20121205%2F10197997_003647426000_2.jpg',
      'digest': 'ewqeqwe123qw',
      'reason': 'Recommend'
    },
    {
      'url': 'http://us.cnn.com/',
      'title': "sdsadsadasd",
      'source': 'cnn',
      'urlToImage': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562087066613&di=1e6882c26ca810e945de145a9894d15a&imgtype=0&src=http%3A%2F%2Fpic25.nipic.com%2F20121205%2F10197997_003647426000_2.jpg',
      'digest': 'ewqe11qwew1we123qw',
      'reason': 'Hot'
    }
  ]

  res.json(news);
})
 /* GET news list. */

// "localhost:3000/news/userId/1@1.com/pageNum/2"
// router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
//   console.log('Fetching news...');
//   user_id = req.params['userId'];
//   page_num = req.params['pageNum'];

//   rpc_client.getNewsSummariesForUser(user_id, page_num, function(response) {
//     res.json(response);
//   });
// });

// router.post('/userId/:userId/newsId/:newsId', function(req, res, next) {
//   console.log('logging news click...');
//   user_id = req.params['userId'];
//   page_num = req.params['newsId'];

//   rpc_client.logNewsClickForUser(user_id, newsId);
//   res.status(200);
// });

module.exports = router;
