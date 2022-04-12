ur hero is our main character: the little turtle guy we're controlling
from turtle import Turtle

# our hero's move distance is effectively his speed. Feel free to alter this, but I've found 20 to be a good amount.
MOVE_DISTANCE = 20


class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        #       hero styling
        self.shape("turtle")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.setheading(90)
        self.color("forestgreen")

    # returns our hero to his starting position. we'll call this after each successful crossing/level-up
    def go_home(self):
        self.goto(0, -315)
        self.setheading(90)

    # the following are our movement commands, to be linked to keystrokes. pretty self-explanatory. setheading refers to
    # degrees in a 360-degree circle
    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def turn_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def turn_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
