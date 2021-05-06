import numpy as np
from .Hardcoded import Hardcoded


def ask_question(question):
    return input(question)


def get_public_ip4_adressV0():
    """Returns the 127.0.0.1 IP address of the local machine in Python"""

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


def get_public_ip4_adressV1():
    """Returns the 127.0.0.1 IP address of the local machine in Python"""
    return ask_question(f"Please enter your public ipv4 adress:\n")


def get_public_ip4_adress():
    """Returns the public IP address of the local machine in Python"""
    # Import Module
    import socket

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # connect to the server on local computer
    s.connect(("8.8.8.8", 80))

    # Print Output
    hostname = s.getsockname()[0]
    print(f"hostname={hostname}")
    s.close()
    return hostname


def add_two(x):
    """Adds two to an incoming integer."""
    return x + 2
