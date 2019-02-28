
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
radius = 100
 
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
high = list()
severe = list()
moderate = list()
low = list()
failed_stations = list()
 
for station in severe:
    threat_stations.remove(station)
 
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
    if station in highest_stations:
        severe.append(station)
    elif rel_level(pol(y - d0), station) >= 0.7 and rising_gradient(pol, d0, y):
        high.append(station)
    elif rel_level(pol(y + 1 - d0), station) >= 0.7 and rising_gradient(pol, d0, y + 1):
        moderate.append(station)
    else:
        low.append(station) 
 
"""
 
for i in range(0, len(threat_stations)):
    name = threat_stations[i][0]
    for station in stations:
        if station.name == name:
            station_list.append((station, threat_stations[i][1]))
            break
 
severe = station_list[:9]
print("Severe:", [(station[0].name, station[0].relative_water_level()) for station in severe])
high = []
x = datetime.datetime.now()
 
y = matplotlib.dates.date2num(x) + 1
remaining_stations = list()
failed_stations = list()
 
for station in stations:
    if station not in severe and station not in high:
        remaining_stations.append(station)
 
for station in remaining_stations:
    if station.typical_range_consistent():
        dt = 2
        try: 
            dates0, levs0 = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
            pol, d0 = polyfit(dates0, levs0, 4)
            #print (pol, d0, y-d0)
            #print(pol(y - d0), station.typical_range[1])
        except (IndexError, ValueError):
            failed_stations.append(station.name)
            print("Skipping a station")
            continue
     
        pl = pol(y - d0)
        relative = station.relative_water_level()
        #rel_level(pl,station)
    
        if relative >= 0.5 and pl > station.latest_level:
            high.append((station.name, relative )) 
print("High:", high)  



    
" Moderate : in 2 days time relative level will be above 0.7 "
" Low : in 5 days times relative level above 0.7"


z = matplotlib.dates.date2num(x) + 2
 
moderate = []
list_num = len(severe) + len(high)
for station in station_list[list_num + 1:] :
    station = station[0]
    if station.typical_range_consistent():
        dt = 2
        dates_mod, levs_mod = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        try:
            pol_mod, d_mod = polyfit(dates_mod, levs_mod, 4)
            #print (pol_mod, d_mod, z-d_mod)
            #print(pol_mod(z - d_mod), station.typical_range[1])
        except :
            failed_stations.append(station.name)
            print("Skipping a station")
            continue
        rising = rising_gradient(pol_mod, d_mod, z)
        #rel_level(pol_mod(z - d_mod), station)
         
        if  rising == True and pol_mod(z - d_mod) > 0.8*station.typical_range[1]:
            moderate.append((station.name, station.relative_water_level())) 
 
"""
 
print("Severe:", [station.name for station in severe])
print("High:", [station.name for station in high])
print("Moderate:", [station.name for station in moderate])
print("Low:", [station.name for station in low])
print("Failed stations:", list(set(failed_stations))) 



    
