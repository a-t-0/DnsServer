class Hardcoded:
    """Stores hardcoded data"""

    def __init__(self, pwd):
        """Initialise parameters that are used in configuration."""
        self.script_dir = 5
        self.port = 5379
        self.username = "admin"
        self.pwd = pwd

        # set DNS resource record type:
        self.zone_type = "A"
        self.ns_zone_type = "NS"
        self.www_zone_type = "CNAME"
        self.www_name = "www"

        # set Technitium DNS API properties
        self.add_zone_keyword = "createZone"
        self.delete_zone_keyword = "deleteZone"
