import numpy as np
from getpass import getpass
from .get_json import get_json
from .control_server import add_record_to_zone
from .control_server import create_zone
from .helper import ask_question
from .Hardcoded import Hardcoded
from .Server import Server


def main():
    """
    This function is called in `__main__.py`
    """
    hc = Hardcoded("temp")
    get_pwd(hc)
    get_token(hc)
    server = Server(hc.token)

    # step 4 of readme (add a domain to tab "zone")
    create_zone("hiveminds.eu", hc)
    # step 5 of readme
    add_record_to_zone("hiveminds.eu", hc, server)


def get_pwd(hc):
    hc.pwd = getpass(f"Please enter your (new) TechnitiumDNS server password:")
    # print(f'your password = {hc.pwd}')


def get_token(hc):
    # url = "https://api.github.com"
    url = f"http://127.0.0.1:{hc.port}/api/login?user={hc.username}&pass={hc.pwd}"
    response = get_json(url)
    if response["status"] == "ok":
        hc.token = response["token"]
    else:
        raise Exception(
            f"The token was not retrieved from the local technitium host because the status was not ok. The servers response was:{response}"
        )


# TODO: call logout


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
