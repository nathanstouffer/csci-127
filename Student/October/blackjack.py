import card # imports the file that contains the class "Card"

def evaluate(hand):
    result = 0
    for oneCard in hand:
        result += oneCard.get_value()
    return result

def process_hand(hand):
    output = ""
    for i in range(len(hand)):
        output += hand[i].get_rank() + " of " + hand[i].get_suit()
        if i + 1 < len(hand):
            output += ", "
    output += " evaluates to " + str(evaluate(hand))
    print(output)

ace = card.Card("ace", "spades")
king = card.Card("king", "diamonds")
queen = card.Card("queen", "hearts")
jack = card.Card("jack", "clubs")
ten = card.Card("ten", "spades")
nine = card.Card("nine", "hearts")
eight = card.Card("eight", "diamonds")
seven = card.Card("seven", "clubs")
six = card.Card("six", "spades")
five = card.Card("five", "hearts")
four = card.Card("four", "diamonds")
three = card.Card("three", "clubs")
two = card.Card("two", "spades")

process_hand([ace, king])
process_hand([queen, ace])
process_hand([ace, jack])
process_hand([ten, ace])
process_hand([two, three, four, five, six, seven])
process_hand([eight, nine, two])
