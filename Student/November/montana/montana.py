import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------

def read_file(file_name):
    """Read census data from a file"""
    
    years = []
    populations = []

    census_file = open(file_name, "r")
    for one_line in census_file:
        values = one_line.split()
        years.insert(0, int(values[0]))
        populations.insert(0, int(values[1]))
    census_file.close()

    years.reverse()
    populations.reverse()

    return ([np.array(years), np.array(populations)])

# --------------------------------------

def main():
    """Main function to produce graphs"""
    
    years, populations = read_file("montana.txt")

    plt.figure("Historical Montana Populations")    # Graph 1
    plt.plot(years, populations, "ro")
    plt.plot(years, populations, "black")
    plt.xlabel("Year")
    plt.ylabel("Population")

    population_gain = np.empty(len(years), dtype=int)
    for i in range(len(population_gain) - 1):
        population_gain[i + 1] = populations[i + 1] - populations[i]
    
    plt.figure("Net Gain in Population")    # Graph 2
    plt.plot(years, population_gain, "ro")
    plt.plot(years, population_gain, "black")
    plt.xlabel("Year")
    plt.ylabel("Population Gain")

    plt.show()

# --------------------------------------

if __name__ == "__main__":
    main()
