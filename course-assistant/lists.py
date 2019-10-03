# --------------------------------------
# CSCI 127, Lab 4
# September 24, 2019
# Nathan Stouffer
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    
    ## my code is written below
    
    ## first solution is here
    ## we assume that there exists at least one solutio
    wins = points_earned // 3
    ties = points_earned % 3
    losses = games_played - wins - ties

    valid = True
    while (valid):
        ## print possible record
        print(str(wins) + "-" + str(ties) + "-" + str(losses))
        
        ## compute new solution
        wins -= 1
        ties += 3
        losses -= 2
        
        ## test that solution is still valid
        if (wins < 0 or losses < 0):
            valid = False

    print()

# --------------------------------------

def process_seasons(seasons):
    ## iterate through each season
    for i in range(len(seasons)):
        season = seasons[i]
        process_season(i+1, season[0], season[1]) 

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[2, 3], [2, 4], [2, 6], [17, 17], [17, 24], [0, 0], [10, 2], [10, 3]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
