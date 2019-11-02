import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Nathan Stouffer                       |
# Last Modified: ??, 2019               |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:

    # constructor to initialize global variables
    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.types = types

    # funtion to return a string representation of the pokemon
    def __str__(self):
        str_types = self.types[0]
        for i in range(1, len(self.types)):
            str_types += " and " + self.types[i]

        return "Number: {}, Name: {}, CP: {}: Type: {}".format(
            self.number, self.name.capitalize(), self.combat_points, str_types)

# function to print the pokedex
def print_pokedex(pokedex):
    for pokemon in pokedex:
        print(pokemon)

# function to look up a pokeman by its name
def lookup_by_name(pokedex, name):
    found = False
    for pokemon in pokedex:
        if name == pokemon.name:
            found = True
            print(pokemon)
    if (found == False):
        print("There is no Pokemon named {}".format(name))

# function to look up a pokeman by its number
def lookup_by_number(pokedex, number):
    found = False
    for pokemon in pokedex:
        if number == pokemon.number:
            found = True
            print(pokemon)
    if (found == False):
        print("There is no Pokemon number {}".format(number))

# function to count the number of pokemon tha are of pokemon_type
def total_by_type(pokedex, pokemon_type):
    count = 0
    for pokemon in pokedex:
        if pokemon_type in pokemon.types:
            count += 1
    print("Number of Pokemon that contain type {} = {}".format(pokemon_type, count))

# function to compute the average hitpoints of the pokedex
def average_hit_points(pokedex):
    average = 0
    count = 0
    for pokemon in pokedex:
        average += pokemon.combat_points
        count += 1
    average /= count
    print("Average Pokemon combat points = {:.2f}".format(average))

# function to print the menu for the user
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
