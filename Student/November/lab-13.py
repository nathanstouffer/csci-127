import numpy as np
import random
import matplotlib.pyplot as plt

# ----------------------------------

class Deck():
    """A class to represent an unshuffled deck of cards"""

    def __init__(self):
        """A constructor method to create an array containing a deck of cards"""
        self.deck = np.empty(52, dtype=Card)
        
        suit_array = np.array(["hearts", "spades", "diamonds", "clubs"])
        i = 0
        for ia in range(4):
            suit = suit_array[ia]
            for ib in range(1, 14):
                self.deck[i] = Card(suit, ib)
                i += 1

    def get_card(self, index):
        """A reader method to return a card within the deck"""
        return self.deck[index]

# ----------------------------------

class Card():
    """A class to represent a single card"""

    def __init__(self, suit, value):
        """A constructor method to create a card"""
        # The actual face-value of the card is not important for this program,
        # only the point-value. Therefore, the card object only keepts track
        # of the points
        self.suit = suit
        self.value = value
        if (value > 10):
            self.value = 10
        elif (value == 1):
            self.value = 11

    def get_suit(self):
        """A reader method to return the suit of a card"""
        return self.suit

    def get_value(self):
        """A reader method to return the point value of a card"""
        return self.value

# ----------------------------------

def random_index(old_index):
    """A function to ensure that the same card is not chosen twice in a row"""
    new_index = random.randint(0, 51)
    if (new_index == old_index):
        new_index = random_index(old_index)
    return new_index

# ----------------------------------

def main(how_many):
    card_deck = Deck()
    
    sum_arrays = np.empty(how_many, dtype=int)
    for i in range(how_many):
        index = random.randint(0, 51)
        card_one = card_deck.get_card(index)
        card_two = card_deck.get_card(random_index(index))

        sum_arrays[i] = card_one.get_value()
        if (card_one.get_value() == 11 and card_two.get_value() == 11):
            sum_arrays[i] += 1
        else:
            sum_arrays[i] += card_two.get_value()

    plt.figure("CSC 127, Lab 13")
    plt.title("Histogram of BlackJack Hands")
    plt.xlabel("Hand Value")
    plt.ylabel("Probability")
    plt.grid(True)
    plt.xticks(np.arange(4, 22))
    plt.xlim(3, 22)
    plt.hist(sum_arrays, density=True, bins=np.arange(4, 23), color='g', align='left')

    plt.show()

# ----------------------------------

if __name__ == "__main__":
    main(10000)
