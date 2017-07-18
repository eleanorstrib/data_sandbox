import os
import twitter
import csv
from support_accounts import accounts

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY', '')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET', '')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', '')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', '')


api = twitter.Api(consumer_key=TWITTER_API_KEY,
                  consumer_secret=TWITTER_API_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
                  )

def get_tweets(api, accounts):
    for k, v in accounts.items():
        print("getting data for %s...", k)
        tweets = api.GetSearch(term=v['handle'], count=100)
        create_csv(company, tweets)
    return True

def create_csv(company, tweets):
    writer = csv.writer(open(company + '.csv', 'w'))
    json_keys = tweets[0]._json.keys()
    writer.writerow(json_keys)

    record = []
    for i in range(0, len(json_keys)):
        for header in json_keys:
            cell = found_tweets[i]._json[header]
            record.append(cell)
        writer.writerow(record)
        record.clear()
    writer.close()


if __name__ == '__main__':
    get_tweets(api, accounts)
