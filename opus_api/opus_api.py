# -*- coding: utf-8 -*-

from json_cache import jcache
import requests
import crawler
import settings
import json
import bs4
import urllib
from exceptions import InvalidSrcException, InvalidTrgException

"""
Main module.

Provides OPUS queries
"""


def jsonify(to_jsonify):
    return json.dumps(to_jsonify, indent=2, sort_keys=True)


def get_size(url):
    return urllib.urlopen(url).info()['content-length']


def checkLangs(src, target):
    valid_langs = json.loads(langs())['langs']
    if src not in valid_langs:
        raise InvalidSrcException(src)
    if target not in valid_langs:
        raise InvalidTrgException(target)


@jcache
def get(src, target):
    checkLangs(src, target)

    html = crawler.get(src, target)
    crawl_soup = bs4.BeautifulSoup(html, 'html.parser')
    counts = crawl_soup.find('div', {'class': 'counts'})

    corpora = {}
    moses_links = counts.find_all('a', text='moses')
    for link in moses_links:
        name = link.parent.parent.children.next().text
        url = settings.site_url + link['href']
        size = get_size(url)
        corpora[name]\
            = {
                'url': url,
                'size': size
            }
    corpora = jsonify({'corpora': corpora})
    return corpora


@jcache
def langs():
    html = requests.get(settings.site_url).content
    crawl_soup = bs4.BeautifulSoup(html, 'html.parser')

    langs = {}
    for tag in crawl_soup.find('select').find_all('option'):
        langs[tag['value']] = tag.text
    langs = jsonify({'langs': langs})
    return langs
