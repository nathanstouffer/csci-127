census_file = open("census.txt", "r")

total_pop = 0
for one_line in census_file:
    values = one_line.split()
    print("State: " + values[0] + ", Population: " +  values[1])
    total_pop += int(values[1])

census_file.close()
print("\nThe total population of the United States in 2013 was", str(total_pop) + ".")
