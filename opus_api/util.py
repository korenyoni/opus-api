import json


def jsonify(to_jsonify):
    """
    Internal function to dump dicts into json format.
    """
    return json.dumps(to_jsonify, indent=2, sort_keys=True)
