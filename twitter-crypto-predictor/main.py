import requests
import requests_oauthlib
import json
import matplotlib.pyplot as plt

url = "https://api.twitter.com/1.1/search/tweets.json?q=ethereum&count=100"

twitter_consumer_key = 	'ZPZp0TRl1mSRyWIHdWg2Y0V0X'
twitter_consumer_secret = '0SMJBx7NgWepI7vlgdUK0RHoKjWvbXow6uUdfYIlq9005kNAvR'
twitter_access_token = '1010028021779066880-8XN3uB57m7tZ7GFnmStLLT30ER1Kqg'
twitter_access_secret = 'VcF6F3S8ybtinA3Oesj7WnsGsufbWxbP7Lg5aSdpV9HQq'

keywords = ["Acquired", "acquired", "Bought", "bought", "Buyout", "buyout",
            'Underperforming', 'underperforming', 'Crypto', 'crypto', 'Sell', 'sell'
            'Bitcoin', 'bitcoin', 'ether', 'Ether', 'price', 'Price' ]

auth = requests_oauthlib.OAuth1(twitter_consumer_key,
                               twitter_consumer_secret,
                               twitter_access_token,
                               twitter_access_secret)

response = requests.get(url, auth = auth)
tweet_json = response.json()
# print(tweet_json)
tweet = tweet_json['statuses'][0]['text']
id_str = tweet_json['statuses'][0]['id_str']
lang = tweet_json['statuses'][0]['lang']
bad = {}
badData = {}
time = []

# for i in range(0,20):
statuses = tweet_json['statuses']
for i in range(len(statuses)):
    # print(len(statuses))
    tweet = statuses[i]['text']
    id_str = statuses[i]['id_str']
    lang = statuses[i]['lang']
    print(id_str)
    #  currentTime goes up to the minute, so two tweets a few seconds
    # appart will have the same currentTime.
    currentTime = statuses[i]['created_at'][0:16]
    if lang == 'en':
        for word in keywords:
            if word in tweet:
                if currentTime in bad:
                    bad[currentTime] += 1
                    # adds new tweet to the tweet list for that time.
                    badData[currentTime].append(tweet)
                else:
                    bad[currentTime] = 1
                    badData[currentTime] = [tweet]
                    time.append(currentTime)
                break # break is used to exit for loop. if we find
                       # one keyword, no reason to see if the tweet
                       # has another keyword
    print(bad)
    print(badData)
    print(time)
    try:
        response = requests.get(url, auth = auth)
        tweet_json = response.json()
        statuses = tweet_json['statuses']
    except:
        break

badPlot = []
timePlot = []
counter = 0

for t in time[::-1]: #starting at -1 in time and incrementing backwards
    badPlot.append(bad[t])
    timePlot.append(counter)
    counter += 1

counter = 0
# for t in time[::-1]:
#     while counter < 10:
#         print(t)
#         print(badData[t])
#         counter += 1

# print(timePlot)
# print(badPlot)

timeTicks = []
correspondingTimes = []

for i in range(len(timePlot)):
    if i % 10 == 0:
        correspondingTimes.append(timePlot[i])
        timeTicks.append(time[-(i+1)]) #time is in reverse cronilogical order

plt.figure(figsize=(16,11))
plt.plot(timePlot, badPlot, label='ethereum', c = 'red')
plt.legend()
plt.xticks(correspondingTimes, timeTicks)
plt.show()
