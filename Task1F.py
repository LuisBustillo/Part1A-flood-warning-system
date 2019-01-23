from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

print("Task 1F Requirements")
print("----------------")

print(sorted(inconsistent_typical_range_stations(build_station_list())))
