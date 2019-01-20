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
    
    
    distances = []
    
    
    for station in stations:
        distance = haversine(station.coord, p)
        
        
        stations_and_distances.append((station, distance))
        
    
            
            
    
    final = sorted_by_key(stations_and_distances, 1, reverse=False)
    print(stations_and_distances[:10])
    return final


    


    
