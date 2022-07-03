from shutil import move
from turtle import Turtle, Screen, right

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def turn_back():
    tim.back(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_back, key='s')
screen.onkey(fun=clear_screen, key='c')


screen.exitonclick()







# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# def turn_left():
#     tim.left(90)


# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.onkey(key="m", fun=turn_left)

# screen.exitonclick()



