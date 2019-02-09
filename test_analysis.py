
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


def test_polyfit():
    stations = build_station_list()
    station = stations[0]
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
    N = randint(0, 5)
    

    
    assert type(polyfit(dates, levels, N)) == tuple
    