# -*- coding: utf-8 -*-

import soup_cache
import settings
import json

"""
Main module.

Provides OPUS queries
"""


def jsonify(to_jsonify):
    return json.dumps(to_jsonify, indent=2, sort_keys=True)


def get(src, target):
    crawl_soup = soup_cache.get(src, target)
    counts = crawl_soup.find('div', {'class': 'counts'})
    corpora = {}
    moses_links = counts.find_all('a', text='moses')
    for link in moses_links:
        corpora[link.parent.parent.children.next().text]\
            = settings.site_url + link['href']
    corpora = jsonify({'corpora': corpora})
    return corpora


def langs():
    langs = {}
    crawl_soup = soup_cache.langs()
    for tag in crawl_soup.find('select').find_all('option'):
        langs[tag['value']] = tag.text
    langs = jsonify({'langs': langs})
    return langs
