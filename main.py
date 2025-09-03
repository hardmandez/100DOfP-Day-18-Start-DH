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
t.speed("fastest")

#set grid elements
columns = 0
rows = 0

#extract 8 colours from an image.
colours = colorgram.extract("img.png",8)

#get square size
print(t.position())
square_size = int(input("Enter the square size: "))
square_spacing = int(input("Enter the square spacing: "))

def calculate_start(square_size, square_spacing):
    sq_length = (square_spacing * square_size)/2
    sq_x_start = 0.00 - sq_length
    sq_y_start = 0.00 - sq_length
    return sq_x_start, sq_y_start

def random_color():
    r_colour = random.randint(0, 255)
    g_colour = random.randint(0, 255)
    b_colour = random.randint(0, 255)
    return r_colour, g_colour, b_colour

def print_row(hops, hop_size):
    for _ in range(1,hops):
        t.penup()
        t.dot(5, random_color())
        t.forward(hop_size)

def new_row():
    t.penup()
    print(t.heading)
    t.dot(5, random_color())

def new_row(hop_size):
    print(t.heading())
    if (t.heading() == 0.0):
        t.setheading(90)
        t.dot(5, random_color())
        t.forward(hop_size)
        t.setheading(180)
    else:
        t.setheading(90)
        t.dot(5, random_color())
        t.forward(hop_size)
        t.setheading(0)
t.penup()
t.setposition(calculate_start(square_size, square_spacing))

for i in range(1,square_size):
    print(t.position())
    print_row(square_size, square_spacing)
    new_row(square_spacing)

screen.listen()
screen.exitonclick()