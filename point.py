class Point:
    def __init__(self, lat_rad, lon_rad, alt_msl=0):
        super().__init__()
        self.lat_rad = lat_rad
        self.lon_rad = lon_rad
        self.alt_msl = alt_msl

    def __str__(self):
        return 'lat_rad: {} lon_rad: {} alt_msl: {}'.format(self.lat_rad, self.lon_rad, self.alt_msl)
