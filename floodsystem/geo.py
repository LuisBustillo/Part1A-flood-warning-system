# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine

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

    


    
