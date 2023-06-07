from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up",)
screen.onkey(fun=snake.down, key="Down",)
screen.onkey(fun=snake.left, key="Left",)
screen.onkey(fun=snake.right, key="Right",)

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
# segment_1.penup()
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.penup()
# segment_2.goto(x=-20, y=0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.penup()
# segment_3.goto(x=-40, y=0)
# screen.update()
# xcor = 0
# for _ in range(3):
#     segment_1 = Turtle(shape="square")
#     segment_1.color("white")
#     segment_1.setx(xcor)
#     xcor -= 20

# segments = [segment_1, segment_2, segment_3]

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

#     Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


#     detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()





























screen.exitonclick()