" Tests for Modules in floodsystem/flood.py "

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from random import randint
from floodsystem.stationdata import build_station_list



def test_stations_highest_rel_level ():
        N = randint(0, 2000)
        assert len (stations_highest_rel_level(update_water_levels(build_station_list()), N)) > 0
        assert type (stations_highest_rel_level(update_water_levels( build_station_list()), N))  == list
        for item in stations_highest_rel_level(update_water_levels( build_station_list()), N) :
                assert type(item[0]) == str
                assert type(item[1]) == int
