from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    relatives = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() >= tol:
            relatives.append((station.name, station.relative_water_level()))
           
    descending_relatives = sorted_by_key(relatives, 1, reverse= True)
    return descending_relatives