# -*- coding: utf-8 -*-

import bs4
import site_cache
import pprint

"""
Main module.

Provides OPUS queries
"""

sc = site_cache.SiteCache()
c = sc.get_site()
soup = bs4.BeautifulSoup(c, 'html.parser')


def get_title():
    return soup.title


def langs(pp):
    langs = {}
    for tag in soup.find('select').find_all('option'):
        langs[tag['value']] = tag.text
    langs = {'langs': langs}
    return pprint.pformat(langs) if pp else langs
