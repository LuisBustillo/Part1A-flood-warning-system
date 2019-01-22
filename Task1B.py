import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
a = geo.stations_by_distance(build_station_list(), (52.2053, 0.1218))
c = a[:10]
d = a[-10:]

for i in c:
    print(i[0].name , i[0].town , i[1])
    
for i in d:
    print(i[0].name, i[0].town, i[1])
    
