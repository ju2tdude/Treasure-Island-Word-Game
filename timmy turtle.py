import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

timmy_turtle = Turtle()
timmy_turtle.shape("arrow")
timmy_turtle.shapesize(0.75)
timmy_turtle.speed(100)

""""" DRAWING OF A BROKEN LINE """


# # for _ in range(10):
# #     timmy_turtle.forward(10)
# #     timmy_turtle.penup()
# #     timmy_turtle.forward()
#     timmy_turtle.pendown()


""""" MY CODE FOR GENERATING A POLYGON """


# for _ in range (3):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(120)
#     timmy_turtle.color("black")
# for _ in range (4):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)
#     timmy_turtle.color("blue")
# for _ in range (5):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(72)
#     timmy_turtle.color("cyan")
# for _ in range (6):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(60)
#     timmy_turtle.color("green")
# for _ in range (7):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(51.43)
#     timmy_turtle.color("yellow")
# for _ in range (8):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(45)
#     timmy_turtle.color("red")
# for _ in range (9):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(40)
#     timmy_turtle.color("purple")
# for _ in range (10):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(36)
#     timmy_turtle.color("pink")


""""" POLYGON FROM TRIANGLE TO DECAGON """


# def shape(sides):
#     angle = 360/sides
#     for _ in range (sides):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)
#
#
# for sides in range(3, 11):
#     shape(sides)


"""""RANDOM COLOR GENERATION"""


# def color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
# direction = ["90", "180", "270", "360"]
# while True:
#     timmy_turtle.pensize(15)
#     timmy_turtle.color(color())
#     a = int(random.choice(direction))
#     timmy_turtle.right(a)
#     timmy_turtle.forward(20)

"""""GENERATING RANDOM COLORED SPIROGRAPH"""


# def color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for _ in range (36):
#     timmy_turtle.color(color())
#     timmy_turtle.right(10)
#     timmy_turtle.circle(100)


def color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


global y
y = 0
for _ in range(10):
    y += 30

    def start():
        for _ in range(10):
            timmy_turtle.penup()
            timmy_turtle.forward(50)
            timmy_turtle.dot(20, color())
            timmy_turtle.pendown()

    start()
    timmy_turtle.penup()
    timmy_turtle.goto(0, y)
    timmy_turtle.color("white")

screen = Screen()
screen.exitonclick()