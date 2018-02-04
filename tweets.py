import tweepy
from tweepy import OAuthHandler
import yweather
import crypto

auth = None
api = None

client = yweather.Client()


def get_trends(country, password):
    global auth, api

    if not crypto.check_password(password):
        return {'keyword': 'Wrong password for Tweeter trends', 'url': '/'}

    if auth is None:
        credentials = crypto.get_credentials(password)
        auth = OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
        auth.set_access_token(credentials['access_token'], credentials['access_secret'])
        api = tweepy.API(auth)

    code = client.fetch_woeid(country)
    trends = api.trends_place(code)
    res = []
    for trend in trends[0]['trends']:
        res.append({'keyword': trend['name'], 'url': trend['url']})

    return res

# print(get_trends('SWITZERLAND', 'trucbidule973dtu'))


