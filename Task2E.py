from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list(use_cache=False)
update_water_levels(stations)

highest_stations = stations_highest_rel_level(stations, 5)
 
'''
for i in highest:
    highest_stations.append(i[1])
'''
for i in highest_stations:
    station_name = i[0]
    station_0 = None
    for station in stations:
        if station.name == station_name:
            station_0 = station
            break                
    dt = 10
    dates0, levs0 = fetch_measure_levels(station_0.measure_id, dt = datetime.timedelta(days = dt))
    plot_water_levels(station_0, dates0, levs0)
    



