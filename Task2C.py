from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels

print("Task 2C Requirements")
print("--------------------")

stations = build_station_list()
update_water_levels(stations)

print(stations_highest_rel_level(stations, 10))

"Alternatively use Function that depended enitirely on Task 2B"