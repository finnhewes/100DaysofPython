# scoreboard to go on the top of the screen; will keep user score and display high score
from turtle import Turtle
from midprompts import Midprompts

# font styling
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
FONT2 = ("Courier", 32, "normal")

prompts = Midprompts()

# all-time score log (saved as a lightweight txt file). will create a new one if one doesn't yet exist
with open("data.txt") as file:
    high_score = int(file.read())


# scoreboard class
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

        # resets scoreboard; erases current board and starts from scratch.
    def reset_sb(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(f'{self.score}')
            self.highscore = self.score
        prompts.gameover()
        self.score = 0

        # refreshes scoreboard to reflect a new score, and new high score (if any)
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
