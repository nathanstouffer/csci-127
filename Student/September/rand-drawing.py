import random

def main():
    dimensionsList = []

    answer = input("Enter an integer to determine the number of rows: ")
    dimensionsList.append(answer)
    answer = input("Enter an integer to determine the number of columns: ")
    dimensionsList.append(answer)

    for i in range(int(dimensionsList[0])):
        output = ""
        for i in range(int(dimensionsList[1])):
            randNumber = random.randint(1, 2)

            if randNumber == 1:
                output += str("*")
            else:
                output += str("-")
        print(output) 

main()
