# bringing all of our pieces together!
from turtle import Screen
from hero import Hero
from scoreboard import Score
from carmanager import CarManager
from street import Street, SolidLine, DashedLine, Lane
import time

# setting up our game window
screen = Screen()
screen.screensize(600, 600, "white")
screen.tracer(0)

# setting up our street/game board
def lane_divider(ycor):
    start_x = -400
    for i in range(20):
        new_dash = DashedLine(ycor)
        new_dash.goto(start_x, ycor)
        start_x += 100

def street_setup():
    street = Street()
    top_line = SolidLine(280)
    bottom_line = SolidLine(-280)
    lane1 = Lane(-220)
    lane2 = Lane(-110)
    lane3 = Lane(0)
    lane4 = Lane(110)
    lane5 = Lane(220)
    lane_divider(-165)
    lane_divider(-55)
    lane_divider(55)
    lane_divider(165)

# initializing our created objects
street_setup()
hero = Hero()
hero.go_home()
car_manager = CarManager()
scoreboard = Score()

# making the screen "listen" to detect keystrokes, and move our hero accordingly
screen.listen()
screen.onkey(fun=hero.move_forward, key="Up")
screen.onkey(fun=hero.turn_left, key="Left")
screen.onkey(fun=hero.turn_right, key="Right")
screen.onkey(fun=hero.go_back, key="Down")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    # This won't create a car every .1 seconds, because we've instituted the "dice roll" functionality in the car
    # manager class, which guarantees a car will be generated every second, at a minimum.
    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collisions between cars and our hero. If hero is smushed, he turns red. Cars will stop. Breaks game loop.
    for each in car_manager.all_cars:
        if hero.distance(each) < 30 and (each.ycor() - hero.ycor()) < 20:
            car_manager.stop_cars()
            hero.color("crimson")
            game_is_on = False

    # detecting successful crossings. If our hero makes it to the other side, he'll return to his starting position, the
    # score increases by 1, and our cars speed up slightly.
    if hero.ycor() > 290:
        hero.go_home()
        car_manager.inc_speed()
        scoreboard.score += 1
    screen.update()
    scoreboard.refresh()

# Game over sequence will run when the game loop is broken
scoreboard.game_over()
# Keeps our window open until exited, so game can run successfully
screen.exitonclick()
