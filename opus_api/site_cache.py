import requests
import requests_cache


class Singleton(type):
    """
    Singleton metaclass
    https://stackoverflow.com/a/6798042/4650776
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = \
                super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SiteCache(object):
    """
    Class managing a single site cache
    """
    __metaclass__ = Singleton
    requests_cache.install_cache('site')

    def get_site(self):
        return requests.get('http://opus.lingfil.uu.se/').content
