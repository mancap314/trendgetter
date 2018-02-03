import pycurl
from io import BytesIO
from bs4 import BeautifulSoup
import pandas as pd


base_url = 'https://trends.google.com/trends/hottrends/atom/feed?pn='
country_code = {'UNITED_STATES': 'p1', 'ARGENTINA': 'p30', 'AUSTRALIA': 'p8', 'AUSTRIA': 'p44', 'BELGIUM': 'p41',
                 'BRAZIL': 'p18', 'CANADA': 'p13', 'CHILE': 'p38', 'COLOMBIA': 'p32', 'CZECHIA': 'p43',
                 'DENMARK': 'p49', 'EGYPT': 'p29', 'FINLAND': 'p50', 'FRANCE': 'p16', 'GERMANY': 'p15', 'GREECE': 'p48',
                 'HONG_KONG': 'p10', 'HUNGARY': 'p45', 'INDIA': 'p3', 'INDONESIA': 'p19', 'IRELAND': 'p54',
                 'ISRAEL': 'p6', 'ITALY': 'p27', 'JAPAN': 'p4', 'KENYA': 'p37', 'MALAYSIA': 'p34', 'MEXICO': 'p21',
                 'NETHERLANDS': 'p17', 'NEW_ZEALAND': 'p53', 'NIGERIA': 'p52', 'NORWAY': 'p51', 'PHILIPPINES': 'p25',
                 'POLAND': 'p31', 'PORTUGAL': 'p47', 'ROMANIA': 'p39', 'RUSSIA': 'p14', 'SAUDI_ARABIA': 'p36',
                 'SINGAPORE': 'p5', 'SOUTH_AFRICA': 'p40', 'SOUTH_KOREA': 'p23', 'SPAIN': 'p26', 'SWEDEN': 'p42',
                 'SWITZERLAND': 'p46', 'TAIWAN': 'p12', 'THAILAND': 'p33', 'TURKEY': 'p24', 'UKRAINE': 'p35',
                 'UNITED_KINGDOM': 'p9', 'VIETNAM': 'p28'}


def get_google_trends(country):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, '{}{}'.format(base_url, country_code[country]))
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    body = body.decode('UTF-8')

    # parsing
    soup = BeautifulSoup(body, 'xml')
    res = []
    for item in soup.find_all('item'):
        keyword = item.find('title').get_text()
        title = item.find('ht:news_item_title').get_text().replace('<b>', '').replace('</b>', '')
        source = item.find('ht:picture_source').get_text()
        link = item.find('ht:news_item_url').get_text()
        publication_date = item.find('pubDate').getText()
        res.append({'keyword': keyword, 'title': title, 'source': source, 'link': link, 'publication_date': publication_date})

    return res

def get_countries():
    return sorted(list(country_code.keys()))


# # example
# country = 'SWITZERLAND'
# res_ch = get_google_trends(country)
# print(res_ch)




