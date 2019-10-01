class Card:
    """Card class for representing and manipulating one playing card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def get_value(self):
        """ A reader method that returns the blackjack value of the card"""
        return self.value

    def assign_value(self, rank):
        """A helper function to determine the blackjack value of a rank"""
        rankDictionary = {'ace': 11, 'king': 10, 'queen': 10, 'jack': 10, 'ten': 10, 'nine': 9, 'eight': 8, 'seven': 7, 'six': 6, 'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
        return rankDictionary.get(rank)
