import turtle
import random

window = turtle.Screen()

def create(x, y):
    racer = turtle.Turtle()
    racer.up()
    racer.shape("turtle")
    racer.color(random.random(), random.random(), random.random())
    racer.goto(x, y)
    racer.down()
    racer.stamp()
    return racer

racer_1 = create(-200, 100)
racer_2 = create(-200, 0)
racer_3 = create(-200, -100)

for i in range(10):
    racer_1.forward(random.randint(1, 40))
    racer_1.dot()
    racer_2.forward(random.randint(1, 40))
    racer_2.dot()
    racer_3.forward(random.randint(1, 40))
    racer_3.dot()

racer_1_distance_traveled = racer_1.xcor() - -200
racer_2_distance_traveled = racer_2.xcor() - -200
racer_3_distance_traveled = racer_3.xcor() - -200

if racer_1.xcor() > racer_2.xcor() and racer_1.xcor() > racer_3.xcor():
    print("Turtle racer #1 wins, traveling a distance of " + str(racer_1_distance_traveled) + " pixels!")
elif racer_2.xcor() > racer_1.xcor() and racer_2.xcor() > racer_3.xcor():
    print("Turtle racer #2 wins, traveling a distance of " + str(racer_2_distance_traveled) + " pixels!")
elif racer_3.xcor() > racer_1.xcor() and racer_3.xcor() > racer_2.xcor():
    print("Turtle racer #3 wins, traveling a distance of " + str(racer_3_distance_traveled) + " pixels!")
elif racer_1.xcor() == racer_2.xcor() and racer_1.xcor() > racer_3.xcor():
    print("Turtle racer #1 and #2 tied for the win, traveling a distance of " + str(racer_1_distance_traveled) + " pixels!")
elif racer_2.xcor() == racer_3.xcor() and racer_2.xcor() > racer_1.xcor():
    print("Turtle racer #2 and #3 tied for the win, traveling a distance of " + str(racer_2_distance_traveled) + " pixels!")
elif racer_1.xcor() == racer_3.xcor() and racer_1.xcor() > racer_2.xcor():
    print("Turtle racer #1 and #3 tied for the win, traveling a distance of " + str(racer_1_distance_traveled) + " pixels!")
else:
    print("Turtle racer #1, #2, and #3 tied for the win, traveling a distance of " + str(racer_1_distance_traveled) + " pixels!")
                      
window.exitonclick()
    
