import numpy as np
from .get_json import get_json
from .Hardcoded import Hardcoded


def main():
    """
    This function is called in `__main__.py`
    """
    hc = Hardcoded("temp")
    get_token(hc)


def get_token(hc):
    url = "https://api.github.com"
    # url = f'http://localhost:/api/login?user={hc.username}&pass={hc.pwd}'
    ans = get_json(url)


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
