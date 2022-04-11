# draws the "net" across the midline of the game board
from turtle import Turtle

GAP_SIZE = 40


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)
        self.width = 5

    def draw(self, num_times):
        for each in range(num_times):
            self.pendown()
            self.forward(GAP_SIZE)
            self.penup()
            self.forward(GAP_SIZE)
