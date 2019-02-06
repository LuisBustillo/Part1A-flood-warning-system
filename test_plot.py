from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
def test_plot_water_levels():
    stations = build_station_list()
    station = stations[0]
    assert plot_water_levels(station, [0, 1, 2, 3, 4], [10, 20, 30, 40, 50]) == "No Error"