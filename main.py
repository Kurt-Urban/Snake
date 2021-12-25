from turtle import Screen
import time

from snake import Snake
from food import Food
from score import Scoreboard

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snek")
s.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
s.listen()

s.onkeypress(snake.left, "Left")
s.onkeypress(snake.right, "Right")
s.onkeypress(snake.up, "Up")
s.onkeypress(snake.down, "Down")

game_running = True

food.create_food()


while game_running:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.create_food()
        snake.add_segment()
        scoreboard.update_score()

    for segment in snake.segments:
        if (
            snake.segments.index(segment) != 1
            and segment.distance(snake.head) < 10
            and segment != snake.head
        ):
            game_running = False
            scoreboard.game_over()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_running = False
        scoreboard.game_over()

s.exitonclick()
