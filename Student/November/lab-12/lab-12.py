import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Nathan Stouffer
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

# -----------------------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    pop_averages = np.zeros(number_buckets, dtype=int)
    n = len(county_populations)//number_buckets
    for bucket in range(number_buckets):
        bucket_length = county_populations[bucket*n:(bucket+1)*n]
        count = bucket_length.sum()//n
        pop_averages[bucket] = count
    return pop_averages
        
# -----------------------------------------------------

def graph_summary(averages):
    plt.figure("CSCI 127, Lab 12")
    plt.xlabel("Country Groupings")
    plt.ylabel("Country Popuation Average")
    plt.title("Montana County Popluation Analysis")
    plt.plot(range(1, 5), averages, "c--")
    plt.plot(range(1, 5), averages, "bh")
    plt.xticks(range(1, 5))

    plt.show()

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
