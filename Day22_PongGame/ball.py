# our ball class. contains the ball's mechanics as well.
from turtle import Turtle
from random import randint, choice

# start from dead center
START_POS = (0, 0)

# direction list... "start angle" chooses a random choice from this list of random angles (each within 45 degrees of
# left or right) and sets the angle that the ball will be served to start the point.
d_list = [randint(0, 45), randint(315, 360), randint(135, 180), randint(180, 225)]
START_ANGLE = choice(d_list)

# ball object
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.width = 20
        self.ht = 20
        self.movedistance = 10
        self.penup()
        self.goto(START_POS)
        self.color("white")
        self.speed("normal")

    # serves the ball to start the point. a random choice is made from the list of random directions.
    def serve(self):
        self.setheading(choice(d_list))
        self.forward(self.movedistance)

    # moves the ball forward by our pre-determined amount
    def move(self):
        self.forward(self.movedistance)

    # changes the angle of the ball (if it bounces off of a paddle)
    def new_heading(self):
        if 0 <= self.heading() <= 45:
            self.setheading(randint(135, 225))
            self.speed(randint(1, 10))
            self.move()
        elif 135 <= self.heading() <= 180:
            self.setheading(randint(315, 405))
            self.speed(randint(1, 10))
            self.move()
        elif 180 < self.heading() <= 225:
            self.setheading(randint(315, 405))
            self.speed(randint(1, 10))
            self.move()
        elif 315 <= self.heading() <= 360:
            self.setheading(randint(135, 225))
            self.speed(randint(1, 10))
            self.move()

    # changes the angle of the ball (if it bounces off of a wall)
    def wall_bounce(self):
        if 0 <= self.heading() <= 45:
            self.setheading(360-self.heading())
            self.move()
        elif 135 <= self.heading() <= 180:
            self.setheading(360-self.heading())
            self.move()
        elif 180 < self.heading() <= 225:
            self.setheading(360-self.heading())
            self.move()
        elif 315 <= self.heading() <= 360:
            self.setheading(360-self.heading())
            self.move()
