import diskcache as dc
from os.path import expanduser

cache = dc.Cache(expanduser('~') + '/.opus_api')


def jcache(function):
    """
    Decorator for caching API json results
    """
    def wrapper(*args, **kwargs):
        key = None
        if function.__name__ == 'get':
            key = args
        elif function.__name__ == 'langs':
            key = 'langs'
        if key and key in cache:
            return cache[key]
        result = function(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper


def hcache(function):
    """
    Decorator for caching crawler html
    """
    def wrapper(*args, **kwargs):
        src = args[0]
        trg = args[1]
        key = ('html', src, trg)
        if key in cache:
            html = cache[key]
            return html
        else:
            return function(src, trg)
    return wrapper
