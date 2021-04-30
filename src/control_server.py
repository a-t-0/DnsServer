import numpy as np
from .get_json import get_json
from .Hardcoded import Hardcoded


def delete_domain_from_zones(domain_name, hc):
    """Deletes domain from zones if it is in."""
    # check if domain is in zone or not.
    if is_domain_in_zones(domain_name, hc):
        add_or_delete_zone(hc.delete_zone_keyword, domain_name, hc)


def add_domain_to_zones(domain_name, hc):
    """Adds domain to zones if it is not yet in."""

    # check if domain is in zone or not.
    if is_domain_in_zones(domain_name, hc):
        add_or_delete_zone(hc.delete_zone_keyword, domain_name, hc)
    add_or_delete_zone(hc.add_zone_keyword, domain_name, hc)


def add_or_delete_zone(add_or_delete_keyword, domain_name, hc):
    """Creates a domain to the "zone" tab, not the "allowed zone" tab."""
    # http://localhost:5380/api/createZone?token=x&domain=example.com&type=Primary
    if add_or_delete_keyword == "deleteZone" or add_or_delete_keyword == "createZone":
        url = f"http://127.0.0.1:{hc.port}/api/{add_or_delete_keyword}?token={hc.token}&domain={domain_name}&type=Primary"
        response = get_json(url)
        if response["status"] == "ok":
            print(f"domain_name={domain_name} added or removed succesfully!")
        else:
            raise Exception(
                f"The domain was not added to/removed from the zone correctly. The servers response was:{response}"
            )
    else:
        raise Exception(
            f"You called a method to add or delete, but gave the wrong keyword:{add_or_delete_keyword}."
        )


def is_domain_in_zones(domain, hc):
    """Returns True if the domain is already in the list of zones. False otherwise."""
    # print(f'get_zones(hc)={get_zones(hc)}')
    list_of_domains_in_zone = get_zones(hc)
    if domain in list_of_domains_in_zone:
        return True
    else:
        return False


def get_zones(hc):
    """Returns a list of zones in the Technitium DNS zones tab."""
    # http://localhost:5380/api/createZone?token=x&domain=example.com&type=Primary
    url = f"http://127.0.0.1:{hc.port}/api/listZones?token={hc.token}"
    response = get_json(url)
    if response["status"] == "ok":
        zones_jsons = response["response"]["zones"]
        zones_list = list(map(lambda x: x["name"], zones_jsons))
        print(f"zones_list={zones_list}")
        return zones_list
    else:
        raise Exception(
            f"The domain lists were not retrieved correctly. The servers response was:{response}"
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


def add_record_to_zone_for_name_server(domain_name, hc, value):
    """Adds a record to a  domain in the "zone" tab.. Basically sets some properties of the domain for Technitium."""
    url = f"http://127.0.0.1:{hc.port}/api/addRecord?token={hc.token}&domain={domain_name}&type={hc.ns_zone_type}&value={value}"
    response = get_json(url)
    if response["status"] == "ok":
        print(f"domain_name={domain_name} added succesfully!")
    else:
        raise Exception(
            f"The domain was not added to the zone correctly. The servers response was:{response}"
        )


def add_glue_record(dns, hc, server):
    """Adds a record to a  domain in the "zone" tab.. Basically sets some properties of the domain for Technitium."""
    url = f"http://127.0.0.1:{hc.port}/api/addRecord?token={hc.token}&domain={dns}&type={hc.zone_type}&value={server.your_public_ipv4_address}"
    response = get_json(url)
    if response["status"] == "ok":
        print(f"dns={dns} added succesfully!")
    else:
        raise Exception(
            f"The domain was not added to the zone correctly. The servers response was:{response}"
        )


def add_record_to_zone_for_www(domain_name, hc, server):
    """Adds a record to a  domain in the "zone" tab.. Basically sets some properties of the domain for Technitium."""
    # http://localhost:5380/api/addRecord?token=x&domain=example.com
    # http://localhost:5380/api/addRecord?token=x&domain=example.com&type=A&value=<your_local_ipv4_adress>
    # url = f"http://127.0.0.1:{hc.port}/api/addRecord?token={hc.token}&domain={hc.www_name}&type={hc.www_zone_type}&value={domain_name}"
    url = f"http://127.0.0.1:{hc.port}/api/addRecord?token={hc.token}&domain={hc.www_name}.{domain_name}&type={hc.www_zone_type}&value={domain_name}"
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
