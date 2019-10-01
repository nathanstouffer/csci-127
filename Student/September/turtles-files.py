import turtle

def main(file_name):
    input_text = open(file_name, 'r')

    turtle = turtle.Turtle()
    turtle.speed(0)
    window = Turtle.Screen()

    while input_text:
        input_list = input_text.split()
        try:
            turtle.goto(int(input_list[0]), int(input_list[1]))
        except ValueError:
            if (input_list[0] == 'UP\n'):
                turtle.up()
            else:
                turtle.down()
                  
            

main("mystery.txt")
