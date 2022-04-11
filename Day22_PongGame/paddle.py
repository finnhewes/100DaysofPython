# creates our paddles
from turtle import Turtle

# feel free to change this move distance, but this felt best to me.
MOVE_DISTANCE = 30

# directional headings (degrees on a 360 deg circle)
UP = 90
DOWN = 270

# paddle sizes
LEN = 5
WID = 1.25

# left and right sent to opposite sides of our game board
START_POS_L = (-400, 0)
START_POS_R = (400, 0)


class Paddle(Turtle):
    # takes side input on object creation and sends the paddle to its corresponding side
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=LEN, stretch_wid=WID)
        self.setheading(UP)
        self.color("white")
        if side == "left":
            self.goto(START_POS_L)
        if side == "right":
            self.goto(START_POS_R)

# move paddle in a direction (up or down)
    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

# after a point is scored, the paddles are returned to their starting positions to await the serve.
    def paddle_reset(self, side):
        if side == "left":
            self.goto(START_POS_L)
        if side == "right":
            self.goto(START_POS_R)
