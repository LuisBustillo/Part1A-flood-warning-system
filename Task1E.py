from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

print ("Task 1E Requirements")
print("---------------")
print( "The {} rivers with the Greatest monitoring stations are : {} ".format(9, rivers_by_station_number(build_station_list(),9) ))