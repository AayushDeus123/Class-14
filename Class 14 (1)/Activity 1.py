#Making a square in Python using turtle
print('This is the Turtle Program')
import turtle
sc = turtle.Screen()
pen = turtle.Turtle()
sc.bgcolor('Yellow')
pen.color('Red')

for i in range(4):
    pen.forward(100)
    pen.right(90)

pen.penup()
pen.goto(-101 , 101)
pen.pendown()
pen.color('Blue')

for i in range(4):
    pen.forward(100)
    pen.right(90)

turtle.mainloop()