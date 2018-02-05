This web app provides the last available trends by country from Google
Trends and Twitter. You can test it [there](https://trend-getter.herokuapp.com/)

## Installation
If you want to run it locally, you have to:
1. Clone the repo
2. Create a file *cred_clear.txt* in the root directory with your
Twitter API credentials of the form:
```
consumer_key = xxx
consumer_secret = yyy
access_token = zzz
access_secret = aaa
```
(see [there](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)
to get Twitter APi credentials if you don't already have some)

3. Create a file *password.txt* in the root directory containing one line with
a password of a **multiple of 12** characters (12or 24...)
4. Run *crypto.encrypt_credentials()*
5. Run *trendgetter.py*

## Functioning
The credentials encryption part is described [there](https://mancap314.github.io/hide-application-credentials.html)

If no (or wrong) password is provided on the app user interface, only the Google
trends will be shown.

The Twitter trends are not available for certain countries, e.g. Hungary or Czechia.