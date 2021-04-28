class Hardcoded:
    """Stores hardcoded data"""

    def __init__(self, pwd):
        """Initialise parameters that are used in configuration."""
        self.script_dir = 5
        self.port = 5380
        self.username = "admin"
        self.pwd = pwd

        # set DNS resource record type:
        self.zone_type = "A"
