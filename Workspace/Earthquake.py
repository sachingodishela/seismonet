import numpy as np
class EarthQuake:
    waveform = [np.array([]), np.array([]), np.array([])] # ew, ns, vt
    def __init__(self, lat, long, depth, magnitude, time_stamp, region, station):
        self.latitude = lat
        self.longitude = long
        self.depth = depth
        self.magnitude = magnitude
        self.time_stamp = time_stamp
        self.region = region
        self.station = station

    def add_data(self, direction, series):
        if(direction == 'ew'):
            self.waveform[0] = series
        elif(direction == 'ns'):
            self.waveform[1] = series
        else:
            self.waveform[2] = series
