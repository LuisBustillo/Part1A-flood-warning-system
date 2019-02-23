from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
import matplotlib

stations = build_station_list()
update_water_levels(stations)

threat_stations = stations_highest_rel_level(stations, 50)
station_list = list()
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

failed_stations = list()
for station in station_list[10:]:
    station = station[0]
    if station.typical_range_consistent():
        dt = 2
        dates0, levs0 = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        try:
            pol, d0 = polyfit(dates0, levs0, 4)
        except IndexError:
            failed_stations.append(station.name)
            print("Skipping a station")
            continue
     
        pl = pol(y - d0)
    
        relative = station.relative_water_level()
        
    
        if relative >= 0.5 and pl > station.latest_level:
            high.append((station.name, relative)) 
print("High:", high)  
print("Failed stations:", failed_stations) 

    
