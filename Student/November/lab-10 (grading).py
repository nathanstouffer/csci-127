# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Last Modified: 10/31/17 
# -------------------------------------------------
# A program to practice class inheritence that gives different advice based on
#     your major and if you are or aren't having math and major troubles
# -------------------------------------------------

class Generic_Major:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.major_troubles = False
        self.math_troubles = False
        self.honors = False
        self.minor = Generic_Minor()

    def set_minor(self, minor):
        self.minor = minor
        
    def get_first_name(self):
        return self.firstName.title()

    def get_last_name(self):
        return self.lastName.title()

    def get_major(self):
        return "Generic"

    def set_major_troubles(self, troubles):
        self.major_troubles = troubles
        
    def set_math_troubles(self, troubles):
        self.math_troubles = troubles

    def get_major_troubles(self):
        return self.major_troubles

    def get_math_troubles(self):
        return self.math_troubles

    def major_advising(self):
        if self.major_troubles is True:
            print("because you are having troubles with your major:")
            print("--> visit your professor during office hours")
            print("--> visit your academic advisor")

    def math_advising(self):
        if self.math_troubles is True:
            print("because you are having troubles with math:")
            print("--> visit the Math Learning Center in Wilson 1-112")

    def honors_advising(self):
        print("because you are in honors, you can also:")
        print("--> talk Dawn Major")
        print("--> talk to an honors advisor")
        print("--> visit the office hours of an honors professor for help")

    def set_honors(self, honors):
        self.honors = honors

    def get_honors(self):
        return self.honors

        
class CLS_Major(Generic_Major):
    
    def get_major(self):
        return "College of Letters and Science"
    
    def major_advising(self):
        if self.major_troubles is True:
            Generic_Major.major_advising(self)
        
class COE_Major(Generic_Major):
    
    def get_major(self):
        return "College of Engineering"
    
    def major_advising(self):
        if self.major_troubles is True:
            Generic_Major.major_advising(self)
            print("--> visit the EMPower Student Center in Roberts 313")

class Computer_Engineering_Major(COE_Major):
    
    def get_major(self):
        return "Computer Engineering"

    def major_advising(self):
        if self.major_troubles is True:
            Generic_Major.major_advising(self)
            print("--> visit the EMPower Student Center in Roberts 313")

class Physics_Major(CLS_Major):
    
    def get_major(self):
        return "Physics"

    def major_advising(self):
        if self.major_troubles is True:
            CLS_Major.major_advising(self)
            print("--> visit the Physics Learning Center in Barnard Hall 230")

class Computer_Science_Major(COE_Major):
    
    def get_major(self):
        return "Computer Science"

    def major_advising(self):
        if self.major_troubles is True:
            COE_Major.major_advising(self)
            print("--> visit the CS Student Success Center in Barnard Hall 259")
            print("--> visit a CS professional advisor in Barnard Hall 357")

class Generic_Minor:

    def get_minor(self):
        return "No Minor"

    def minor_advising(self):
        pass

class Mechatronics_Minor(Generic_Minor):

    def get_minor(self):
        return "Mechatronics"

    def set_minor(self, minor):
        self.minor = minor

    def minor_advising(self):
        print("Because you are struggling and have a minor:")
        print("--> You could see your minor's advisor for help")
        print("--> See your peer advisor for the Mechanical Engineering department")

class Computer_Science_Minor(Generic_Minor):

    def get_minor(self):
        return "Computer Science"

    def set_minor(self, minor):
        self.minor = minor

    def minor_advising(self):
        print("Because you are struggling and have a minor:")
        print("--> You could see your minor's advisor for help")
        print("--> See your peer advisor for the Computer Science department")

class Physics_Minor(Generic_Minor):

    def get_minor(self):
        return "Physics"

    def set_minor(self, minor):
        self.minor = minor

    def minor_advising(self):
        print("Because you are struggling and have a minor:")
        print("--> You could see your minor's advisor for help")
        print("--> See your peer advisor for the Physics department")

# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------

def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles())+ ", Honors: " + str(student.get_honors())
          + ", Minor: " + str(student.minor.get_minor())+ "\n") #honors part added for honors lab section component
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
        student.minor.minor_advising()
        if student.get_honors(): #added for honors lab section component
            student.honors_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    #honors part added with permission for the honors lab section component
    honors = input("Is " + student.get_first_name() + " " + student.get_last_name() + " in honors? (Y/N)").title()
    if honors == "Y" or honors == "Yes" or honors == "True":
        student.set_honors(True)
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    msu_student.set_minor(Physics_Minor())
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
    msu_student.set_minor(Computer_Science_Minor())
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    msu_student.set_minor(Mechatronics_Minor())
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    msu_student.set_minor(Physics_Minor())
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()


