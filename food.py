from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)

    def create_food(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
