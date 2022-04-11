from turtle import Screen
from box import Box
from snake import Snake
from food import Food
from midprompts import Midprompts
import time
from scoreboard import Score

# basic window setup/styling
screen = Screen()
screen.setup(width=630, height=630)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initializing classes constructed in other files
box = Box()
box.run()
prompts = Midprompts()
snake = Snake()
food = Food()
scoreboard = Score()

# detect keystrokes
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# creating a loop with this truthy statement so that I can easily separate the start sequence and run it just once,
# upon starting a new game
new_game = True

# game loop
game_is_on = True
while game_is_on:
    # run start sequence on new game, and immediately "turn it off", so it runs just once
    if new_game:
        prompts.start_sequence()
        new_game = False
        # refresh screen and scoreboard, as well as snake movements, after a .1 sec delay. gives the game a "playable"
        # user experience, not too slow, not too fast, with a constantly updated scoreboard.
    screen.update()
    time.sleep(.1)
    snake.move()
    scoreboard.refresh()

    # detect collision with food,
    if snake.head.distance(food) < 15:
        # make new food appear
        food.new_piece()
        # extend snake by 1 piece
        snake.extend()
        # score increase
        scoreboard.score += 1
        scoreboard.refresh()

    # detect collision with wall, game over!
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_sb()
        snake.reset_snake()
        new_game = True

    # detect collision with tail; if head collides with any segment in the tail, game over sequence is triggered
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_sb()
            snake.reset_snake()
            new_game = True

    # keeps window open until exited, so game can run.
screen.exitonclick()
