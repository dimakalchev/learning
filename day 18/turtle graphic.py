from turtle import Turtle, Screen
import random
from random import randint

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


tim = Turtle()
tim.shape("turtle")
tim.color("orange")


def square():
    for i in range(4):
        tim.right(90)
        tim.forward(100)


def intermittent():
    for _ in range(20):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.pendown()
# От треугольника до девятиугольника
# angles = [120, 90, 72, 60, 51.5, 45, 40]
# choice_angle = 0
# figure_angles = 3
# while choice_angle != 6:
#     for _ in range(figure_angles):
#         tim.right(angles[choice_angle])
#         tim.forward(100)
#     choice_angle += 1
#     figure_angles += 1
#     change_color()


def rand_start():
    tim.penup()
    tim.goto(randint(-150, 0), randint(0, 150))
    tim.pendown()

# Random walk
# side_list = [0, 90, 180, 270, 360]
# tim.hideturtle()
# tim.pensize(10)
# tim.speed(0)
# rand_start()
# for _ in range(2000):
#     random_side = random.choice(side_list)
#     tim.setheading(random_side)
#     tim.forward(20)
#     change_color()


def draw_spirograph(size_of_gap):
    tim.hideturtle()
    tim.speed(0)
    rand_start()
    for _ in range(int(360 / size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(13)









screen = Screen()
screen.exitonclick()
