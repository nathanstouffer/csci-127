# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Nathan Stouffer
# Last Modified: Saturday October 28, 2017
# -------------------------------------------------
# This program utilizes objects and inheritance to advise students on where to recieve academic assistence. Each major has its own objects that may inherit properties
# from another major, depending on the hierarchy of that specific major. (i.e. Computer Science is in the College of Engineering). After all the known input is given,
# my enhancement allows the user to add another student with their own properties. It then prints the advising for that student as well.
# -------------------------------------------------

class Base_Student():
    """A class representing a base student"""

    def __init__(self, first_name, last_name):
        """A constructor method that declares the student's information"""
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.major = ""
        self.output = ""
        self.major_troubles = False
        self.math_troubles = False

    def set_major_troubles(self, boolean):
        """A writer method to change the major troubles variable"""
        self.major_troubles = boolean

    def set_math_troubles(self, boolean):
        """A writer method to change the math troubles variable"""
        self.math_troubles = boolean

    def get_first_name(self):
        """A reader method to return a student's first name"""
        return self.first_name

    def get_last_name(self):
        """A reader method to return a student's last name"""
        return self.last_name

    def get_major(self):
        """A reader method to return a student's major"""
        return self.major

    def get_major_troubles(self):
        """A reader method to return the major troubles variable"""
        return self.major_troubles

    def get_math_troubles(self):
        """A reader method to return the math troubles variable"""
        return self.math_troubles

    def major_advising(self):
        """A print method that prints the advising for a student"""
        print(self.output + "--> visit your professor during office hours\n--> visit your academic advisor")
        self.output = ""

    def math_advising(self):
        """A print method that prints the advising for math help"""
        if self.math_troubles:
            print("because you are having troubles with math:\n--> visit the Math Learning Center in Wilson 1-112")

# -------------------------------------------------

class Generic_Major(Base_Student):
    """A class representing an undeclared major"""

    def __init__(self, first_name, last_name):
        """A constructor method for a Generic Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "Generic"

    def major_advising(self):
        """A mutator method that addes to the advising output string"""
        if self.major_troubles:
            if len(self.output) == 0:
                self.output = "because you are having troubles with your major:\n"
            Base_Student.major_advising(self)


# -------------------------------------------------

class CLS_Major(Base_Student):
    """A class representing a CLS Major"""

    def __init__(self, first_name, last_name):
        """A constructor method for a CLS Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "College of Letters and Sciences"

    def major_advising(self):
        """A mutator method that addes to the advising output string"""
        if self.major_troubles:
            if len(self.output) == 0:
                self.output = "because you are having troubles with your major:\n"
            Base_Student.major_advising(self)

# -------------------------------------------------

class COE_Major(Base_Student):
    """A class representing a COE Major"""

    def __init__(self, first_name, last_name):
        """A constructor method for a COE Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "College of Engineering"

    def major_advising(self):
        """A mutator method that addes to the advising output string"""
        if self.major_troubles:
            if len(self.output) == 0:
                self.output = "because you are having troubles with your major:\n"
            self.output += "--> visit the EMPower Student Center in Roberts 313\n"
            Base_Student.major_advising(self)


# -------------------------------------------------

class Computer_Engineering_Major(COE_Major):
    """A class representing a Computer Engineering Major"""

    def __init__(self, first_name, last_name):
        """A constructor method for a Computer Engineering Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "Computer Engineering"


# -------------------------------------------------

class Physics_Major(CLS_Major):
    """A class representing a Physics Major"""

    def __init__(self, first_name, last_name):
        """A constructor method for a Physics Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "Physics"

    def major_advising(self):
        """A mutator method that addes to the advising output string"""
        if self.major_troubles:
            if len(self.output) == 0:
                self.output = "because you are having troubles with your major:\n"
            self.output += "--> visit the Physics Learning Center in Barnard Hall 230\n"
            CLS_Major.major_advising(self)


# -------------------------------------------------

class Computer_Science_Major(COE_Major):
    """A class representing a CS Major"""

    def __init__(self, first_name, last_name):
        """A concstructor method for a Computer Science Major"""
        Base_Student.__init__(self, first_name, last_name)
        self.major = "Computer Science"

    def major_advising(self):
        """A mutator method that addes to the advising output string"""
        if self.major_troubles:
            if len(self.output) == 0:
                self.output = "because you are having troubles with your major:\n"
            self.output += "--> visit the CS Student Success Center in Barnard Hall 259\n--> visit a CS professional advisor in Barnard Hall 357\n"
            COE_Major.major_advising(self)

# -------------------------------------------------

def add_student(first_run):
    """A non-fruitful function that allows the user to add another student to advise"""
    print()
    run_loop = True
    while run_loop:
        if first_run == True:
            answer = input("Would you like to add another student? Enter yes or no: ").lower().strip()
        else:
            answer = 'yes'
        
        if answer == 'no':
            print("------------------------------")
            run_loop = False
        elif answer == 'yes':
            first_name = input("Enter the students' first name: ").lower().strip()
            last_name = input("Enter the students' last name: ").lower().strip()
            major = input("Enter the students' major. Choose from:\n- Generic\n- College of Letters and Sciences\n- College of Engineering\n- Physics\n- Computer Engineering\n- Computer Science\nYour choice: ").lower()
            major_help = False
            math_help = False

            if (major != 'generic' and major != 'college of letters and sciences' and major != 'college of engineering' and major != 'physics' and major != 'computer engineering' and major != 'computer science'):
                answer = invalid_answer("major")
                print("------------------------------")
                if answer == 'no':
                    run_loop = False
                    break
            
            answer = input("Is this student having trouble with his/her major? Enter yes or no: ").lower().strip()
            if (answer != 'yes' and answer != 'no'):
                if invalid_answer("answer") == 'no':
                    run_loop = False
                    break
            elif answer == 'yes':
                major_help = True
                
            answer = input("Is this student having troubles with math? Enter yes or no: ").lower().strip()
            if (answer != 'yes' and answer != 'no'):
                if invalid_answer("answer") == 'no':
                    run_loop = False
                    break
            elif answer == 'yes':
                math_help = True

            if major == 'generic': # This block of if-statements creates an major class depending on the major type
                student = Generic_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
            elif major == 'college of letters and sciences':
                student = CLS_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
            elif major == 'college of engineering':
                student = COE_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
            elif major == 'physics':
                student = Physics_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
            elif major == 'computer engineering':
                student = Computer_Engineering_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
            else:
                student = Computer_Science_Major(first_name, last_name)
                print_added_student(student, major_help, math_help)
        else:
            answer = invalid_answer("answer")
            if answer == 'no':
                run_loop = False
            print("------------------------------")

        first_run = True

# -------------------------------------------------

def invalid_answer(term):
    answer = input("That was not a valid " + term + ". Would you like to try again? Enter yes or no: ").lower().strip()
    if answer == 'yes':
        add_student(False)
    elif (answer != 'no' and answer != 'yes'):
        invalid_answer(term)
    else:
        return answer
    

# -------------------------------------------------

def print_added_student(student, major_help, math_help):
    student.set_major_troubles(major_help)
    student.set_math_troubles(math_help)
    advise(student)

# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    add_student(True) # Calling my enhancement method

# -------------------------------------------------

main()


