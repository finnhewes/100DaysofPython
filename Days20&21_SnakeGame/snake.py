# generating our snake object
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# move distance below can be toggled with, but this seemed the most natural to me
MOVE_DISTANCE = 20

# the directions below are "set-heading" values (degrees in a circle). I'm setting them here as directional variables to
# make it less confusing for myself later on.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        #   this empty list will "catch" all of our segments as we add them
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    # creating a new snake by adding segments from the starting position list above
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # creating the motion mechanics by having the head move, and then have each segment move to the previous position
    # of the segment "ahead" of itself. sort of the way a worm moves, by "scrunching" itself forward.
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # add a new segment to the end of our snake by appending it to the segments list we created above
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # lengthen our snake by calling the function above to be called each time it "eats" a piece of food.
    def extend(self):
        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()
        self.add_segment((last_x, last_y))

    # setting up directional info below
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # reset snake flings the existing snake off into a black hole/mass grave off of the map, and generates a new snake
    # in the original starting position. people will never know about the massive pile of bodies accumulating just off
    # the side of the map... dad, can you check the closet one more time?
    def reset_snake(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
