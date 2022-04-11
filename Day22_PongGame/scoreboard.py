# keeps score for our game
from turtle import Turtle
import time
# font styling
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 48, "normal")


# scoreboard object to be displayed at all times
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    # start our scoreboard
    def begin(self):
        self.goto(-200, 360)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(200, 360)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)
        self.refresh()

    # updates the scoreboard with the current scores
    def refresh(self):
        self.clear()
        self.goto(-200, 360)
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(200, 360)
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)


# game over object to be displayed when we have reached end game
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")

    def run(self):
        self.goto(0, 0)
        self.write(f"G A M E   O V E R", align=ALIGNMENT, font=FONT)


# countdown, to be displayed at the beginning of the game and before each serve
class Countdown(Turtle):
    def __init__(self):
        # styling
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    # runs countdown
    def run(self):
        self.write("3", align=ALIGNMENT, font=FONT2)
        time.sleep(.5)
        self.clear()
        self.write("2", align=ALIGNMENT, font=FONT2)
        time.sleep(.5)
        self.clear()
        self.write("1", align=ALIGNMENT, font=FONT2)
        time.sleep(.5)
        self.clear()
        self.write("GO!", align=ALIGNMENT, font=FONT2)
        time.sleep(.5)
        self.clear()
