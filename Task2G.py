from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.geo import stations_within_radius
import matplotlib
import numpy as np

location = (52.21, 0.103)
radius = 30

def rel_level (x, station):
    return (x - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])

def rising_gradient(pol, d0, x):   
    grad_poly = np.polyder(pol)
    grad = grad_poly (x - d0)
    if grad > 0: 
        return True
    else :
        return False

stations = build_station_list()
update_water_levels(stations)
stations_in_radius = stations_within_radius(stations, location, radius)
threat_stations = list()
for station in stations_in_radius:
    station_name = station
    station_0 = None
    for station in stations:
        if station.name == station_name:
            station_0 = station
            if station.typical_range_consistent():
                threat_stations.append(station_0)
                break 
highest_stations = stations_highest_rel_level(threat_stations, 10)

for station in list(highest_stations):
    
    if station[1] <= 1:
        highest_stations.remove(station)

high = list()
moderate = list()
low = list()
failed_stations = list()

for i in highest_stations:
    station_name = i[0]
    station_0 = None
    for station in threat_stations:
        if station.name == station_name:
            station_0 = station
            threat_stations.remove(station_0)

for station in threat_stations:
    try:
        dt = 2 
        dates0, levs0 = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        pol, d0 = polyfit(dates0, levs0, 4)
        #print (pol, d0, y-d0)
        #print(pol(y - d0), station.typical_range[1])
    except (IndexError, ValueError, KeyError):
        failed_stations.append(station.name)
        print("Skipping a station")
        continue

    x = datetime.datetime.now()
    y = matplotlib.dates.date2num(x) + 1
    
    if rel_level(pol(y - d0), station) >= 0.7 and rising_gradient(pol, d0, y):
        high.append(station)
    elif rel_level(pol(y + 1 - d0), station) >= 0.7 and rising_gradient(pol, d0, y + 1):
        moderate.append(station)
    else:
        low.append(station) 


print("Severe:", [highest_stations])
print("High:", [station.name for station in high])
print("Moderate:", [station.name for station in moderate])
print("Low:", [station.name for station in low])
print("Failed stations:", list(set(failed_stations)))





