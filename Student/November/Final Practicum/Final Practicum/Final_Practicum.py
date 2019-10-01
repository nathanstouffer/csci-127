## Question 1 -------------------------

"""
import pandas as pd

units = ["Chemical and Biological Engineering", "Civil Engineering", "Computer Engineering", "General Engineering", \
    "Mechanical and Industrial Engineering", "School of Computing"]

enrollments = [563, 731, 410, 210, 1463, 552]

dataset = list(zip(units, enrollments))
dataframe = pd.DataFrame(data=dataset, columns=["Unit", "Enrollment"])

dataframe = dataframe.sort_values(by=["Enrollment"])
print(dataframe[-4:-2])
"""

## Question 2 -------------------------

"""
import numpy as np

# -----------------

class Course_Schedule:

    def __init__(self, how_many):
        self.course_array = np.empty(how_many, dtype=Course)
        self.index = 0

    def __str__(self):
        output = "My Schedule\n-----------"
        for i in range(self.index):
            output += "\n" + self.course_array[i].__str__()
        return output

    def add(self, course):
        self.course_array[self.index] = course
        self.index += 1

# -----------------

class Course:
     
     def __init__(self, rubric, number):
         self.rubric = rubric
         self.number = number

     def __str__(self):
        return self.rubric + " " + str(self.number)

# -----------------

def main():
    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)

main()
"""

## Question 3 -------------------------

"""
import numpy as np
import matplotlib.pyplot as plt

units = ["CS", "ChBE", "Civi", "M&IE", "General", "CpE"]
enrollments = [552, 563, 731, 1463, 210, 410]

plt.figure("COE Enrollment Visualization")
plt.title("Pie Chart of COE Enrollments")
plt.pie(enrollments, labels=units, colors=["blue", "gold"], explode=[.02, .02, .02, .02, .02, .02], counterclock=False)

plt.show()
"""