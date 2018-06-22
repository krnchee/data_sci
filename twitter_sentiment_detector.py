import tweepy
from textblob import textblob

consumer_key = 'BI2NpuGAv8Wk0j7LbTob4GUzK'
consumer_secert = '80LVsuaba0alCj5T5kNBD3H9w8dpjSD45kr2r5McsTr0qLvDOi'

access_token = '1010028021779066880-K5yiJR0eI7PKN8pHyaWm8tAVkQ62Yh'
access_token_secret = '8S3NZC3VXM5bvANCkDPyoiZcxs8vcbO6ZqBRklxHryIxu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secert)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
