# -----------------------------------------+
# Your name                                |
# CSCI 127, Program 2                      |
# Last Updated: ???, 2019                  |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

suits = ["clubs", "diamonds", "spades", "hearts"]

## function that returns all the suits of a hand
def get_all_suits(hand):
    result = []
    for card in hand:
        result.append(card[1])
    return result

## function that returns just the ranks of a hand
def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

## function that returns a boolean describing whether
## or not a hand is a straight
def check_straight(hand):
    ## get card ranks
    ranks = get_all_ranks(hand)

    ## assume the hand is a straight until that is disproved
    first = ranks[0]
    ## iterate through the hand
    for i in range(1,5):
        num = ranks[i]
        ## find any cards not in a straight
        if (num != first + i):
            return False
    return True

## function that returns a boolean describing whether
## or not a hand is a flush
def check_flush(hand):
    ## create a concatenated string of all the suits
    suits_in_hand = get_all_suits(hand)

    ## test if hand is a flush
    for suit in suits:
        if (suits_in_hand.count(suit) == 5):
            return True

    ## otherwise, return False
    return False        

## function to determine whether a hand is royal flush
def royal_flush(hand):
    ## get ranks of cards
    ranks = get_all_ranks(hand)

    ## check for royal flush
    return (check_straight(hand) == True and ranks[0] == 10 and check_flush(hand) == True)
        
## function to determine whether a hand is a straight flush
def straight_flush(hand):
    return (check_straight(hand) == True and check_flush(hand) == True)

## function to determine whether a hand is a straight
def straight(hand):
    return (check_straight(hand) == True)

## function to determine whether a hand has four of a kind
def four_of_a_kind(ranks):
    ## iterate through numbers
    for i in range(2,15):
        ## test for four of a kind
        if (ranks.count(i) == 4):
            return True
    return False

## function to determine whether a hand has a full house
def full_house(ranks):
    return (three_of_a_kind(ranks) == True and one_pair(ranks) == True)
##    if (three_of_a_kind(ranks) == True):
##        if (one_pair(ranks) == True):
##            return 
##        for i in range(2,15):
##            ## test for pairs
##            if (ranks.count(i) == 2):
##                return True
##    ## iterate through numbers
##    for i in range(2,15):
##        ## test for three of a kind
##        if (ranks.count(i) == 3):
##            ## iterate through numbers
##            for j in range(2,15):
##                ## test for pairs
##                if (ranks.count(j) == 2):
##                    return True
##            return False
##    return False

## function to determine whether a hand has a three of a kind
def three_of_a_kind(ranks):
    ## iterate through numbers
    for i in range(2,15):
        ## test for three of a kind
        if (ranks.count(i) == 3):
            return True
    return False

## function to determine whether a hand as two pairs
def two_pair(ranks):
    ## iterate through hand
    for i in range(2, 15):
        for j in range(i+1, 15):
            if (ranks.count(i) == 2 and ranks.count(j) == 2):
                return True
    return False

## function to determine whether a hand has at least one pair
## will not evaluate true for three of a kind, but will for two-pair
def one_pair(ranks):
    ## iterate through numbers
    for i in range(2,15):
        ## test for a pair
        if (ranks.count(i) == 2):
            return True
    return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")

    evaluate([[14, "spades"], [10, "spades"], [8, "spades"], [2, "hearts"], [5, "spades"]])     # nothing
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [5, "spades"]])      # 1 pair
    evaluate([[14, "spades"], [6, "spades"], [14, "clubs"], [6, "hearts"], [5, "spades"]])      # 2 pair
    evaluate([[14, "spades"], [6, "spades"], [8, "spades"], [6, "hearts"], [6, "clubs"]])       # 3 of a kind
    evaluate([[3, "spades"], [5, "spades"], [6, "spades"], [4, "hearts"], [2, "spades"]])       # straight
    evaluate([[4, "spades"], [6, "spades"], [4, "diamonds"], [6, "hearts"], [6, "clubs"]])      # full house
    evaluate([[14, "spades"], [6, "spades"], [6, "diamonds"], [6, "hearts"], [6, "clubs"]])     # 4 of a kind
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [9, "spades"], [10, "spades"]])   # straight flush
    evaluate([[13, "spades"], [11, "spades"], [12, "spades"], [14, "spades"], [10, "spades"]])  # royal flush

# -----------------------------------------+

main()
