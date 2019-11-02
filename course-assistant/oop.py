# -----------------------------------------------------
# CSCI 127, Lab 8
# October 22, 2019
# Nathan Stouffer
# -----------------------------------------------------

# class to represent a contact in a simple smartphone
class Contact:

    # constructor to initialize global variables
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number

        self.title = ""

    # method to print out contact info
    def print_entry(self):
        name = self.title
        if (self.title != ""):
            name += " "
        name += self.first + " " + self.last
        output = "{:25}{}".format(name, self.number)
        print(output)

    # method to set the first name
    def set_first_name(self, first):
        self.first = first

    # method to set the title
    def set_title(self, title):
        self.title = title

    # method to return the number
    def get_cell_number(self):
        return self.number

    # method to return the area code
    def get_area_code(self):
        return self.number[0:3]

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
