# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Your Name                            |
# --------------------------------------

# The missing functions go here.

## function to instantiate and return a dictionary
def create_dictionary(filename):
    # open file
    fin = open(filename, 'r')

    # create empty dictionary
    ascii_dict = {}

    # iterate through file
    for line in fin:
        line = line.strip().split(",")
        # declare key and val variables
        key = line[1]
        val = line[0]

        # test for weird cases
        if key == "comma":
            key = ","
        elif key == "space":
            key = " "

        # add value to dictionary
        ascii_dict[key] = val

    # close file
    fin.close()

    return ascii_dict

## function to translate a sentence using a given dictionary
def translate(sentence, dictionary, file_name):
    # initialize empty output string
    output = ""
    
    # iterate through each letter in sentence
    for letter in sentence:
        # add output to the string
        output += letter + " "
        # test if letter is key
        if letter not in dictionary:
            output += "UNKNOWN\n"
        else:
            output += str(dictionary[letter]) + "\n"

    # print(output) # for testing
            
    # open file
    fout = open(file_name, "w")
    # output string
    fout.write(output)
    # close file
    fout.close()

# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
