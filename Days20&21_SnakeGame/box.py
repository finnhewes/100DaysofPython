# Creating the box/walls/borders of the game environment
from turtle import Turtle


class Box(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lime")
        self.penup()
        self.goto(-290, 290)
        self.setheading(0)

    def run(self):
        self.pendown()
        self.forward(140)
        self.penup()
        self.forward(300)
        self.pendown()
        self.forward(140)
        self.setheading(270)
        self.forward(580)
        self.setheading(180)
        self.forward(580)
        self.setheading(90)
        self.forward(580)
        self.penup()
        self.hideturtle()
