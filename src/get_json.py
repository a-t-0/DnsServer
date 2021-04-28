import numpy as np
from .Hardcoded import Hardcoded

def get_json(url):
    # import urllib library
    from urllib.request import urlopen

    # import json
    import json

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    print(data_json)
    return data_json


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
