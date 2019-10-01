# --------------------------------------
# CSCI 127, Lab 2
# September 12, 2017
# Nathan Stouffer
# --------------------------------------

import turtle    

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.goto(-300, 300)
border.down()
for side in range(4):
    border.forward(600)
    border.right(90)

lollipop = turtle.Turtle()
lollipop.color("red")
lollipop.hideturtle()
lollipop.speed(0)

stick = turtle.Turtle()
stick.color("black")
stick.width(5)
stick.hideturtle()
stick.speed(0)
stick.right(90)

""" 
Do not delete or change any of the Python statements above this line.

The next 4 statements illustrate a lollipop of radius 30 whose bottom 
is at (0,0) and a stick of length 60 whose top appears at (0, 0)
""" 

import random

def draw_lollipop(pRadius, pXCor, pYCor):
    stick.up()
    stick.goto(pXCor, pYCor)
    stick.down()
    stick.forward((2 * pRadius))

    lollipop.up()
    lollipop.goto(pXCor, pYCor)
    lollipop.down()
    lollipop.begin_fill()
    lollipop.circle(pRadius)
    lollipop.end_fill()

for i in range(100):
    radius = random.randint(10, 30)
    xCor = random.randint((-300 + radius), (300 - radius))
    yCor = random.randint((-300 + 4 * radius), (300 - 4 * radius))
    
    draw_lollipop(radius, xCor, yCor)
