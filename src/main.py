import numpy as np
from getpass import getpass
from .get_json import get_json
from .control_server import add_domain_to_zones
from .control_server import add_record_to_zone
from .control_server import add_record_to_zone_for_www
from .control_server import add_record_to_zone_for_name_server
from .control_server import add_glue_record
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
    website = get_website()
    server = Server(hc.token, website)

    # step 4 of readme (add a domain to tab "zone")
    add_domain_to_zones(server.website, hc)
    # step 6 of readme
    add_record_to_zone(server.website, hc, server)
    add_record_to_zone_for_www(server.website, hc, server)

    # add name server name:@, Type:NS, TTL 3600, Data ns2.hiveminds.eu
    add_record_to_zone_for_name_server(server.website, hc, f"ns2.{website}")

    # add name server name:@, Type:NS, TTL 14400, Data ns1.hiveminds.eu
    add_record_to_zone_for_name_server(server.website, hc, f"ns1.{website}")

    # add name server: name:ns1.hiveminds.eu, type:a,TTL: 3600, Data: IP4
    add_glue_record(f"ns1.{website}", hc, server)

    # add name server: name:ns2.hiveminds.eu, type:a,TTL: 3600, Data: IP4
    add_glue_record(f"ns2.{website}", hc, server)


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


def get_website():
    question = f"Please enter your website name, (without the www.) so someting like:mywebsite.io\n"
    return ask_question(question)


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
