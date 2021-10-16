from turtle import Turtle, Screen
from random import randint, choice
import heroes

tim = Turtle()

tim.shape("turtle")

screen = Screen()
screen.colormode(255)

direction = [0, 90, 180, 270]

# count = 0
# while count < 4:
#     tim.forward(100)
#     tim.right(90)
#     count += 1
#

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

def draw_shape(num):
    angle = 360/num
    for _ in range(num):
        tim.forward(100)
        tim.right(angle)

def draw_random_walk():
    tup = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.pencolor(tup)
    tim.forward(25)
    tim.setheading(choice(direction))

shape = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}

# tim.pencolor("Blue")
# for _ in range(100):
#     if _ % 2 == 0:
#         tim.pendown()
#         tim.forward(5)
#     else:
#         tim.penup()
#         tim.forward(5)
tim.speed(10)
tim.pensize(10)
# for keys in shape:
#     tup = (randint(0, 255), randint(0, 255), randint(0, 255))
#     tim.pencolor(tup)
#     # tim.pencolor("red")
#     draw_shape(shape[keys])

for _ in range(200):
    draw_random_walk()


print(tim.speed())
print(tim.pensize())
screen.exitonclick()
