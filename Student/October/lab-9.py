# Joy and Beauty of Data, Second Practicum – March 30, 2017

"""Question One. 25 points. Supply the missing function so that when this code runs:"""

def episodes_directed(stranger_things_dict, director):
    episode_count = 0
    for key in stranger_things_dict:
        if stranger_things_dict[key] == director:
            episode_count += 1
    print("The", director, "directed", episode_count, "episodes")

stranger_things = {}
stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
stranger_things["Holly, Jolly"] = "Shawn Levy"
stranger_things["The Body"] = "Shawn Levy"
stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
stranger_things["The Monster"] = "The Duffer Brothers"
stranger_things["The Bathtub"] = "The Duffer Brothers"
stranger_things["The Upside Down"] = "The Duffer Brothers"

episodes_directed(stranger_things, "The Duffer Brothers")
episodes_directed(stranger_things, "Shawn Levy")
episodes_directed(stranger_things, "Kerri Cobb")
print()

##The following output is produced:
##The Duffer Brothers directed 6 episodes
##Shawn Levy directed 2 episodes
##Kerri Cobb directed 0 episodes



"""Question Two. 50 points. Supply the missing class and methods so that when this code runs:"""
# “Stranger Things” is the title of the series.
# “The Duffer Brothers” is the creator of the series.
# 1 is the number of seasons that the series has run.
# 8 is the number of episodes that the series contains.

class Series():

    def __init__(self, series_title, series_creator, number_of_seasons, number_of_episodes):
        self.series_title = series_title
        self.series_creator = series_creator
        self.number_of_seasons = number_of_seasons
        self.number_of_episodes = number_of_episodes

    def __str__(self):
        return self.series_title + " has aired " + str(self.number_of_episodes) + " episodes over " + str(self.number_of_seasons) + " seasons."

    def addSeason(self):
        self.number_of_seasons += 1

    def addEpisodes(self, extra_episodes):
        self.number_of_episodes += extra_episodes


stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)


print(stranger_things)
stranger_things.addSeason() # here comes the next season
stranger_things.addEpisodes(9) # there are now 9 more episodes
print(stranger_things)

##The following output is produced:
##Stranger Things has aired 8 episodes over 1 seasons.
##Stranger Things has aired 17 episodes over 2 seasons. 



"""Question Three. 25 points. Object Oriented Concepts."""
##(a) What is the name of the constructor method in a class?
    # The name of the constructor method in a class is '__init__' and its first parameter must be 'self'
    
##(b) Suppose the class Athlete is already defined and we want to define a new class called
##Runner that is a subclass of Athlete. Complete the following one line of Python:
    # class Runner(Athlete):
    

##(c) In the context of the Athlete class, give a concrete example of the difference between
##an instance and an instance variable.
    # An instance is an object with variables inside it, while an instance variable contains one object

##(d) Describe briefly the difference between a reader method and a writer method.
    # A reader method simply returns information while a writer method changes the states of instance variables in the object

##(e) To override the + operator, an __add__ method can be defined in a class. What method
##must be defined to override the ** operator?
    # __pow__
