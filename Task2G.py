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

severe = stations_highest_rel_level(stations, 10)
print(severe)
high = []
x = datetime.datetime.now()
print(x)
y = matplotlib.dates.date2num(x) + 1
print(y)

for station in stations:
    if station.latest_level != None and station.typical_range != None:
        dt = 2
        dates0, levs0 = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
    
        pol, d0 = polyfit(dates0, levs0, 4)
     
        pl = pol(y - d0)
    
        relative = (pl - station.typical_range[0]) / station.typical_range[1] - station.typical_range[0]
        
    
        if relative >= 1 and station not in severe:
            high.append((station.name, relative)) 
print(high)   

    
