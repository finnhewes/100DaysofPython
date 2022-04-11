# prompts that appear in the middle of the screen
from turtle import Turtle
import time

# general font styling
ALIGNMENT = "center"
FONT2 = ("Courier", 32, "normal")


# prompt class
class Midprompts(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)

        # run at startup, a basic "count-in"
    def start_sequence(self):
        for i in ["3", "2", "1", "GO!"]:
            self.write(f"{i}", align=ALIGNMENT, font=FONT2)
            time.sleep(.75)
            self.clear()

        # run at game over (duh)
    def gameover(self):
        self.write(f"G A M E   O V E R", align=ALIGNMENT, font=FONT2)
        time.sleep(2)
        self.clear()
