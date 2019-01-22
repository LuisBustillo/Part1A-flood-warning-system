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
    
