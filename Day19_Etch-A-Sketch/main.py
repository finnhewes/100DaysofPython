from turtle import Turtle
from turtle import Screen

# tim is our cursor
tim = Turtle()

# screen is our window/drawing pad
screen = Screen()

# self explanatory directional functions below
def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def rot_left():
    tim.left(5)

def rot_right():
    tim.right(5)

# gives us a fresh screen to draw on
def clear_drawing():
    screen.reset()

# prompts the screen to "listen" for our keystrokes, allowing us to control our cursor by pressing the keys listed below.
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=rot_left)
screen.onkey(key="d", fun=rot_right)
screen.onkey(key="c", fun=clear_drawing)

# keeps our window open until we exit, so we can successfully make drawings
screen.exitonclick()
