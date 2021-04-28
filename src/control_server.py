import numpy as np
from .get_json import get_json
from .Hardcoded import Hardcoded


def create_zone(domain_name, hc):
    """Creates a domain to the "zone" tab, not the "allowed zone" tab."""
    # http://localhost:5380/api/createZone?token=x&domain=example.com&type=Primary
    url = f"http://127.0.0.1:{hc.port}/api/createZone?token={hc.token}&domain={domain_name}&type=Primary"
    response = get_json(url)
    if response["status"] == "ok":
        print(f"domain_name={domain_name} added succesfully!")
    else:
        raise Exception(
            f"The domain was not added to the zone correctly. The servers response was:{response}"
        )


def add_record_to_zone(domain_name, hc, server):
    """Adds a record to a  domain in the "zone" tab.. Basically sets some properties of the domain for Technitium."""
    # http://localhost:5380/api/addRecord?token=x&domain=example.com
    # http://localhost:5380/api/addRecord?token=x&domain=example.com&type=A&value=<your_local_ipv4_adress>
    url = f"http://127.0.0.1:{hc.port}/api/addRecord?token={hc.token}&domain={domain_name}&type={hc.zone_type}&value={server.your_public_ipv4_address}"
    response = get_json(url)
    if response["status"] == "ok":
        print(f"domain_name={domain_name} added succesfully!")
    else:
        raise Exception(
            f"The domain was not added to the zone correctly. The servers response was:{response}"
        )


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
