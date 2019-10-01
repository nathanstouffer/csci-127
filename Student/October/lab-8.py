# -----------------------------------------------------
# CSCI 127, Lab 8
# October 24, 2017
# Nathan Stouffer
# -----------------------------------------------------

import string

class Contact():
    """An object containing information regarding contacts"""

    def __init__(self, firstName, lastName, phoneNumber):
        """A method assigning the information for a contact"""
        
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.title = ""

    def __str__(self):
        """A method that prints the information of a conctact"""
        if self.title != "":
            return ("{:25}".format(self.title + " " +  self.firstName + " " +  self.lastName) + self.phoneNumber)
        else:
             return ("{:25}".format(self.firstName + " " +  self.lastName) + self.phoneNumber)

    def set_first_name(self, firstName):
        """A method reassigning the first name of a contact"""
        self.firstName = firstName

    def set_title(self, title):
        """A method reassigning the title of a contact"""
        self.title = title

    def get_cell_number(self):
        """A method returning the cell phone number of a contact"""
        return self.phoneNumber

    def get_area_code(self):
        """A method returning the area code of a contact"""
        areaCode = ""
        for i in range(3):
            areaCode += self.phoneNumber[i]

        return areaCode
            

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        print(person)
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
