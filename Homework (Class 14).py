print('This is the Turtle Program')
import turtle
sc = turtle.Screen()
pen = turtle.Turtle()
sc.bgcolor('Brown')
pen.color('Orange')

for i in range(4):
    pen.forward(100)
    pen.right(90)
turtle.done()