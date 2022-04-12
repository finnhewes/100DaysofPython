from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def rot_left():
    tim.left(5)

def rot_right():
    tim.right(5)

def clear_drawing():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=rot_left)
screen.onkey(key="d", fun=rot_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()