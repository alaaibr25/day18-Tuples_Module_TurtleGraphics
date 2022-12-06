# ---------(1) 3-12-2022 Day18 TurtleGraphics ---------#
# ---------(1) Turtle Graphics ---------#
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.color("DarkSeaGreen4")

# 1#🟠 challenge - Draw a Square:
for n in range(4):
    tim.forward(100)
    tim.right(90)    #90 degrees

# 2#🟠 Challenge - Draw a Dashed Line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()    #pen is on the paper

# ---------(3) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# 3#🟠 Challenge - Draw a triangle, square, pentagon, hexagon, heptagon,
# octagon, nonagon & decagon
# 360 / 4 = 90  , 360/5 = 72

# tim.shape("arrow")
# colors = ["cyan", "dark sea green", "crimson", "plum","misty rose",  "tomato", "DarkMagenta" ]
#
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)

# ---------(4) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# 4#🟠 Challenge - Draw a Random Walk

# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)    # "fastest"
#
# for _ in range(100):
#     # tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
#
# ---------(5) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# 5#🟠 Challenge - Draw a Random Walk with random colors RGB color
# colormode need turtle module not the object

# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)    # "fastest"
# turtle.colormode(255)
#
# def random_color():
#     """Return a random color using RGB"""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     d = random.randint(0, 255)
#     return (r, g, d)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# ---------(6) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# 6#🟠 Challenge - Draw a Spirograph.

# tim.speed(0)
# turtle.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     d = random.randint(0, 255)
#     return r, g, d
#
#
# def draw_spirograph(size_gap):
#     for _ in range(int(360 / size_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_gap)
#
#
# draw_spirograph(5)
#size_gap : to change the tilt of my circle
# int(360 / size_gap) : 360/ each offset = it will repeat our code many times
#Size_gap : to determine how many times  needs to be drawn. int(360 / size_gap)
#current_heading >> tim.heading()
# change heading >> setheading()
# setting new_heading>> setheading from the current_heading >> .heading()

# ---------(8) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# 8#🟠 Final_Project -


screen.exitonclick()

# ---------(2) ✅3-12-2022 Day18 TurtleGraphics✅ ---------#
# ---------(2) 🟠Import Module🟠 ---------#

# keyword Module name
# 1#🟠 import turtle

# new_turtle = module_name.Class_name()
# tim =turtle.Turtle()

# 2#🟠 from turtle import Turtle

# tim = Turtle()

# 3#🟠 from turtle import *

# 4#🟠 Aliasing MOdules
# keyword + Module name + keyword + alias name
# import turtle as t

# tim = t.Turtle()
# Alias_name : a name that we define.

# 5#🟠 Installing Module
# import heroes
# print(heroes.gen())   #generate a new hero name

# ---------(5)✅ 3-12-2022 Day18 TurtleGraphics✅ ---------#
# **#🟠# Tuple: (1, 3, 8)
# Tuple Carved in Stone, You can't change the values like list
# Tuple is Immutable

# my_tuple = (1, 3, 8)
# print(my_tuple[0])   # =1

# my_tuple[2] = 12   #TypeError

# to change a Tuple, convert it to a list
# list_to_tuple = list(my_tuple)
# list_to_tuple[2] = 12
# print(list_to_tuple)    # = [1, 3, 12]

# ---------(9 read) 3-12-2022 Day18 TurtleGraphics ---------#
# tkinter : Graphical User Interface (GUI)



