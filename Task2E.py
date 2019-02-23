from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit

stations = build_station_list()
update_water_levels(stations)
levels = []
for station in stations:
    if station.latest_level != None and station.typical_range != None:
        relative = (station.latest_level - station.typical_range[0]) / station.typical_range[1] - station.typical_range[0]    
        levels.append((relative, station.name, station.measure_id))
sorted_levels = sorted_by_key(levels, 0)
highest = sorted_levels[-5:]
highest_stations = []
for i in highest:
    highest_stations.append(i[1])

for i in highest_stations:
    station_name = i
    station_0 = None
    for station in stations:
        if station.name == station_name:
            station_0 = station
            break                
    dt = 10
    dates0, levs0 = fetch_measure_levels(station_0.measure_id, dt = datetime.timedelta(days = dt))
    plot_water_levels(station_0, dates0, levs0)
    
    


