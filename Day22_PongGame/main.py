import turtle as t
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Score, Countdown, GameOver
from boundaries import Boundary, GoalLine

# game window setup/styling
screen = t.Screen()
screen.setup(width=1000, height=1000, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

# making the goals for left and right side
lside = GoalLine()
lside.goto(-390, 0)
rside = GoalLine()
rside.goto(390, 0)

# making top and bottom walls
top = Boundary()
top.goto(0, 300)
bottom = Boundary()
bottom.goto(0, -300)

# creating our left and right paddles, the ball and net, and the scoreboard
l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
net = Net()
net.draw(8)
scoreboard = Score()
scoreboard.begin()

# generating countdown and game over objects, but not calling just yet
countdown = Countdown()
game_over = GameOver()

# make screen "listen" for, and detect keystrokes for left and right paddles, and move the paddles accordingly.
screen.update()
screen.listen()
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

# GAME LOOP
game_is_on = True
ball_served = False
while game_is_on:
    # serves the ball only once, to start each point.
    if not ball_served:
        countdown.run()
        ball.serve()
        ball_served = True

    # begins ball moving forward, continuing until it crosses a goal line
    ball.move()
    screen.update()

    # detect collision with wall, and bounces ball off of it
    if ball.ycor() > 300:
        ball.wall_bounce()
    if ball.ycor() < -300:
        ball.wall_bounce()

    # detect collision with paddles, and bounces ball off of them
    if ball.distance(l_paddle) < 60 and -400 < ball.xcor() < -375:
        ball.new_heading()
        ball.movedistance += .2
    if ball.distance(r_paddle) < 60 and 375 < ball.xcor() < 400:
        ball.new_heading()
        ball.movedistance += .2

    # detecting RIGHT SIDE goal line breaches (scores), keep points, return loop
    if ball.xcor() > 425:
        scoreboard.l_score += 1
        scoreboard.refresh()
        # play to 11 points, once a score of 11 is reached by a player, the game is over.
        if scoreboard.l_score == 11:
            game_over.run()
            ball.clear()
            game_is_on = False
        # if score is not 11, game will continue. reset ball and paddles, and serve again.
        else:
            game_is_on = True
            ball_served = False
            ball.home()
            l_paddle.paddle_reset("left")
            r_paddle.paddle_reset("right")

    # detecting LEFT SIDE goal line breaches (scores), keep points, return loop
    if ball.xcor() < -425:
        scoreboard.r_score += 1
        scoreboard.refresh()
        # play to 11 points, once a score of 11 is reached by a player, the game is over.
        if scoreboard.r_score == 11:
            game_over.run()
            ball.clear()
            game_is_on = False
        # if score is not 11, game will continue. reset ball and paddles, and serve again.
        else:
            game_is_on = True
            ball_served = False
            ball.home()
            l_paddle.paddle_reset("left")
            r_paddle.paddle_reset("right")
    # updates screen while game loop is on
    screen.update()

# keep window open, until exited, so game can run
screen.exitonclick()
