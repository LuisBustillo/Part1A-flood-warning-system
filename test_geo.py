




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

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius


def test_stations_by_distance():
    result = stations_by_distance(build_station_list(), (52.2053, 0.1218))
    result_1 = result[0]
    result_2 = result [-1]
    assert len(stations_by_distance(build_station_list(), (52.2053, 0.1218)) > 0
    
    assert result_1[1] == 0.840237595667494
    assert result_2[1] == 467.53431870130544
    assert type(result) == list
    assert type(result_1) == tuple
    assert type(result_2) == tuple
    assert type(result_1[1]) == float
    assert type(result_2[1]) == float
    
def test_stations_within_radius():
    R = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    assert R[0] == "Haslingfield Burnt Mill"
    assert R[-1] == "Oakington"
    assert type(R) == list
    assert type(R[1]) == str