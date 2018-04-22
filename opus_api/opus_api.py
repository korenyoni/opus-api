# -*- coding: utf-8 -*-

from opus_api.util import jsonify, parse_num_tokens, minint, maxint
from opus_api.cache import jcache
import opus_api.crawler as crawler
import opus_api.settings as settings
import requests
import json
import bs4
from opus_api.exceptions import InvalidSrcException, InvalidTrgException, InvalidFormException

"""
Main module.

Provides OPUS queries
"""


def checkLangs(src, target):
    """
    Ensure src and target are both valid,
    raise specific exceptions in case either are not.
    """
    valid_langs = json.loads(lang_map())
    if src not in valid_langs:
        raise InvalidSrcException(src)
    if target not in valid_langs:
        raise InvalidTrgException(target)


def checkForm(form):
    """
    Ensure form is valid
    """
    if form not in {'moses', 'tmx'}:
        raise InvalidFormException(form)


@jcache
def get(src, target, minimum=minint(), maximum=maxint(), form='moses'):
    """
    Get corpora for src-target (default format: MOSES)
    """
    checkLangs(src, target)
    checkForm(form)

    html = crawler.get(src, target)
    crawl_soup = bs4.BeautifulSoup(html, 'html.parser')
    counts = crawl_soup.find('div', {'class': 'counts'})

    corpora = []
    link_id = 1
    moses_links = counts.find_all('a', text=form)
    for link in moses_links:
        row = link.parent.parent.contents
        name = row[0].text
        url = settings.site_url + link['href']
        src_tokens = row[3].text
        trg_tokens = row[4].text
        src_tokens_f = parse_num_tokens(src_tokens)
        trg_tokens_f = parse_num_tokens(trg_tokens)
        total_s = src_tokens_f + trg_tokens_f
        if (total_s > minimum
                and (total_s < maximum or maximum == maxint())):
            corpora.append(
                {
                    'name': name,
                    'id': link_id,
                    'url': url,
                    'src_tokens': src_tokens,
                    'trg_tokens': trg_tokens
                })
            link_id += 1
    corpora = jsonify({'corpora': corpora})
    return corpora


@jcache
def lang_map():
    """
    Get name-id mapping of available languages
    """
    lang_list = json.loads(langs())
    name_id_map = {}
    for lang in lang_list:
        name_id_map[lang['name']] = lang['id']
    return jsonify(name_id_map)


@jcache
def langs():
    """
    Get list of both src and target languages
    """
    html = requests.get(settings.site_url).content
    crawl_soup = bs4.BeautifulSoup(html, 'html.parser')

    langs = []
    lang_id = 0
    tags = crawl_soup.find('select').find_all('option')
    for tag in tags:
        name = tag['value']
        langs.append({
            'name': name,
            'id': lang_id,
            'description': tag.text
        })
        lang_id += 1
    langs.pop(0)
    langs = jsonify(langs)
    return langs
