import diskcache as dc
from os.path import expanduser

cache = dc.Cache(expanduser('~') + '/.opus_api')


def jcache(function):
    """
    Decorator for caching json results
    """
    def wrapper(*args, **kwargs):
        key = None
        if function.__name__ == 'get':
            key = (args[0], args[1])
        elif function.__name__ == 'langs':
            key = 'langs'
        if key and key in cache:
            return cache[key]
        result = function(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper
