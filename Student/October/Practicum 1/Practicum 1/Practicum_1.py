# Question 1:

"""
import turtle

def bobcat_line(p_drawing_turtle, p_number_segments, p_segment_length):
    window = turtle.Screen()
    p_drawing_turtle.goto(0, 0)

    p_drawing_turtle_color = 'gold'
    for i in range(p_number_segments):
        if (p_drawing_turtle_color == 'gold'):
            p_drawing_turtle.color('blue')
            p_drawing_turtle_color = 'blue'
        else:
            p_drawing_turtle.color('gold')
            p_drawing_turtle_color = 'gold'

        p_drawing_turtle.goto(p_drawing_turtle.xcor() + p_segment_length, 0)

    window.exitonclick()

drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle()

number_segments = int(input("Enter number of segments: "))
segment_length = int(input("Enter length of a segment: "))

bobcat_line(drawing_turtle, number_segments, segment_length)
"""

# Question 2:

"""
scores = [0, 31, 27, 31, 49, 21, 17, 25]

wins = "0"
losses = "0"
for i in range(len(scores)):
    if (i % 2 == 0):
        if (scores[i] > scores[i + 1]):
            wins = str(int(wins) + 1)
        else:
            losses = str(int(losses) + 1)

print("MSU has", wins, "win(s)", "and", losses, "loss(es)")
"""
