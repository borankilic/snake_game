from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0 )


snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.turn_north, "Up")
screen.onkey(snake.turn_south, "Down")
screen.onkey(snake.turn_west, "Left")
screen.onkey(snake.turn_east, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    score_board.update_score()

#    detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        score_board.increase_score()
        snake.extend()

#    detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            score_board.reset()
            snake.reset()



screen.exitonclick()
