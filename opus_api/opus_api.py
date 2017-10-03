# -*- coding: utf-8 -*-

import bs4
import site_cache

"""
Main module.

Provides OPUS queries
"""

sc = site_cache.SiteCache()
c = sc.get_site()
soup = bs4.BeautifulSoup(c, 'html.parser')


def get_title():
    return soup.title
