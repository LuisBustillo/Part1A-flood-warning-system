
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
from random import randint

def test_plot_water_levels():
    stations = build_station_list()
    station = stations[0]
    assert plot_water_levels(station, [0, 1, 2, 3, 4], [10, 20, 30, 40, 50]) == "No Error"
def test_plot_water_level_with_fit():
    
    stations = build_station_list()
    station = stations[0]
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
    N = randint(1, 5)
    assert plot_water_level_with_fit(station, dates, levels, N) == "No Error"    