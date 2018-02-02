import tweepy
from tweepy import OAuthHandler
import credentials as cred

consumer_key = cred.TWEET_CONSUMER_KEY
consumer_secret = cred.TWEET_CONSUMER_SECRET
access_token = cred.TWEET_ACCESS_TOKEN
access_secret = cred.TWEET_ACCESS_SECRET

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# tweets = api.user_timeline(screen_name='EmmanuelMacron', count=10, include_rts=True)
#
# for tweet in tweets:
#     print(tweet.text) #actual message
#     print(tweet.created_at) #datetime of the tweet, timezone?
#     # print(tweet)
#     print('___________________')

# WOEID: Yahoo geo id lookup, code for France: 23424819, Switzerland: 23424957, Lyon (France): 609125 available on http://woeid.rosselliot.co.nz/lookup/
print('Trends in Switzerland:')
trends_ch = api.trends_place('23424957')
print(trends_ch)
for trend in trends_ch[0]['trends']:
    print(trend['name'])

print('Trends in France:')
trends_fr = api.trends_place('23424819')
print(trends_fr)
for trend in trends_fr[0]['trends']:
    print(trend['name'])

print('trends in Lyon:')
trends_lyon = api.trends_place('609125')
print(trends_lyon)
for trend in trends_lyon[0]['trends']:
    print(trend['name'])
