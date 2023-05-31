# import colorgram
import turtle
import random
from rgb_list import rgb_colors
# rgb_colors = []
# colors = colorgram.extract('20_001.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle, Screen
tim = Turtle()


def start_pos(turtle_name, xcor, ycor):
    turtle_name.penup()
    turtle_name.goto(xcor, ycor)
    turtle_name.pendown()


def dot_10():
    for _ in range(10):
        tim.pencolor(random.choice(rgb_colors))
        tim.dot(50)
        tim.penup()
        tim.fd(65)
        tim.pendown()


tim.speed(0)
tim.hideturtle()
turtle.colormode(255)
xcor = -300
ycor = -275
for color in range(10):
    start_pos(tim, xcor, ycor)
    dot_10()
    ycor += 65









screen = Screen()
screen.exitonclick()
