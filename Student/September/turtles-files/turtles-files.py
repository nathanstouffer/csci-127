import turtle

def main(file_name):
    open_file = open(file_name, 'r')

    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.down()
    
    input_text = open_file.readline()

    while input_text:
        input_list = input_text.split()
        try:
            pen.goto(int(input_list[0]), int(input_list[1]))
        except ValueError:
            if (input_list[0] == 'UP'):
                pen.up()
            else:
                pen.down()
        input_text = open_file.readline()

    window.exitonclick()
            

main("mystery.txt")
