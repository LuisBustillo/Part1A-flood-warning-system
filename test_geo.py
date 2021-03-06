
from floodsystem.geo import rivers_with_stations, stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.station import inconsistent_typical_range_stations
from random import randint
from floodsystem.geo import stations_within_radius

def test_rivers_with_stations ():
    stations = build_station_list()
    x = rivers_with_stations(stations)
    assert type(x) == set
    assert len(x) > 0
    for item in x:
        assert type(item) == str

def test_stations_by_river (): 
    stations = build_station_list()
    x = stations_by_river(stations)
    assert type(x) == dict
    assert len(x) > 0
    for item in x:
        assert type(item) == str

def test_stations_by_distance():
    result = stations_by_distance(build_station_list(), (52.2053, 0.1218))
    result_1 = result[0]
    result_2 = result [-1]
    assert len(stations_by_distance(build_station_list(), (52.2053, 0.1218))) > 0
    assert result_1[1] == 0.840237595667494
    assert result_2[1] == 467.53431870130544
    assert type(result) == list
    assert type(result_1) == tuple
    assert type(result_2) == tuple
    assert type(result_1[1]) == float
    assert type(result_2[1]) == float
    
def test_rivers_station_number ():
    stations = build_station_list()
    N = randint(0, 2000)
    assert len (rivers_by_station_number(stations,N)) > 0
    assert type (rivers_by_station_number(stations,N))  == list
    for item in rivers_by_station_number(stations,N) :
        assert type(item[0]) == str
        assert type(item[1]) == int

def test_inconsistent_typical_range_stations ():
    stations = build_station_list()
    x = inconsistent_typical_range_stations(stations)
    assert type(x) == list
    assert len(x) > 0
    for item in x:
        assert type(item) == str
    
def test_stations_within_radius():
    R = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    assert R[0] == "Haslingfield Burnt Mill"
    assert R[-1] == "Oakington"
    assert type(R) == list
    assert type(R[1]) == str                                                            
                                            