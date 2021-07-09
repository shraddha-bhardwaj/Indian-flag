# INDIAN FLAG
import turtle

flag = turtle.Turtle()

flag.speed(4)
flag.pensize(6)
flag.color('#000080')


def draw(x, y):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()


# This loop is for Ashoka Chakra
for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)
draw(0, -80)
flag.circle(80, 360)

draw(0, -90)

# Green Rectangle
flag.color('#138808')
flag.begin_fill()

flag.forward(400)
flag.backward(800)
flag.right(90)
flag.forward(250)
flag.left(90)
flag.forward(800)
flag.left(90)
flag.forward(250)
flag.left(90)

flag.end_fill()


# Orange Rectangle
flag.color('#FF9933')
draw(-400, 90)

flag.begin_fill()

flag.right(180)
flag.forward(800)
flag.left(90)
flag.forward(250)
flag.left(90)
flag.forward(800)
flag.left(90)
flag.forward(250)

flag.end_fill()

flag.hideturtle()

turtle.done()
