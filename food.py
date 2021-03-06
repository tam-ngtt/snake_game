from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("green")
        self.speed("fastest")
        self.random_pos()

    def random_pos(self):
        x = random.uniform(-250, 250)
        y = random.uniform(-250, 250)
        return self.goto(x, y)
