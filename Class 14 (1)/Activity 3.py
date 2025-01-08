#Making a spiral using TURTLE
import turtle
s = turtle.Screen()
p = turtle.Turtle()
s.bgcolor('Orange')
p.color('Red')

size = 0

while True:
    for i in range(100):
        p.forward(size + 1)
        p.left(90)
        size = size - 5
    size = size + 1
    turtle.mainloop()