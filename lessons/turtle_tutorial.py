"""EX08 work."""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.forward(50)
leo.left(30)
leo.right(40)

i: int = 0  # simplified code 
while (i < 4):
        leo.forward(300)
        leo.left(90)
        i = i + 1

i: int = 0 #exercise 2
while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1
leo.penup()
leo.goto(45, 60)
leo.pendown()
 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.color("blue")
colormode(255)
leo.begin_fill()
    # code for shape to be filled 
leo.end_fill()


done()