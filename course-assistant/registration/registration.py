import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 19, 2019                               |
# Nathan Stouffer                                 |
# -------------------------------------------------

def read_file(file_name):
    fin = open(file_name)
    length = int(fin.readline())

    names = []
    enrollments = np.zeros(length, dtype=np.int16)    

    for i in range(0, length):
        line = fin.readline().split(",")
        names.append(line[0])
        enrollments[i] = int(line[1].rstrip())
    
    fin.close()

    names = np.array(names)

    return names, enrollments

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    #print(college_names)
    #print(college_enrollments)

    plt.figure("Montana State University Fall 2019 Enrollments")
    plt.xlabel("College Name")
    plt.ylabel("College Enrollment")
    plt.yticks(range(0, 4401, 400))
    
    bars = plt.bar(college_names, college_enrollments)
    for i in range(0, len(bars)):
        if (i % 2 == 0):
            # set to blue
            bars[i].set_color('b')
        else:
            # set to yellow
            bars[i].set_color((1.0, 0.8, 0.0))

    plt.show()

# -------------------------------------------------

main("fall-2019.csv")
