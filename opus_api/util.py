import json
import re
import sys


def minint():
    return -sys.maxsize - 1


def maxint():
    return sys.maxsize


def jsonify(to_jsonify):
    """
    Internal function to dump dicts into json format.
    """
    return json.dumps(to_jsonify, indent=2, sort_keys=True)


def parse_num_tokens(num_tokens):
    """
    Internal function to parse number of tokens
    from human readable format to a number.
    """
    match = re.match("(\d+.\d+)(M|k)", num_tokens)
    if match:
        num = match.group(1)
        quan = match.group(2)
        if quan == 'M':
            return float(num)
        return float(num) / 1000
    return 0
