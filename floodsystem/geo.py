# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
def rivers_with_stations (stations):
    "given a list of station objects, returns a set with the names of the rivers with a monitoring station"
    rivers_set = set()
    for station in stations:
        if len(station.river) > 0 :
            rivers_set.add(station.river)
    return rivers_set


def stations_by_river(stations):
    "function that returns a dictionary that maps river names to a list of station objects on a given river"
    river_station_dict = {}
    for station in stations:
        if station.river not in river_station_dict:
            river_station_dict[station.river] = [station.name] 
        elif station.river in river_station_dict:
            river_station_dict[station.river].append(station.name)
    return river_station_dict

from floodsystem.station import MonitoringStation

def stations_by_distance(stations, p):
    stations_and_distances = []
    
    

    
    
    for station in stations:
        distance = haversine(station.coord, p)
        
        
        stations_and_distances.append((station, distance))
        
    
            
            
    
    final = sorted_by_key(stations_and_distances, 1, reverse=False)
    
    return final

def stations_within_radius(stations, centre, r):
    within_radius = []
    stations_and_distances = []
    for station in stations:
        distance = haversine(station.coord, centre)
        stations_and_distances.append((station, distance))
    for i in stations_and_distances:
        if i[1] < r:
                
            within_radius.append(i[0].name)
    return within_radius

    


    
