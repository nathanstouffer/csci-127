# --------------------------------------
# CSCI 127, Lab 4
# September 26, 2017
# Nathan Stouffer
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")

    """For a record to be plausible, it must meet two conditions. First, the elements must sum to the
    games played. And, second: 3*(wins) + 1*(ties) + 0*(losses) = points_earned"""

    reverse_list = []
    for i in range(games_played + 1):
        for ia in range(games_played + 1 - i):
            for ib in range(games_played + 1 - i - ia):
                if (i + ia + ib == games_played and 3*i + 1*ia == points_earned):
                    reverse_list += [str(i) + "-" + str(ia) + "-" + str(ib)]

    for ic in range(len(reverse_list)):
        print(reverse_list[-1 * (ic + 1)])

    print()

# --------------------------------------

def process_seasons(seasons):
    for i in range(len(seasons)):
        process_season(i + 1, seasons[i][0], seasons[i][1])

# --------------------------------------

# format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

process_seasons(soccer_seasons)

input()
