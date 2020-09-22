import datetime 
import numpy as np
from Earthquake import EarthQuake
from Station import Station
import pickle

earth_quakes = {}
'''
"date_time_string station_code" : [waveforms1, waveforms2, waveforms3, . . .]
'''
stations = {}
'''
"station_code" : [eq_object_without_station]
'''
import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

counter = 1
for file in files("./data/Raw"):
    if(file == 'desktop.ini'):
        continue
    print(str(counter)+'. ',end='')
    counter = counter + 1
    with open('./data/Raw/'+file, 'r') as fp:
        print("current file: {}".format(file))
        direction  = file.split('.')[1]
        line = fp.readline()
        time_string = line.split()
        time_stamp = datetime.datetime.strptime(time_string[2] + " " + time_string[3], '%d/%m/%Y %H:%M:%S')
        line = fp.readline()
        lat = line.split()
        if(len(lat) == 3):
            latitude = lat[1] + " " + lat[2]
        elif (len(lat) == 2):
            latitude = " ".join(lat[1].split('°'))
        else:
            raise Exception("wtf")
        line = fp.readline()
        long = line.split()
        if(len(long) == 3):
            longitude = long[1] + " " + long[2]
        elif(len(long) == 2):
            longitude = " ".join(long[1].split('°'))
        else:
            raise Exception("wtf")
        line = fp.readline()
        depth = line.split()[-1]
        magnitude = float(fp.readline().split()[1])
        region = fp.readline().split()[-1]
        fp.readline()
        fp.readline()
        station_code = fp.readline().split()[-1]
        fp.readline()

        if station_code not in stations:
            station_lat = line.split()
            station_latitude = station_lat[1] + " " + station_lat[2]
            station_long = fp.readline().split()
            station_longitude = station_long[1] + " " + station_long[2]
            station_height = float(fp.readline().split()[-1])
            fp.readline()
            record_time = fp.readline()
            sampling_rate = fp.readline()
        else:
            for i in range(5):
                fp.readline()

        record_duration = fp.readline()
        for i in range(8):
            fp.readline()
        series_data = np.array([])
        for line in fp:
            series_data = np.append(series_data, (float(line.split()[0])))
        time_stamp_string = time_stamp.strftime('%d/%m/%Y, %H:%M:%S')
        if time_stamp_string + " " + station_code in earth_quakes:
            earth_quakes[time_stamp_string + " " + station_code].add_data(direction, series_data)
        else:
            station = Station(station_code, station_latitude, station_longitude, station_height)
            earth_quakes[time_stamp_string + " " + station_code] = EarthQuake(latitude, longitude, depth, magnitude, time_stamp, region, station)

with open('waveforms.pickle', 'wb') as handle:
    pickle.dump(earth_quakes, handle, protocol=pickle.HIGHEST_PROTOCOL)


import matplotlib.pyplot as plt

# data = pickle.load(open('waveforms.pickle', 'rb'))
counter = 1
for quake in earth_quakes:
    print(str(counter) + '. ' + quake)
    counter = counter + 1
    forms = earth_quakes[quake].waveform
    plt.figure(figsize=(19.2, 10.8))
    plt.plot(forms[0], label='E-W', color = 'red')
    plt.plot(forms[1], label='N-S', color = 'yellow')
    plt.plot(forms[2], label='V', color = 'green')
    # plt.show()
    plt.savefig('plots/' + quake.replace('/', '').replace(',', '').replace(' ', '_').replace(':', '') + '.png')