import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 14, 2017
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_yahtzee(self):
        """A reader method that tests the data for yahtzees"""
        counts = Yahtzee.count_outcomes(self)
        for value in counts:
            if (value == 5):
                return True

    def is_it_full_house(self):
        """A reader method that tests the data for full houses"""
        full_house = False

        counts = Yahtzee.count_outcomes(self)
        for value in range(1, 7):
            if (counts[value] == 3):
                for value in range(1, 7):
                    if (counts[value] == 2):
                        full_house = True
        return full_house

    def is_it_large_straight(self):
        """A reader method that tests the data for large straights"""
        bool_1to5 = True
        bool_2to6 = True
        
        counts = Yahtzee.count_outcomes(self)
        for value in range(1, 6):
            if (counts[value] != 1):
                bool_1to5 = False
        for value in range(2, 7):
            if (counts[value] != 1):
                bool_2to6 = False

        if (bool_1to5 == True or bool_2to6 == True):
            return True
        else:
            return False
        
# -------------------------------------------------
        
def main(how_many):

    yahtzees = 0
    full_houses = 0
    large_straights = 0
    game = Yahtzee()

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_yahtzee():
            yahtzees += 1
        elif game.is_it_full_house():
            full_houses += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Yahtzees:", yahtzees)
    print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
    print("Number of Full Houses:", full_houses)
    print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Large Straight Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(5000)
    
        
