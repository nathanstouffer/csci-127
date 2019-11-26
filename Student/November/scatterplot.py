import matplotlib.pyplot as plt
import numpy as np
import math
import random

# --------------------------------------

def create_y_values():
    y_axis = np.zeros(10)
    for i in range(len(y_axis)):
        y_axis[i] = random.randint(0, 100)
    return y_axis

# --------------------------------------

def main(graph_min, graph_max):
    plt.axis([0, 11, graph_min, graph_max])
    f, (plot1, plot2) = plt.subplots(1, 2, sharey = True)

    x_values = np.arange([1, 11])
    plot1.ylabel("Student score")
    
    plot1.scatter(x_values, create_y_values(), color='r')
    plot2.scatter(x_values, create_y_values(), color='b')

    plt.show()

# --------------------------------------

main(0, 100)
