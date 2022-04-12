# our street graphic/game board. Just some extra styling, none of these are functional objects.
from turtle import Turtle

# these refer to the center y-pos of our lanes
Y_LIST = [220, 110, 0, -110, -220]

# this is the "pavement"
class Street(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.home()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_len=100, stretch_wid=29)

# these are the far-side boundaries of the road
class SolidLine(Turtle):
    def __init__(self, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("gold")
        self.shapesize(stretch_wid=.175, stretch_len=100)
        self.goto(0, y_cor)

# these are the dashed lane markers
class DashedLine(Turtle):
    def __init__(self, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=.175, stretch_len=2.5)
        self.goto(0, y_cor)

# this is the worn pavement within the lanes... a slightly lighter tone than the parts of the road that aren't driven over
class Lane(Turtle):
    def __init__(self, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("dimgray")
        self.shapesize(stretch_wid=5, stretch_len=100)
        self.goto(0, y_cor)
