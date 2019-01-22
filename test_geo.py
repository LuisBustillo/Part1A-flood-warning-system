<<<<<<< HEAD
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
=======
from geo import stations_by_distance
from stationdata import build_station_list
def test_stations_by_distance():
    result = stations_by_distance(build_station_list(), (52.2053, 0.1218))
    result_1 = result[0]
    result_2 = result [-1]
    assert len(stations_by_distance.stations_and_distances) > 0
    assert len(stations_by_distance.final) > 0
    assert result_1[1] == 0.840237595667494
    assert result_2[1] == 467.53431870130544
    
>>>>>>> efdc86e9f1274e466769cd77782b9f3f29e989f7
