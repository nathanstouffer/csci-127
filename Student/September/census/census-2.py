census_file = open("census.txt", "r")
summary_file = open("summary.txt", "w")

input_line = census_file.readline()
cumulative_population = 0
while input_line:
    values = input_line.split()
    cumulative_population = cumulative_population + int(values[1])
    summary_file.write(str(cumulative_population) + "\n")
    input_line = census_file.readline()

census_file.close()
summary_file.close()
