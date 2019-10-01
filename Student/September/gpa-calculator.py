
# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Nathan Stouffer
# Last Modified: September 9, 2017 
# ---------------------------------------
# This program calculates the GPA of a user. It first asks how many courses the user is taking, and, based on that answer, it prompts the user to report the letter grade recieved and number credits
# each course is worth. The program then converts the letter grade to a 4-point scale and computes the GPA using the standard method (multiplying each translated grade by the number of credits the
# the course was worth, finding that sum, and dividing it by the total credits taken. It then prints that value.
# ---------------------------------------

def errorHandleMethod(pI): #This method ensures that users input variable type 'int' when necessary
    runLoop = True
    while runLoop == True:
        try:
            if pI == -1:
                userInput = int(input("Enter the number of courses you are taking: "))
                runLoop = False
                return userInput
            else:
                additionalCredits = int(input("Enter credits for course " + str(pI + 1) + ": "))
                return additionalCredits
        except ValueError:
            print("You did not enter a valid anser. Please enter an integer.")

def translate(pGrade): #This method organizes the options of what the user could type and return the correct gpa point value
    if pGrade == 'A' or pGrade == 'a':
        return 4.0;
    elif pGrade == 'A-' or pGrade == 'a-':
        return 3.7;
    elif pGrade == 'B+' or pGrade == 'b+':
        return 3.3;
    elif pGrade == 'B' or pGrade == 'b':
        return 3.0;
    elif pGrade == 'B-' or pGrade == 'b-':
        return 2.7;
    elif pGrade == 'C+' or pGrade == 'c+':
        return 2.3;
    elif pGrade == 'C' or pGrade == 'c':
        return 2.0;
    elif pGrade == 'C-' or pGrade == 'c-':
        return 1.7;
    elif pGrade == 'D+' or pGrade == 'd+':
        return 1.3;
    elif pGrade == 'D' or pGrade == 'd':
        return 1.0;
    elif pGrade == 'F' or pGrade == 'f':
        return 0.0;
    else:
        return 'incorrect value';

courseCount = 0
while courseCount <= 0:
    courseCount = errorHandleMethod(-1)

creditList = []
gradeList = []
gpa = 0

for i in range(courseCount): #Based on how many courses the user said he/she was taking. This prompts the user for the letter grades and credits for each course
    runLoop = True
    
    while runLoop == True:
        print()
        courseGrade = input("Enter grade for course " + str(i + 1) + ": ")
        courseCredits = errorHandleMethod(i)
        gradeList.append(courseGrade)
        creditList.append(courseCredits)
    
        if translate(gradeList[i]) != 'incorrect value':
            gpaPoints = translate(gradeList[i])
            gpa += gpaPoints * creditList[i]
            runLoop = False
        else:
            print('You did not enter a valid grade. Please try again.')
            gradeList.remove(courseGrade)
            creditList.remove(courseCredits)
            runLoop = True

creditListSum = 0

for ii in range(courseCount):
    creditListSum += creditList[ii]

gpa /= creditListSum

print()
print("Your GPA is " + str(round(gpa, 2)))

print()
print("Press enter to quit.")
input()
