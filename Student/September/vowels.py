# --------------------------------------
# CSCI 127, Lab 3
# September 19, 2017
# Nathan Stouffer
# --------------------------------------

def count_vowels(sentence):
    p_vowel_count = 0

    for i in range(5):
        p_vowel_count += sentence.count(vowel_list[i])

    return p_vowel_count

def count_vowels_iterative(sentence):
    p_vowel_count = 0

    for i in range(len(sentence)):
        for ii in range(5):
            if (sentence[i] == vowel_list[ii]):
                p_vowel_count += 1
    
    return p_vowel_count

def count_vowels_recursive(sentence, p_vowel_count, i):
    if (i == len(sentence)):
        return p_vowel_count
    else:
        p_sentence = sentence

        for ii in range(5):
            if (sentence[i] == vowel_list[ii]):
                p_vowel_count += 1

        i += 1
        return count_vowels_recursive(p_sentence, p_vowel_count, i)

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Number of vowels using recursion =", count_vowels_recursive(sentence, 0, 0))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

vowel_list = ['a', 'e', 'i', 'o', 'u']
main()
