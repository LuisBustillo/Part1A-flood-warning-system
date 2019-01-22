from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

"Part 1D Requirements"
print("Task 1D part 1")

stations = build_station_list()

river_to_station_set = sorted(rivers_with_stations(stations))
print (len(river_to_station_set))
print ( river_to_station_set[:10])

print("--------------")

print("Task 1D part 2")

Task1D_2 = stations_by_river(stations)
River_Cam = sorted(Task1D_2['River Cam'])
River_Aire = sorted(Task1D_2['River Aire'])
Thames = sorted(Task1D_2['River Thames'])

print("Stations by River Aire : {}".format(River_Aire) )
print("Stations by River Cam : {}".format(River_Cam) )
print("Stations by River Thames : {}".format(Thames) )