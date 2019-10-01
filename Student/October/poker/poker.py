
# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 2: Three Card Poker
# Nathan Stouffer
# Last Modified: Tuesday October 3, 2017
# --------------------------------------
# This program recieves an input file with different poker hands of three cards. It takes each hand on its own and evaluates it to see what type of hand it is (between a flush,
# three of a kind, two of a kind, and nothing). It then prints the values of the cards and the evaluation and prints it in a new file. My enhancement
# --------------------------------------

def flush(p_suit_list, p_output): # This function evaluates if the hand is a flush
    if (p_suit_list[0] == p_suit_list[1] == p_suit_list[2]):
        p_output.write("\nPoker Hand Evaluation: FLUSH\n\n")
        return True
    else:
        return False

# --------------------------------------

def three_of_a_kind(p_value_list, p_output): # This function evaluates if the hand is a three of a kind
    if (p_value_list[0] == p_value_list[1] == p_value_list[2]):
        p_output.write("\nPoker Hand Evaluation: THREE OF A KIND\n\n")
        return True
    else:
        return False

# --------------------------------------

def two_of_a_kind(p_value_list, p_output): # This function evaluates if the hand is a two of a kind
    if (p_value_list[0] == p_value_list[1] or p_value_list[0] == p_value_list[2] or p_value_list[1] == p_value_list[2]):
        p_output.write("\nPoker Hand Evaluation: TWO OF A KIND\n\n")
        return True
    else:
        return False

# --------------------------------------

def nothing(p_output): # This funcion only runs if the other scenarios are ALL false, so it just prints "NOTHING"
    p_output.write("\nPoker Hand Evaluation: NOTHING\n\n")

# --------------------------------------

def print_hand(p_hand_as_list, p_output): # This function prints the prints the hand in an organized order
    p_output.write("Poker Hand\n----------\n")

    for i in range(3):
        p_output.write("Card " + str(i + 1) + ": " + p_hand_as_list[i][0].capitalize() + " of " + p_hand_as_list[i][1].capitalize() + "\n")

# --------------------------------------

def evaluate(p_hand_as_list, p_poker_output): # This function provides structure to evaluate the hand
    suit_list = []
    value_list = []
    for i in range(len(p_hand_as_list)):
        value_list.append(p_hand_as_list[i][0])
        suit_list.append(p_hand_as_list[i][1])

    output = flush(suit_list, p_poker_output)
    if (output == False):
        output = three_of_a_kind(value_list, p_poker_output)
        if (output == False):
            output = two_of_a_kind(value_list, p_poker_output)
            if (output == False):
                output = nothing(p_poker_output)

# --------------------------------------

def main(poker_input, poker_output, cards_in_hand):    

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, poker_output)
        evaluate(hand_as_list, poker_output)

# --------------------------------------

poker_input = open("poker.in", "r")

run_loop = True
i = 0
file_path = ""
while (run_loop == True):
    for ii in range(i):
        file_path += "../"
    try:
        run_loop = False
        file_path += "Desktop/poker.out"
        poker_output = open(file_path, "w")
    except FileNotFoundError:
        i += 1
        run_loop = True
    

main(poker_input, poker_output, 3)

poker_input.close()
poker_output.close()

