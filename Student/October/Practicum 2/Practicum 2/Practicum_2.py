# Problem 1

"""score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0

for key in score_differences:
    if score_differences[key] > 0:
        wins += 1
    else:
        losses += 1

print(wins, "wins -", losses, "losses")"""

# Problem 2

"""class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    
    def __init__(self, manufacturer, refrigerant):
        Appliance.__init__(self, manufacturer)
        self.refrigerant = refrigerant

    def __str__(self):
        return "The " + self.manufacturer + " refrigerator contains refrigerant " + self.refrigerant

my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)"""

