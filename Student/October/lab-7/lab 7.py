# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# Nathan Stouffer
# --------------------------------------

def print_matrix(p_matrix, p_rows, p_columns, p_matrix_name):
    print(p_matrix_name + "\n")
    for i in range(p_rows):
        output = "| "
        for ia in range(p_columns):
            if (p_matrix.get((i, ia), 0) > -1):
                output += " " + str(p_matrix.get((i, ia), "0")) + "| "
            else:
                output += str(p_matrix.get((i, ia))) + "| "
        print_header(p_columns)
        print(output)

    print_header(p_columns)
    print()

# --------------------------------------

def add_matrices(p_matrix_1, p_matrix_2, p_rows, p_columns):
    matrix_3 = {}

    for key in p_matrix_1:
        if (p_matrix_1.get(key) + p_matrix_2.get(key, 0) != 0):
            matrix_3[key] = p_matrix_1.get(key) + p_matrix_2.get(key, 0)
        if (p_matrix_2.get(key, 0) != 0):
            del p_matrix_2[key]
    for key in p_matrix_2:
            matrix_3[key] = p_matrix_2[key]

    return matrix_3

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main("sparse-matrix.txt")
