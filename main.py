from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.listen()
# SCREEN TRACER turns off the animation on the screen unless u call screen update function
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
# This object creates the snake body with the desirable segments
snake = Snake(segments=6)
food = Food()
score = Score()
screen.update()


# Loop is to continue the movement of snake until it hits its own body or the box


def move():
    gameIsOn = True

    while gameIsOn:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.respawn()
            score.add()
            snake.extend()
        screen.update()
        time.sleep(0.07)

        # Detect collision with wall
        if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 275 or snake.head.ycor() < -275:
            gameIsOn = False
            score.gameOver()

        # Detect collision with tail
        for segment in snake.snakes[1:]:
            if snake.head.distance(segment)<10:
                gameIsOn = False
                score.gameOver()


screen.onkey(key="z", fun=move)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)

screen.exitonclick()
