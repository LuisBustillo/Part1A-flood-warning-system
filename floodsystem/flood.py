from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
import operator

def stations_level_over_threshold(stations, tol):
    "Function returns a list of tuples of stations at which the current relative water level is greater than tol in the form (station name, relative water level)"    
    relatives = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() >= tol:
            relatives.append((station.name, station.relative_water_level()))
           
    descending_relatives = sorted_by_key(relatives, 1, reverse= True)
    return descending_relatives

def stations_highest_rel_level(stations, N):
        stations_rel_level_list = []
        for station in stations:
                 if station.relative_water_level() != None :
                        stations_rel_level_list.append((station.name, station.relative_water_level()))
        stations_rel_level_list.sort(key = operator.itemgetter(1), reverse =True)
        N_station_list = []
        for i in range (0, len(stations_rel_level_list)):
                if i < N:
                        N_station_list.append(stations_rel_level_list[i])
        return N_station_list

