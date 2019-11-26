import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Nathan Stouffer     
# Last Modified: ??, 2019               
# ---------------------------------------------
# A brief overview of the program.
# ---------------------------------------------

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)

        self.value = 0

    def read_series_information(self, fname):
        fin = open(fname, 'r')

        i = 0
        for line in fin:
            split = line.split(",")
            card = WackyPackageCard(int(split[0]), split[1], int(split[2]))
            self.cards[i] = card
            i += 1

        fin.close()

    def read_collection_information(self, fname):
        fin = open(fname, 'r')

        for line in fin:
            line = line.strip().lower().split()
            description = line[0]
            for i in range(1, len(line)):
                description += " " + line[i]
            # search for card value
            for card in self.cards:
                if (card.get_description().lower() == description):
                    card.set_cards_owned(card.get_cards_owned()+1)

        fin.close()

    def collection_value(self):
        for card in self.cards:
            self.value += card.get_cards_owned() * card.get_value()
        return self.value

    def determine_missing_information(self):
        count = 0
        cost = 0

        for card in self.cards:
            if (card.get_cards_owned() == 0):
                count += 1
                cost += card.get_value()

        return count, cost
                
    def __str__(self):
        # create header
        output = "My " + str(self.year)
        output += " collection of " + self.manufacturer
        output += " Wacky Packages\n\n"

        output += "{:<10s}{:25}{:>10s}{:>10s}\n".format("Number", "Description", "Value", "Owned")
        output += "{:<10s}{:25}{:>10s}{:>10s}\n".format("------", "-----------", "-----", "-----")
        
        for item in self.cards:
            output += str(item) + "\n"
    
        return output

# Place the missing methods here.  Do not modify the code below.

# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number

# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    print("Number of missing cards =", number_of_missing_cards)
    print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()
