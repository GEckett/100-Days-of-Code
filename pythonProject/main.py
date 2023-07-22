import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

#square challenge

#for _ in range(4):
#    timmy.forward(100)
#    timmy.left(90)

#dashed line challenge

#for _ in range(15):
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()
#    timmy.forward(10)

#shapes challenge

#n = 3
#while n < 10:
#    r = round(random.uniform(0.1, 1.0), 2)
#    b = round(random.uniform(0.1, 1.0), 2)
#    g = round(random.uniform(0.1, 1.0), 2)
#    timmy.pencolor(r, b, g)
#    for _ in range(n):
#        timmy.forward(100)
#        timmy.left(360 / n)
#    n += 1

#random walk challenge

#def random_color():
#    r = round(random.uniform(0.1, 1.0), 2)
#    b = round(random.uniform(0.1, 1.0), 2)
#    g = round(random.uniform(0.1, 1.0), 2)
#    timmy.pencolor(r, b, g)

#n = 3
#timmy.speed(10)
#directions = [0, 90, 180, 270]
#while n < 200:
#    random_color()
#    timmy.pensize(10)
#    timmy.setheading(random.choice(directions))
#    timmy.forward(30)
#    n += 1

#spirograph challenge


def random_color():
    r = round(random.uniform(0.1, 1.0), 2)
    b = round(random.uniform(0.1, 1.0), 2)
    g = round(random.uniform(0.1, 1.0), 2)
    timmy.pencolor(r, b, g)


turtle.speed("fastest")
n = 0
while n < 360:
    timmy.left(n)
    random_color()
    timmy.circle(100)
    n += 5



screen = Screen()
screen.exitonclick()





