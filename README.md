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