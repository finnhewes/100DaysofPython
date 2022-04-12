# scoreboard is displayed at the top of our screen, and tells us which level we're on
from turtle import Turtle
ALIGNMENT = "center"
# feel free to change the font to suit your preferences
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.score = 0
        # feel free to change the color to suit your preferences
        self.color("crimson")

    # initialize scoreboard
    def begin(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Game over sequence, to be triggered if/when our hero is smushed by a car.
    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", align=ALIGNMENT, font=FONT)

    # update scoreboard
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
