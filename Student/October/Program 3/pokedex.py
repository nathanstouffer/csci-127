# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Nathan Stouffer
# Last Modified: October 17, 2017
# ---------------------------------------
# This program recieves a Pokedex from a file and puts the information in a dictionary with numbers as the keys for each Pokemon. It then presents the user with different functions
# to perform on the Pokedex (looking it up by number or name, printing the number of hitpoints, etc.). For my enhancement, I coded another test in the 'getChoice' function to make sure
# the program doesn't break. If the user does not input a value when prompted in the 'getChoice' function, the program will no longer break, it will prompt the user for information
# again.
# ---------------------------------------

import string

# ---------------------------------------

def printMenu(): # This function prints the menu
    print("1. Print Pokedex\n2. Lookup Pokemon by Name\n3. Lookup Pokemon by Number\n4. Print Number of Pokemon\n5. Print Total Hit Points of All Pokemon\n6. Quit\n")

# ---------------------------------------

def printPokedex(pPokedex): # This function prints the entire Pokedex with some formating adjustments
    print("\nThe Pokedex\n-----------")

    number = 1
    for key in pPokedex:
        valueList = list(pPokedex[key])
        print("Number:" + str(number) + ", Name: " + valueList.pop(0) + ", HP: " + str(valueList.pop(0)) + ", Type: " + valueList.pop(0), end="")
        if (len(pPokedex) > 0):
            output = ""
            for i in range(len(valueList)):
                output += " and " + valueList[i]
        print(output)
        print("-----------")
        number += 1

    print("End Pokedex\n\n")

# ---------------------------------------

def lookupByName(pPokedex, pName): # This function looks up a Pokemon by name and prints the information for that Pokemon
    nameNotIn = True
    for key in pPokedex:
        if pName in pPokedex[key]:
            valueList = list(pPokedex[key])
            print("Number:" + str(key) + ", Name: " + valueList.pop(0) + ", HP: " + str(valueList.pop(0)) + ", Type: " + valueList.pop(0), end="")
            if (len(pPokedex) > 0):
                output = ""
                for i in range(len(valueList)):
                    output += " and " + valueList[i]
            print(output + "\n")
            nameNotIn = False
    if (nameNotIn == True):
        print("The pokemon named " + pName.capitalize() + " does not exist\n")

# ---------------------------------------

def lookupByNumber(pPokedex, pNumber): # This function looks up a Pokemon by number and prints the information for that Pokemon
    if (pNumber > 0 and pNumber <= len(pPokedex)):
        valueList = list(pPokedex[pNumber])
        print("Number:" + str(pNumber) + ", Name: " + valueList.pop(0) + ", HP: " + str(valueList.pop(0)) + ", Type: " + valueList.pop(0), end="")
        if (len(pPokedex) > 0):
            output = ""
            for i in range(len(valueList)):
                output += " and " + valueList[i]
        print(output + "\n")
    else:
        print("Error: Pokemon number " + str(pNumber) + " does not exist\n")

# ---------------------------------------

def howManyPokemon(pPokedex): # This function counts how many Pokemon are in the Pokedex
    print("There are " + str(len(pPokedex)) + " different Pokemon\n")

# ---------------------------------------

def howManyHitPoints(pPokedex): # This function calculates the total number of hitpoints in the Pokedex
    totalPoints = 0
    for key in pPokedex:
        valueList = list(pPokedex[key])
        totalPoints += valueList[1]
    print("The total number of hit points for all Pokemon is " + str(totalPoints) + "\n")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def createPokedex(filename): # This function takes the Pokemon and their attributes from a file and puts them in a dictionary with a number as the key
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

def getChoice(low, high, message): # This function ensures that input is the correct type and in a certain range
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice and len(answer) > 0:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
        else:
            print("That is not a number, try again.")
            legal_choice = False
    return answer

# ---------------------------------------

def main(): # This function presents the menu and runs the functions the user wants, until the user wants to quit
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
