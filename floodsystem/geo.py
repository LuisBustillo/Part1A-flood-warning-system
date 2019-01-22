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

