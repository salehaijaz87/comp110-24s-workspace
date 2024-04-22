
from turtle import Turtle, colormode, done 

leo: Turtle = Turtle()
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)

leo.begin_fill()
i: int = 0
while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1
leo.end_fill()
colormode(255)
leo.color(99, 204, 250)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.speed(50)
leo.hideturtle()



bob: Turtle = Turtle()
side_length: int = 300
 
i: int = 0
while (i < 3):
        bob.forward(side_length)
        bob.left(120)
        i = i + 1
side_length = side_length * 120
done()