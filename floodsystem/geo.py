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

import operator

def rivers_by_station_number(stations , N):
    "function  that determines the N rivers with the greatest number of monitoring stations."    
    river_stations_tuple = []
    for station in stations:
        river_stations_tuple.append((station.river, len(stations_by_river(stations)[station.river])),)
    set(river_stations_tuple)
    ordered_list = list(set(river_stations_tuple))
    ordered_list.sort(key = operator.itemgetter(1), reverse =True)
    final_list = []
    for item in range (0,len(ordered_list)):
        if item <=  N-1:
            final_list.append(ordered_list[item])
        if item > N-1 :
            if (ordered_list[item][1]) ==  (ordered_list[N-1][1]):
                final_list.append(ordered_list[item])
    return final_list



def stations_by_distance(stations, p):
    "function returns a list of tuples in format (station name, distance from p)"
    stations_and_distances = []
    for station in stations:
        distance = haversine(station.coord, p)
        stations_and_distances.append((station, distance))
    final = sorted_by_key(stations_and_distances, 1, reverse=False)
    
    return final

def stations_within_radius(stations, centre, r):
    "function returning <a list of all stations within a distance r of the centre"
    within_radius = []
    stations_and_distances = []
    for station in stations:
        distance = haversine(station.coord, centre)
        stations_and_distances.append((station, distance))
    for i in stations_and_distances:
        if i[1] < r:
                
            within_radius.append(i[0].name)
    return within_radius

    


    
