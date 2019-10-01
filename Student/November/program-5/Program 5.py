# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: World Series Batting Averages
# Nathan Stouffer
# Last Modified: November 21, 2017
# ---------------------------------------
# A program to calculate the batting averages of baseball players from an input file.
# The program utilizes objects, inheritance, and numpy arrays.
# For my enhancement, I also gave the batting averages in a bar chart to visualize
# the information.
# ---------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------

class Person:
    """A class for manipulating people"""
    
    def __init__(self, firstName, lastName):
        """A constructor method to initialize properties of a person"""
        self.firstName = firstName
        self.lastName = lastName

    def get_first_name(self):
        """A reader method to return a person's first name"""
        return self.firstName

    def get_last_name(self):
        """A reader method to return a person's last name"""
        return self.lastName

# ---------------------------------------

class Batter(Person):
    """A class for manipulating Batters, a subclass of Person"""
   
    def __init__(self, firstName, lastName, position, at_bats, hits):
        """A constructor method to initialize properties of a batter"""
        self.position = position
        self.at_bats = at_bats
        self.hits = hits
        Person.__init__(self, firstName, lastName)

    def get_position(self):
        """A reader method to return a batter's position"""
        return self.position

    def get_at_bats(self):
        """A reader method to return a batter's at bats"""
        return self.at_bats

    def get_hits(self):
        """A reader method to return a batter's hits"""
        return self.hits

# ---------------------------------------

class All_Batters():
    """A class to store all the batter-objects"""

    def __init__(self, number_of_batters):
        """A constructor method to initialize properties of all the batters"""
        self.batters = np.empty(number_of_batters, dtype=object)

    def __str__(self):
        """An output method to customize the printing of the object"""
        output = "Player {:>33}\n----------------------------------------\n"\
                 .format("Batting Average")

        for batter in self.batters:
            output += "{:<22}".format(batter.get_first_name() + " " +\
                        batter.get_last_name() + "(" + batter.get_position() + ")")

            if (batter.get_at_bats() != 0):
                battingAverage = round(float(batter.get_hits()) / \
                                 float(batter.get_at_bats()), 3)
                output += "{:>19}".format(str(battingAverage) + "(" + str(batter.get_hits()) + \
                          " for " + str(batter.get_at_bats()) + ")\n")
            else:
                output += "   0.000 (0 for 0)\n"

        return output

    def add_info(self, at_bats, hits):
        """A writer method to add hits and at bats to a single batter"""
        self.at_bats += at_bats
        self.hits += hits

    def add_batter(self, index, firstName, lastName, position, at_bats, hits):
        """A writer method to add a single batter"""
        self.batters[index] = Batter(firstName, lastName,\
                                     position, at_bats, hits)

    def get_batter(self, index):
        """A reader method to return a single batter"""
        return self.batters[index]

    def get_length(self):
        """A reader method to return the number of batters"""
        return len(self.batters)

    def plot_batting_averages(self):
        """A method that visualizes the data in a bar chart. The x-ticks are in
           alphabetical order"""
        name_list = []
        average_list = []
        for batter in self.batters:
            name_list.append(batter.get_first_name() + " " + batter.get_last_name())
            average_list.append(round(float(batter.get_hits()) / \
                                 float(batter.get_at_bats()), 3))

        x_positions = np.arange(len(self.batters))
        
        plt.bar(name_list, average_list)
        plt.xticks(x_positions, name_list)
        plt.ylabel("Batting Average")
        plt.title("Batting Average by Player")

        plt.show()

# ---------------------------------------

def create_batter_index(fileName, batters_array, lineNumber):
    """A function to populate the 'self.batters' array in All_Batters"""
    
    file = open(fileName, 'r')

    for i in range(lineNumber):
        line = file.readline()

    i = batters_array.get_length()
    while (i > 0):
        line = file.readline()

        line_list = line.strip().split(',')

        firstName = line_list.pop(0)
        lastName = line_list.pop(0)
        position = line_list.pop(0)

        index = batters_array.get_length() - i
        batters_array.add_batter(index, firstName, lastName, position, 0 , 0)
        i -= 1
        
    file.close()
    
    return batters_array.get_length() + 1

# ---------------------------------------

def add_hit_data(fileName, batters_array, lineNumber):
    """A function to add hit data to an individual batter in All_Batters"""
    file = open(fileName, 'r')

    for i in range(lineNumber):
        line = file.readline()

    for line in file:
        line_list = line.strip().split(',')
        firstName = line_list.pop(0)
        lastName = line_list.pop(0)
        at_bats = int(line_list.pop(1))
        hits = int(line_list.pop(1))
        
        for i in range(batters_array.get_length()):
            batter = batters_array.get_batter(i)
            if (batter.get_first_name() == firstName and \
                batter.get_last_name() == lastName):
                All_Batters.add_info(batter, at_bats, hits)

# ---------------------------------------

def main(fileName):
    file = open(fileName, 'r')
    number_of_batters = int(file.readline())
    file.close()
    
    batters_array = All_Batters(number_of_batters)
    
    lineNumber = create_batter_index(fileName, batters_array, 1)
    print(batters_array)

    add_hit_data(fileName, batters_array, lineNumber)
    print(batters_array)

    batters_array.plot_batting_averages()

# ---------------------------------------

if __name__ == "__main__":
    main("batting.txt")
