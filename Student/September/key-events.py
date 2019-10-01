import turtle

window = turtle.Screen()

drawer = turtle.Turtle()
drawer.speed(0)

def east():
    drawer.setheading(0)
    drawer.forward(50)

def north():
    drawer.setheading(90)
    drawer.forward(50)

def west():
    drawer.setheading(180)
    drawer.forward(50)

def south():
    drawer.setheading(270)
    drawer.forward(50)
def fTurn():
    drawer.forward(50)
def rRotate():
    drawerOrientation = drawer.heading()
    drawer.setheading(drawerOrientation - 45)

window.onkey(east, "Right")
window.onkey(north, "Up")
window.onkey(west, "Left")
window.onkey(south, "Down")
window.onkey(fTurn, "f")
window.onkey(fTurn, "F")
window.onkey(rRotate, "r")
window.onkey(rRotate, "R")
window.onkey(rRotate, "Next")
window.listen()

window.exitonclick()
