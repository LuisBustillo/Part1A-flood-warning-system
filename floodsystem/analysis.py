import matplotlib
import numpy as np
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)
    x1 = np.linspace(x[0], x[-1], 100)
    return (poly(x1 - x[0] ), x1)