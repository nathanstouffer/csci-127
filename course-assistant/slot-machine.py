# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Liberty Bell Slot Machine
# Nathan Stouffer
# Last Modified:
# ---------------------------------------
# Simulate a modified Liberty Bell Slot Machine.
# ---------------------------------------

import random

# Constants that represent the result of spinning a reel
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

## The subsequent function is written by me

def spin_payout(reel_1, reel_2, reel_3):
    ## variabe to store the payout
    payout = 0
    
    ## test if the values in the reel are equal
    if (reel_1 == reel_2 and reel_2 == reel_3):
        ## 3 bells
        if (reel_1 == 5):
            payout = 50
        ## 3 hearts
        if (reel_1 == 2):
            payout = 40
        ## 3 diamonds
        if (reel_1 == 1):
            payout = 30
        ## 3 spades
        if (reel_1 == 3):
            payout = 20
        ## 3 horseshoes
        if (reel_1 == 4):
            payout = 10
    ## 2 horseshoes and any 1 other symbol
    else:
        if (reel_1 == 4):
            if (reel_2 == 4 or reel_3 == 4):
                payout = 5
        elif (reel_2 == 4 and reel_3 == 4):
            payout = 5

    ## return value for payout
    return payout

# ---------------------------------------
# convert
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"

# ---------------------------------------
# test_known_spin
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)

# ---------------------------------------
# test_known_spins
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)

# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times. Calculate and print the expected winnings.
# ---------------------------------------

## The subsequent function is written by me

def simulate(how_many):
    ## variables to store information for winnings ratio
    total_cost = 0.05 * how_many
    total_winnings = 0

    ## simulate the slot machine how_many times
    for i in range(0, how_many):
        ## generate random values for slot
        reel_1 = random.randint(1, 5)
        reel_2 = random.randint(1, 5)
        reel_3 = random.randint(1, 5)
        ## increment total_winnings by current winning
        total_winnings += spin_payout(reel_1, reel_2, reel_3)

    ## convert total_winnings to dollars
    total_winnings /= 100
    ## calculate expected winnings
    expected_winnings = (total_winnings / total_cost)

    print("For every $1 spent, you can expect to win {0:.2f}".format(expected_winnings))

# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    simulate(500000)
          
# ---------------------------------------

main()
