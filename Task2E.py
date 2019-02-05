from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels

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
    

station_name = highest_stations[0]
station_0 = None
for station in stations:
    if station.name == station_name:
        station_0 = station
        break
dt = 10
dates0, levs0 = fetch_measure_levels(station_0.measure_id, dt = datetime.timedelta(days = dt))

station_name = highest_stations[1]
station_1 = None
for station in stations:
    if station.name == station_name:
        station_1 = station
        break
dt = 10
dates1, levs1 = fetch_measure_levels(station_1.measure_id, dt = datetime.timedelta(days = dt))

station_name = highest_stations[2]
station_2 = None
for station in stations:
    if station.name == station_name:
        station_2 = station
        break
dt = 10
dates2, levs2 = fetch_measure_levels(station_2.measure_id, dt = datetime.timedelta(days = dt))

station_name = highest_stations[3]
station_3 = None
for station in stations:
    if station.name == station_name:
        station_3 = station
        break
dt = 10
dates3, levs3 = fetch_measure_levels(station_3.measure_id, dt = datetime.timedelta(days = dt))

station_name = highest_stations[4]
station_4 = None
for station in stations:
    if station.name == station_name:
        station_4 = station
        break
dt = 10
dates4, levs4 = fetch_measure_levels(station_4.measure_id, dt = datetime.timedelta(days = dt))


plot_water_levels(station_0, dates0, levs0)
plot_water_levels(station_1, dates1, levs1)
plot_water_levels(station_2, dates2, levs2)
plot_water_levels(station_3, dates3, levs3)
plot_water_levels(station_4, dates4, levs4)


