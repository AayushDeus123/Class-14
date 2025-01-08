#Making stars using TURTLE
print('Stars using Turtle')
import turtle
s = turtle.Screen()
p = turtle.Turtle()
s.bgcolor('Aqua')
p.color('Red')

p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)

p.penup()
p.right(150)
p.forward(50)
p.pendown()
p.right(90)

p.forward(100)
p.right(120)
p.forward(100)
p.right(120)
p.forward(100)

p.penup()
p.goto(-100, 100)
p.pendown()
p.color('Blue')

for i in range(5):
    p.forward(100)
    p.right(144)
    
turtle.done()