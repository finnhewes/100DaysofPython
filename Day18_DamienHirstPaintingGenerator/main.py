from color_gen import tupled_list
from turtle import Turtle
from random import randint
from turtle import Screen

# init our "pen" Turtle object, importing our colors list from our color_gen file
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setx(-200)
tim.sety(-250)
screen = Screen()
colors = tupled_list
screen.colormode(255)

# makes a row of dots, the length of which is determined by the "times" input... 9 "times" gives you a row with 9 dots...
def dot_fn (times):
    for each in range (0,times):
        tim.dot(20, colors[randint(0, len(colors)-1)])
        # using 50px as my intra-dot spacing. feel free to change this to suit your preference
        tim.forward(50)

# the "two rows" function uses the above function to create two rows, stacked on top of each other the first row heads right, 
# our cursor will "turn on its heels", and make another row headed in the opposite direction, and return itself to the side and 
# heading it originated from tworows, as above, takes "times" as an input. 5 "times" will yield 10 rows in our final image
def tworows(times):
    for each in range (0, times):
        dot_fn(9)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        dot_fn(9)
        tim.right(90)
        tim.forward(50)
        tim.right(90)

# running our function
tworows(5)

# keeping window open until exited, so we can create and admire our beautiful contemporary painting
screen.exitonclick()
