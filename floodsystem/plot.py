import matplotlib
import matplotlib.pyplot as plt
import datetime
from floodsystem.analysis import polyfit
def plot_water_levels(station, dates, levels):
   
    plt.plot(dates, levels)
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation = 45)
    plt.title("Station:     {}\n".format(station.name))
    plt.tight_layout
    plt.show()
    return "No Error"

def plot_water_level_with_fit(station, dates, levels, p):
    pol = polyfit(dates, levels, p)
    x = []
    y = []
    for i in pol:
        i[0].append(y)
        i[1].append(x)
    plt.plot(x, y)
    plt.show()
    xax = matplotlib.dates.date2num(dates)
    plt.plot(xax, levels)
    plt.show()

     
        
