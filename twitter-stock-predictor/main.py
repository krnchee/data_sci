
import requests
import requests_oauthlib
import json

url = "https://api.twitter.com/1.1/search/tweets.json?q=Lululemon&count=100"

twitter_consumer_key = 	'ZPZp0TRl1mSRyWIHdWg2Y0V0X'
twitter_consumer_secret = '0SMJBx7NgWepI7vlgdUK0RHoKjWvbXow6uUdfYIlq9005kNAvR'
twitter_access_token = '1010028021779066880-8XN3uB57m7tZ7GFnmStLLT30ER1Kqg'
twitter_access_secret = 'VcF6F3S8ybtinA3Oesj7WnsGsufbWxbP7Lg5aSdpV9HQq'

keywords = ["Acquired", "acquired", "Bought", "bought", "Buyout", "buyout",
            'Underperforming', 'underperforming', 'Stock', 'stock', 'Sell', 'sell'
            'UA', 'under armour' ]

auth = requests_oauthlib.OAuth1(twitter_consumer_key,
                               twitter_consumer_secret,
                               twitter_access_token,
                               twitter_access_secret)

response = requests.get(url, auth = auth)
tweet_json = response.json()
tweet = tweet_json['statuses'][0]['text']
id_str = tweet_json['statuses'][0]['id_str']
lang = tweet_json['statuses'][0]['lang']


for i in range(0,100):
    statuses = tweet_json['statuses']
    for i in range(len(statuses)):
        tweet = statuses[i]['text']
        id_str = statuses[i]['id_str']
        lang = statuses[i]['lang']

        if lang == 'en':
            for word in keywords:
                if word in tweet:
                    print('found tweet')
                    print(tweet)
                else:
                    print('na')
