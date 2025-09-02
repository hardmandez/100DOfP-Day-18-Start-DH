import random
import colorgram
from turtle import Turtle, Screen
#set common screen elements
screen = Screen()
screen.setup(800, 600)
screen.colormode(255)

#set turtle elements
t = Turtle()
t.pensize(10)

#set grid elements
columns = 0
rows = 0

#extract 8 colours from an image.
colours = colorgram.extract("img.png",8)

#get square size
square_size = int(input("Enter the square size: "))
print(square_size)
def random_color():
    r_colour = random.randint(0, 255)
    g_colour = random.randint(0, 255)
    b_colour = random.randint(0, 255)
    return r_colour, g_colour, b_colour

def print_row(hops):
    for _ in range(1,hops):
        t.penup()
        t.dot(5, random_color())
        t.forward(20)

def new_row():
    print(t.heading())
    if (t.heading() > 0.0):
        t.setheading(180)
        t.forward(20)
    else:
        t.setheading(270)
        t.forward(20)

print_row(square_size)
new_row()

screen.listen()
screen.exitonclick()