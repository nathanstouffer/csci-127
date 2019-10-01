import Deck

cards = Deck.Deck()
cards.print_deck()

cards.shuffle()
print("After shuffling...\n")
cards.print_deck()
