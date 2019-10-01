
def average(p_grade1, p_grade2):
    return ((int(p_grade1) + int(p_grade2)) // 2)

# ------------------

def main():
    file_input = open("grades.csv", 'r')
    file_output = open("grades2.csv", 'w')

    input_line = file_input.readline()
    input_line = input_line[:-1] + " Average\n"
    file_output.write(input_line)
    input_line = file_input.readline()

    while input_line:
        input_line = input_line[:-1]
        input_line_list = input_line.split(", ")
        input_line = input_line + ", " + str(average(input_line_list[1], input_line_list[2])) + "\n"
        file_output.write(input_line)
        
        input_line = file_input.readline()

    file_input.close()
    file_output.close()

# ------------------

main()
