## Prerequisites for this project
```
React
Node
Python3
pip
MongoDB
```

## server frontend build
```
cd ./web_server/client
npm run build
```

## server backend start
```
npm start
```

## Python RPC server start
```
python ./backend_server/service.py
```

## Web Scrapers 
```
python ./common/news_api_client.py
```

## User info store in mlib
## News store in local mongodb
## Start web screaper to scrap latest news

## mongodb cli
```
mongo
> show dbs
admin     0.000GB
config    0.000GB
local     0.000GB
top-news  0.004GB
> show tables;
> use top-news
switched to db top-news
> show tables;
news
> 

```

## redis clean
```
redis cli
> flushall
OK
```

## Why RPC / RPC vs REST ?
```
REST: for external usage, front-end to back-end, REST better, because:
Pros:
1. resource oriented
2. easy to modify
2. easy to cache
Cons:
1. format could changed
2. hard to authentication

RPC:
Pros:
1. action oriented
2. RPC is transparentt, like a local procedure call
3. strictly defined, client must know the method name, argument/type
Cons:
1.hard to modify, cause both client and server need to change
```

## Time Decay Model
```
Topic based model, based on user click and more weight on user click, topic associated with predict click probability

initial 14 topics start with same probability
if selected: p = (1 - a) * p + a
if not: p = (1 - a) * p
a = time decay weight(0.2), larger -> more weight on recent
```

## Interview 
```
Intro
In my recent project, I designed and implemented a real time news scraping and recommendation system. The system uses a news pipeline to scrape latest news from various of sources such CNN, BBC. To render the news, I built a single-page web application using React. In addition, in order to customize news list for users, I designed and built a training pipeline for news topic modeling using Tensorflow.

Challenge?
One challenge I was facing is the architecture design of the entire system. The entire system consists of different subsystems. Some requires prompt response like Web server. And some needs longer time to process but could be asynchronous such as news fetching. To make all subsystems work together, I decoupled the Web server, backend server and machine learning serving system using RPC. Besides, I used Worker Thread pattern to implement news fetching with RabbitMQ integrated. As a result, all subsystems are organized in Service Oriented Architecture.
```