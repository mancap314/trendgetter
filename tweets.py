import tweepy
from tweepy import OAuthHandler
import pycurl
from io import BytesIO
from bs4 import BeautifulSoup
import crypto

auth = None
api = None

def get_woeid_code(country):
    '''get the woeid code of a country'''

    #query this page
    woeid_url = 'http://woeid.rosselliot.co.nz/lookup/{}'.format(country)

    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, woeid_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    body = body.decode('UTF-8')

    # parsing and fetch woeid code
    soup = BeautifulSoup(body, 'lxml')
    code = soup.find('div', id='lookup_result').find("td", {"class": "woeid"}).get_text()

    return code


def get_trends(country, password):
    '''get Tweeter trends for the given country'''
    global auth, api

    if country is '':
        return []

    if not crypto.check_password(password):
        return {'keyword': 'Wrong password for Tweeter trends', 'url': '/'}

    if auth is None: #create the auth (and api) objects only once (singleton pattern)
        credentials = crypto.get_credentials(password) #decrypt the encrypted persisted credentials with the password
        auth = OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
        auth.set_access_token(credentials['access_token'], credentials['access_secret'])
        api = tweepy.API(auth)


    code = get_woeid_code(country)
    try:
        trends = api.trends_place(code)
    except:
        return [{'keyword': 'Sorry, no Twitter trends available for this country', 'url': '/'}]

    res = []
    for trend in trends[0]['trends']:
        res.append({'keyword': trend['name'], 'url': trend['url']})

    return res

# print(get_trends('SWITZERLAND', 'trucbidule973dtu'))


