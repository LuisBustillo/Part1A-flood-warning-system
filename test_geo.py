from floodsystem.geo import rivers_with_stations, stations_by_river
from floodsystem.stationdata import build_station_list

def test_rivers_with_stations_1 ():
    stations = build_station_list()
    x = rivers_with_stations(stations)
    assert type(x) == list

def test_rivers_with_stations_2 () :
    stations = build_station_list()
    x = rivers_with_stations(stations)
    assert len(x) > 0

def test_stations_by_river_1 (): 
    stations = build_station_list()
    x = stations_by_river(stations)
    assert type(x) == dict

def test_stations_by_river_2 (): 
    stations = build_station_list()
    x = stations_by_river(stations)
    assert len(x) > 0