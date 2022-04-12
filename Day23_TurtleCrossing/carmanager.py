# generates and manages our cars
from turtle import Turtle
from random import choice, randint

# feel free to replace with any colors you like
color_list = ["crimson", "red", "pink", "deeppink", "darkorange", "gold", "goldenrod", "lavender",
              "thistle", "blueviolet", "purple", "darkslateblue", "olive", "lightseagreen", "lightblue", "royalblue",
              "wheat", "saddlebrown", "mistyrose"]
# move distance determines the starting speed of the cars. They'll speed up after each successful crossing/level-up
MOVE_DISTANCE = 5
# rand increment determines spacing between randomly generated cars. Higher numbers make them more sparse,
# lower numbers, more densly packed
RAND_INCREMENT = 10
# this y list corresponds with the center of the lanes we've established. we'll base our cars' vertical placement on this
Y_LIST = [220, 110, 0, -110, -220]


# car object generator
class CarManager:
    def __init__(self):
        # empty list to "catch" our cars as they're created
        self.all_cars = []

    def create_car(self):
        # choose a random lane to place the car in
        random_y = choice(Y_LIST)
        # basically a "dice roll" with a 10 sided die. Cars are only created when a 1 is "rolled". Gives us some breathing
        # room between cars, but lets us avoid uniform generation patterns
        random_chance = randint(1, RAND_INCREMENT)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2.5, stretch_wid=1.5)
            new_car.penup()
            new_car.color(choice(color_list))
            for i in self.all_cars:
                # detects distance from previously generated cars, and gives the newly generated cars a slight offset,
                # so that they aren't "stacked" on top of each other
                if new_car.distance(i) < 25:
                    # gave them a little bit of y axis variation, so they're not always in the dead center of their lane
                    new_car.goto(400, random_y+(randint(-50, 50)))
                else:
                    new_car.goto(400, random_y)
            # add our newly generated car to the list of cars we've created
            self.all_cars.append(new_car)

    # moves our cars forward y the predetermined move distance (basically, speed)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

    # lets us stop all of our cars at once. useful when game is over.
    def stop_cars(self):
        for car in self.all_cars:
            car.forward(0)

    # increased the move distance (speed) of all of our cars. we'll call this after each successful crossing/level up
    def inc_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += 5
