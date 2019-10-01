import turtle

pencil = turtle.Turtle()
pencil.hideturtle()
pencil.left(90)

def drawRectangle(pTurtle, pXCor, pYCor, pXSideLength, pYSideLength):
    pTurtle.up()
    pTurtle.goto(pXCor, pYCor)
    pTurtle.down()
    for side in range(2):
        pTurtle.forward(pXSideLength)
        pTurtle.right(90)
        pTurtle.forward(pYSideLength)
        pTurtle.right(90)

drawRectangle(pencil, -50, -50, 100, 100)
pencil.left(90)

pencil.begin_fill()
drawRectangle(pencil, 10, -50, 20, 40)
pencil.end_fill()

drawRectangle(pencil, 30, 15, 20, 20)
drawRectangle(pencil, -10, 15, 20, 20)

triangle = turtle.Turtle()
triangle.hideturtle()

triangle.up()
triangle.color("red")
triangle.goto(-50, 50)
triangle.down()
triangle.begin_fill()
triangle.goto(0, 100)
triangle.goto(50, 50)
triangle.goto(-50, 50)
triangle.end_fill()
