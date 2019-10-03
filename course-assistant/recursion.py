# --------------------------------------
# CSCI 127, Lab 3                      |
# September 17, 2019                   |
# Nathan Stouffer                      |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

## my code below

## list of vowels
vowels = [ "a", "e", "i", "o", "u" ]

## function to count the number of vowels
## in a sentence with the built in method
def count_built_in(sentence):
    ## variable to store number of vowels
    num_vowels = 0
    ## iterate through the vowels
    for i in range(0, len(vowels)):
        num_vowels += sentence.count(vowels[i])

    return num_vowels

def count_iterative(sentence):
    num_vowels = 0
    ## iterate through sentence
    for i in range(0, len(sentence)):
        ## test if char is a vowel
        if (sentence[i] in vowels):
            num_vowels += 1

    return num_vowels
        

def count_recursive(sentence):
    ## base case of one vowel
    if (len(sentence) == 1):
        if (sentence in vowels):
            return 1

        else:
            return 0
    ## general case splits up the current sentence at the middle
    else:
        mid = len(sentence)//2
        return count_recursive(sentence[:mid]) + count_recursive(sentence[mid:])
    

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
