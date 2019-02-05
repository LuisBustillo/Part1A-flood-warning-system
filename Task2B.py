from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)

lis = stations_level_over_threshold(stations, 0.8)
print(lis)
