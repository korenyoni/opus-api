import json
import urllib
from hurry.filesize import size


def jsonify(to_jsonify):
    """
    Internal function to dump dicts into json format.
    """
    return json.dumps(to_jsonify, indent=2, sort_keys=True)


def get_size(url):
    """
    Internal function to get size of url.
    OPUS url heads don't have content-length, so the url must be opened
    in order to calculate the size.
    """
    file_length = int(urllib.urlopen(url).info()['content-length'])
    return size(file_length)
