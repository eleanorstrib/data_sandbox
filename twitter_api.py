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
        try:
            tweets = api.GetSearch(term=v['handle'], count=100)
        except:
            print("There was a problem getting the Tweets :(")
        create_csv(k, tweets)
    return True

def create_csv(company, tweets):
    writer = csv.writer(open(company + '.csv', 'w'))
    json_keys = tweets[0]._json.keys()
    writer.writerow(json_keys)

    record = []
    for i in range(0, len(json_keys)):
        for header in json_keys:
            try:
                cell = tweets[i]._json[header]
            except:
                cell = 'no data'
            record.append(cell)
        writer.writerow(record)
        record.clear()


if __name__ == '__main__':
    get_tweets(api, accounts)
