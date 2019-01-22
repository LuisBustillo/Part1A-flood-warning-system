import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
R = geo.stations_within_radius(build_station_list(),  (52.2053, 0.1218), 10)
print(R)