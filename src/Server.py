class Server:
    """Stores server data"""

    def __init__(self, token, website):
        """Initialise parameters that are used in configuration."""
        self.token = token
        self.website = website
        from .helper import get_public_ip4_adress
        from .helper import get_public_ip4_adressV0
        from .helper import get_public_ip4_adressV1

        self.your_public_ipv4_address = get_public_ip4_adress()
        # self.your_public_ipv4_address = get_public_ip4_adressV0()
        self.your_public_ipv4_address = get_public_ip4_adressV1()
        print(f"self.your_public_ipv4_address={self.your_public_ipv4_address}")
