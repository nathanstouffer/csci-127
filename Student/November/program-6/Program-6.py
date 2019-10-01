# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 6: Data Visualization
# Nathan Stouffer and Kevin Browder
# Last Modified: November 21, 2017
# ---------------------------------------
# This program takes the Pre-Disaster Mitigation Plan as a csv from MSU
# and displays it in 3 different graphs (histogram, scatter and pie).
# Each of these graphs displays a different aspect of the plan in a different insightful manner
# ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------

def main():
    buildings_data_frame = pd.read_csv('buildings.csv') ##Import Pre-Mitigation plan into a pandas dataframe

    plt.figure("Figure 1")

    plt.title("Histogram Counting Buildings Constructed per Decade on the MSU campus")
    plt.xlabel("Year Built")
    buildings_data_frame["Year Built"].plot(kind="hist", color="red", grid=True, align='mid') ## Plots a histogram of the number of buildings built per decade


    plt.xticks(np.arange(1890, 2020)[::10])
    plot_2_data = pd.DataFrame(data = list(zip(buildings_data_frame["Square Feet"], buildings_data_frame["Building Value"])), columns=['Square Feet', 'Building Value'])
    plot_2_data.plot.scatter(x="Square Feet", y="Building Value", title="Scatterplot comparing Square Footage to Building Value") ## Plots a scatter plot of square footage vs. building value

    frequency = [0, 0, 0]
    for value in buildings_data_frame["HazMat Risk"]: ## This loop counts the frequency of each HazMat Risk rating and stores it in a list
        if value == "H":
            frequency[0] += 1
        elif value == "M":
            frequency[1] += 1
        elif value == "L":
            frequency[2] += 1

    plot_3_data = pd.DataFrame(data = frequency, columns=[' '], index=["High", "Medium", "Low"])
    plot_3_data.plot(kind='pie', y=' ', title='Pie Chart Showing the HazMat Risk of Buildings at MSU') ## Plots a pie chart of HazMat Risk Ratings
    
    plt.show()

# ---------------------------------------

if __name__ == "__main__":
    main()
