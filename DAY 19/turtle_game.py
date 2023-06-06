from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make yor bet", prompt="Which turtle will win the race? Enter your color: ?")


def start_pos(turtle_name, xcor, ycor):
    turtle_name.penup()
    turtle_name.goto(xcor, ycor)
    turtle_name.pendown()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
din = Turtle(shape="turtle")
sam = Turtle(shape="turtle")
mandy = Turtle(shape="turtle")
cris = Turtle(shape="turtle")
all_turtles = [tim, tom, din, sam, mandy, cris]
number_of_turtle = 0
for color in colors:
    all_turtles[number_of_turtle].color(color)
    number_of_turtle += 1
ycor = -100
for t in all_turtles:
    start_pos(t, xcor=-220, ycor=ycor)
    ycor += 45
    t.penup()


if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle is the winner")
            else:
                print(f"You lose! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)







screen.exitonclick()