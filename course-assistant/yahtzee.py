import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 12, 2019
# Nathan Stouffer
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

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_low_roll(self):
        """A general method to determine whether current roll is a low roll"""
        # if any number is larger than 2, than it is not a low roll
        for num in self.rolls:
            if (num > 2):
                return False
        # otherwise return true
        return True

    def is_it_three_of_a_kind(self):
        """A general method to determine whether current roll is three of a kind"""
        # get unique and counts
        unique, counts = np.unique(self.rolls, return_counts=True)
        # tests for three of a kind
        if (len(unique) != 3):
            return False
        for i in range(0, 3):
            if (counts[i] == 3):
                return True
        return False
            

    def is_it_large_straight(self):
        """A general method to determine whether current roll is a large straight"""
        sorted_roll = np.sort(self.rolls)
        # test if the roll is a large straight
        for i in range(0, len(self.rolls) - 1):
            if (sorted_roll[i] + 1 != sorted_roll[i+1]):
                return False
        return True

# -------------------------------------------------
        
def main(how_many):

    low_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(8)       # 8-sided dice

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_low_roll():
            low_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Low Rolls:", low_rolls)
    print("Percent:", "{:.2f}%\n".format(low_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(20000)
    
        
