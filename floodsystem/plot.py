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
    pol, d0 = polyfit(dates, levels, p)
    
    predicted_levels = []
    for date in dates:
        cd = matplotlib.dates.date2num(date)
        pl = pol(cd - d0)
        predicted_levels.append(pl)

    highest = [station.typical_range[1]] * len(dates)
    lowest = [station.typical_range[0]] * len(dates)
    plt.plot(dates, predicted_levels)
    plt.plot(dates, levels)
    plt.plot(dates, lowest)
    plt.plot(dates, highest)
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation = 45)
    plt.title("Station:     {}\n".format(station.name))
    plt.tight_layout
    
    
    plt.show()
    return "No Error"

     
        
