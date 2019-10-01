import string

# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

# ---------------------------

def count_letters(poem_string):
    count_dictionary = {}

    for letter in poem_string:
        for i in range(len(string.ascii_lowercase)):
            if (letter == string.ascii_lowercase[i]):
                try:
                    count_dictionary[string.ascii_lowercase[i]] += 1
                except (KeyError):
                    count_dictionary[string.ascii_lowercase[i]] = 1

    return count_dictionary

# ---------------------------

text = keep_letters("raven.txt")
count_dictionary = count_letters(text)

for i in range(len(string.ascii_lowercase)):
    try:
        print(string.ascii_lowercase[i] + ": " + str(count_dictionary[string.ascii_lowercase[i]]))
    except (KeyError):
        print(string.ascii_lowercase[i] + ": 0")
