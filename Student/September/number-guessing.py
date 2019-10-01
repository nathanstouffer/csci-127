import random

def main():
    randNumber = random.randint(1, 10)

    print("Guess a number between 1 and 10.\n")

    runLoop = True
    i = 0
    while runLoop == True:
        i += 1
        guess = input("Enter your guess here: ")

        if int(guess) == randNumber:
            if i == 1:
                print("\nCongratulations! You took " + str(i) + " guess.")
            else:
                print("\nCongratulations! You took " + str(i) + " guesses.")
            runLoop = False
        else:
            print("\nPlease try again.")

main()
