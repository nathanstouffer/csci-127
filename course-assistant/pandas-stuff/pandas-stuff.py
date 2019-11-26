import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# November 26, 2019                               |
# Your Name                                       |
# -------------------------------------------------

def main(file_name):
    # read the file_name into a pandas dataframe
    df = pd.read_csv(file_name, header=0)
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    df.plot(title=file_name[:-4], legend=[], x=df.columns[0], y=df.columns[1], kind="bar", color=["blue", "gold"])

    x_axis = df.columns[0]
    y_axis = df.columns[1]

    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
