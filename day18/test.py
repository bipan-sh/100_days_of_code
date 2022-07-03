import turtle
from turtle import Turtle, Screen, color
import random


tim = Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

#direction = [0, 90, 180, 270]
tim.shape('turtle')

#tim.width(5)
turtle.speed(0)


while current_heading < 360:
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)
    
    
    #tim.position(0.00,240.00)
    
    




screen.exitonclick()

