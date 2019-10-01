# --------------------------------------
# CSCI 127, Lab 6
# October 10, 2017
# Nathan Stouffer
# --------------------------------------

# Change 1: The process_season parameters include output_file 

def process_season(output_file, season, games_played, points_earned):
    output_file.write("Season: " + str(season) + ", Games Played: " + games_played + ", Points earned: " + points_earned + "\n")
    output_file.write("Possible Win-Tie-Loss Records\n")
    output_file.write("-----------------------------\n")

    """If wins + ties + losses = games_played and 3*wins + 1* ties = points_earned
       represents planes in xyz, then the points (x, y, z) with integer solutions
       should be all combinations of wins-ties-losses"""

    games_played = int(games_played)
    points_earned = int(points_earned)
    
    normal_vector = [(1*0 - 1*1), -(1*0 - 3*1), (1*1 - 3*1)] #cross product of vectors orthogonal to the two planes
    point = [points_earned // 3, points_earned - ( 3 * (points_earned // 3)), games_played - (points_earned // 3) - (points_earned - ( 3 * (points_earned // 3)))]

    while (point[0] > -1 and point[2] > -1):
        output_file.write(str(point[0]) + "-" + str(point[1]) + "-" + str(point[2]) + "\n")
        for i in range(3):
            point[i] += normal_vector[i]
    output_file.write("\n")

# --------------------------------------

# Change 2: The process_seasons parameters are input_file (e.g. "soccer-in.txt") and output_file (e.g. "soccer-out.txt")

def process_seasons(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    input_line = input_file.readline()
    i = 1
    while input_line:
        input_list = input_line.split()
        process_season(output_file, i, input_list[0], input_list[1])
        i += 1
        input_line = input_file.readline()

    input_file.close()
    output_file.close()

# --------------------------------------

# Change 3: The function process_seasons is called with "soccer-in.txt" and "soccer-out.txt" 

process_seasons("soccer-in.txt", "soccer-out.txt")
