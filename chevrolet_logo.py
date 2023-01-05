import turtle

win = turtle.Screen()
win.title("Chevrolet")
win.bgcolor("#112C55")

t = turtle.Turtle()
t.pencolor#202124")
t.pensize(10)
length = 150
t.penup()
t.setposition(-length/2, length)
t.pendown()
t.begin_fill()
t.forward(length)
t.right(90)
t.forward(length/3)
t.left(90)
t.forward(length)
t.right(105)
t.forward(length/2)
t.right(75)
t.forward(length-15)
t.left(90)
t.forward(length/3)
t.right(90)
t.forward(length)
t.right(90)
t.forward(length/3)
t.left(90)
t.forward(length)
t.right(105)
t.forward(length/2)
t.right(75)
t.forward(length-15)
t.left(90)
t.forward(length/3)
t.color("#F2D988")
t.end_fill()

turtle.done()