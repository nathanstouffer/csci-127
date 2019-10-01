# Object Oriented Programming - Inheritance Demo
# Ryan Bockmon and John Paxton

import random

# ------------------------------------------------

class Character:
    """Common base class for any type of character"""

    def __init__(self, name, age, height, weight):
        """Constructor for a new Character"""
        self.race = "Generic Character"
        self.intelligence = random.randrange(8, 18)
        self.strength = random.randrange(8, 18)
        self.dexterity = random.randrange(8, 18)
        self.wisdom = random.randrange(8, 18)
        self.charisma = random.randrange(8, 18)
        self.name = name                     
        self.age = age
        self.height = height
        self.weight = weight

    def get_intelligence(self):
        """Reader method to return character's intelligence"""
        return(self.intelligence)

    def get_strength(self):
        """Reader method to return character's strength"""
        return(self.strength)

    def get_dexterity(self):
        """Reader method to return character's dexterity"""
        return(self.dexterity)

    def get_wisdom(self):
        """Reader method to return character's wisdom"""
        return(self.wisdom)

    def get_charisma(self):
        """Reader method to return character's charisma"""
        return(self.charisma)

    def set_intelligence(self, intelligence):
        """Writer method to set character's intelligence"""
        self.intelligence = intelligence

    def set_strength(self, strength):
        """Writer method to set character's strength"""
        self.strength = strength

    def set_dexterity(self, dexterity):
        """Writer method to set character's dexterity"""
        self.dexterity = dexterity

    def set_wisdom(self, wisdom):
        """Writer method to set character's wisdom"""
        self.wisdom = wisdom

    def set_charisma(self, charisma):
        """Writer method to set character's charisma"""
        self.charisma = charisma

    def __str__(self):
        """Override the print method for a Character"""
        answer = "Name: " + self.name + "\n"
        answer += "Race: " + self.race + "\n"
        answer += "Age: " + str(self.age) + "\n"
        answer += "Height: " + str(self.height) + " inches\n"
        answer += "Weight: " + str(self.weight) + " lbs\n"
        answer += "Intelligence: " + str(self.intelligence) + "\n"
        answer += "Strength: " + str(self.strength) + "\n"
        answer += "Dexterity: " + str(self.dexterity) + "\n"
        answer += "Wisdom: " + str(self.wisdom) + "\n"
        answer += "Charisma: " + str(self.charisma) + "\n"
        return answer

# ------------------------------------------------

class Human(Character):
    """Define Human to be a subclass of Character"""

    def __init__(self, name, age, height, weight):
        """Constructor for a new Human"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Human"

# ------------------------------------------------

class Orc(Character):
    """Define Orc to be a subclass of Character"""

    def __init__(self, name, age, height, weight):
        """Constructor for a new Orc"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Orc"
        self.set_charisma(self.get_charisma() - 2)
        self.set_intelligence(self.get_intelligence() - 2)
        self.set_strength(self.get_strength() + 2)

# ------------------------------------------------

class Dwarf(Character):
    """Define Dwarf to be a subclass of Character"""

    def __init__(self, name, age, height, weight):
        """"Constructor for a new Dwarf"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Dwarf"
        self.set_charisma(self.get_charisma() - 1)
        self.set_intelligence(self.get_intelligence())
        self.set_strength(self.get_strength() + 4)

# ------------------------------------------------

def main():
    name = input("Enter name: ")                    # e.g. "Borug"
    name = name.capitalize()
    age = input("Enter age: ")                      # e.g. 53
    height = input("Enter height in inches: ")      # e.g. 60
    weight = input("Enter weight in pounds: ")      # e.g. 175
    race = input("Enter race (human, dwarf, or orc): ")     # e.g. "halforc"
    race = race.lower()
    print()

    if (race == "orc"):
        player = Orc(name, age, height, weight)
        print(player)
    elif (race == "human"):
        player = Human(name, age, height, weight)
        print(player)
    elif (race == "dwarf"):
        player = Dwarf(name, age, height, weight)
        print(player)
    else:
        print("Illegal character type.")

# ------------------------------------------------

main()
