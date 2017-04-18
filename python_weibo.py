import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from   mpl_toolkits.mplot3d import Axes3D

def simple_plot():
    """
    simple plot
    """
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin =np.cos(x), np.sin(x)

    plt.figure(figsize=(8,6), dpi=80)
    plt.title("plot title")
    plt.grid(True)
    
    plt.xlabel("x label")
    plt.xlim(-4.0, 4.0)
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

    plt.ylabel("y label")
    plt.ylim(-1.0, 1.0)
    plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

    plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos")
    plt.plot(x, y_sin, "g-",  linewidth=2.0, label="sin")

    plt.legend(loc="upper left", shadow=True)
    plt.show()
    return 
simple_plot()
