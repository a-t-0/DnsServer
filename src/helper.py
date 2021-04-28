import numpy as np
from .Hardcoded import Hardcoded


def ask_question(question):
    return input(question)


def get_public_ip4_adress():
    """Gets the IPv4 IP address of the local machine in Python"""

    # importing socket module
    import socket

    # getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()

    # getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)

    # printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    return ip_address


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
