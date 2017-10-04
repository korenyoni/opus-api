import bs4
import settings
import requests
import crawler
import diskcache as dc
from os.path import expanduser

cache = dc.Cache(expanduser('~') + '/.opus_api')


def get(src, trg):
    if (src, trg) not in cache:
        html = crawler.get(src, trg)
        cache[(src, trg)] = html
    return bs4.BeautifulSoup(cache[(src, trg)], 'html.parser')


def langs():
    if 'main' not in cache:
        html = requests.get(settings.site_url).content
        cache['main'] = html
    return bs4.BeautifulSoup(cache['main'], 'html.parser')
