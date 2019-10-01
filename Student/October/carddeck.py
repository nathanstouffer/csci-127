class Card:
    """Card class for representing and manipulating one playing card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def __str__(self):
        """Overrides the information used by the print function"""
        return "The " + self.rank + " of " + self.suit

# -----------------------------------------------------

import random

class Deck:
    """Deck class for representing and manipulating 52 instances of Card"""

    def __init__(self):
        """A constructor method that creates a 52 card deck"""
        self.cards = []
        for rank in ["two", "three", "four", "five", "six", "seven", "eight",
                     "nine", "ten", "jack", "queen", "king", "ace"]:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                self.cards += [Card(rank,suit)]

    def print_deck(self):
        """A method that prints the 52 card deck"""
        print("Deck of Cards")
        print("-------------")
        number = 1
        for card in self.cards:
            print(number, card)
            number += 1
        print()

    def shuffle(self):
        """A writer method that shuffles a deck of cards"""
        for i in range(len(self.cards)):
            new_location = random.randint(0, 51)
            self.cards[i], self.cards[new_location] = self.cards[new_location], self.cards[i]

# -----------------------------------------------------

cards = Deck()
cards.print_deck()

cards.shuffle()
print("After shuffling...\n")
cards.print_deck()
