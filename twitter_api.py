import os
import twitter
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

# pprint(vars(api))
#
tmobile_support = '@TMobileHelp'
#
# # url = 'https://api.twitter.com/1.1/search/tweets.json?q='
#
found_tweets = api.GetSearch(term='tmobile_support', count=100)


pprint(found_tweets)
