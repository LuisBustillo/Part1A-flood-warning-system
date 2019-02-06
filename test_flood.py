" Tests for Modules in floodsystem/flood.py "

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from random import randint
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold



def test_stations_highest_rel_level ():
        N = randint(0, 10)
        assert len (stations_highest_rel_level(update_water_levels(build_station_list()), N)) > 0
        assert type (stations_highest_rel_level(update_water_levels( build_station_list()), N))  == list
        for item in stations_highest_rel_level(update_water_levels( build_station_list()), N) :
                assert type(item) == tuple
                assert type(item[0]) == str
                assert type(item[1]) == float

def test_stations_level_over_threshold():
        N = randint(0, 1000)
        assert len(stations_level_over_threshold(update_water_levels(build_station_list()), N)) > 0
        assert type(stations_level_over_threshold(update_water_levels(build_station_list()), N)) == list
        for i in stations_level_over_threshold(update_water_levels(build_station_list()), 0.8):
                assert type(i) == tuple
                assert type(i[0]) == str
                assert type(i[1]) == float