# --------------------------------------
# CSCI 127, Lab 6                      |
# October 8, 2019                      |
# Nathan Stouffer                      |
# --------------------------------------

import time
  
## function to determine the average magnitude
## of the earthquakes in the file
def average_magnitude(file_name):
    ## open file
    freader = open(file_name, 'r')
    freader.readline() ## dummy read line

    ## how many earthquakes there are
    count = 0
    ## what will be the average magnitude
    avg_mag = 0

    ## iterate through file, summing the magnitudes
    for line in freader:
        line = line.split(',')
        count += 1
        avg_mag += float(line[2])

    ## close the file
    freader.close()

    ## compute average magnitude
    avg_mag /= count

    ## return average magnitude
    return avg_mag

## function to determine the locations
## of the earthquakes in the file
def earthquake_locations(file_name):
    ## open file
    freader = open(file_name, 'r')
    freader.readline() ## dummy read line

    ## locations list
    loc = []

    ## find locations
    for line in freader:
        line = line.split(',')
        if ((line[-9] in loc) == False):
            loc.append(line[-9])

    ## close file
    freader.close()

    ## sort locations
    loc.sort()
    
    ## print output
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    for i in range(0, len(loc)):
        print(str(i + 1) + ". " + loc[i])
    print()

## function to determine the number of earthquakes
## between bounds in the file
def count_earthquakes(file_name, lower_bound, upper_bound):
    ## open file
    freader = open(file_name, 'r')
    freader.readline()

    ## initialize count of earthquakes in magnitude range
    count = 0

    ## iterate through file, finding the earthquakes
    for line in freader:
        line = line.split(',')
        mag = float(line[2])
        if (mag >= lower_bound and mag <= upper_bound):
            count += 1

    ## close file
    freader.close()

    ## return count
    return count

# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
