import os
import twitter
import csv
from pprint import pprint

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY', '')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET', '')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', '')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', '')

api = twitter.Api(consumer_key=TWITTER_API_KEY,
                  consumer_secret=TWITTER_API_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
                  )


tmobile_support = '@TMobileHelp'

found_tweets = api.GetSearch(term='tmobile_support', count=100)

#create and write to csv
writer = csv.writer(open('test.csv', 'w'))
json_keys = found_tweets[0]._json.keys()
writer.writerow(json_keys)

record = []
for i in range(0, len(json_keys)):
    for header in json_keys:
        cell = found_tweets[i]._json[header]
        record.append(cell)
    writer.writerow(record)
    record.clear()

# print(len(found_tweets), type(found_tweets))
# print(json_keys, type(json_keys))
# for k, v in enumerate(found_tweets):
#     print(found_tweets[k])._json
# sample format to get data from json: found_tweets[0]._json['text']
