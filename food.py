import random
from turtle import Turtle
from snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.respawn()
    def respawn(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        self.goto(x, y)



