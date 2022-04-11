# everyone needs boundaries.
# adds clear boundaries for our game window.
from turtle import Turtle


# upper and lower boundaries... the sides of the table... the ball will bounce off of these
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("teal")
        self.shapesize(stretch_len=100, stretch_wid=1)


# left and right boundaires... the goals... a player scores by hitting the ball into one of these. players defend their
# own goals till the last drop of blood, as true patriots do
class GoalLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        # feel free to change this color to suit your own preferences
        self.color("crimson")
        self.shapesize(stretch_len=1, stretch_wid=29)
