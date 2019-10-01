import random
import Card

class Deck:
    """Deck class for representing and manipulating 52 instances of Card"""

    def __init__(self):
        """A constructor method that creates a 52 card deck"""
        self.cards = []
        for rank in ["two", "three", "four", "five", "six", "seven", "eight",
                     "nine", "ten", "jack", "queen", "king", "ace"]:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                self.cards += [Card.Card(rank,suit)]

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
