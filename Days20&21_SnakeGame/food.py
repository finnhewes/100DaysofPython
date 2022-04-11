# generating "food" in random positions in our game box
from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # pen up keeps the turtle object from tracing a line as it moves to it's designated position
        self.penup()
        # styling the food
        self.shape("circle")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("Crimson")
        self.speed("fastest")
        self.new_piece()

        # generating a new random piece
    def new_piece(self):
        # sending the food to a random position (within the game box)
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)
        
