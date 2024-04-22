"""Scenery of a house."""
 
__author__ = "730664950"
 
from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    tod: Turtle = Turtle()
    tod.speed(100)
    tod.hideturtle()
    draw_bottom(tod, -380, -164, 100)
    draw_background(tod, -380, 335, -200)
    draw_drive(tod, -380, -166, 50)
    draw_star(tod, 150, 200, 10)
    draw_star(tod, 200, 20, 10)
    draw_star(tod, 380, 10, 10)
    draw_star(tod, 320, 30, 10)
    draw_star(tod, 245, -70, 10)
    draw_star(tod, -200, 150, 10)
    draw_star(tod, -250, 300, 10)
    draw_star(tod, -300, 230, 10)
    draw_star(tod, -200, 20, 10)
    draw_star(tod, -110, 250, 10)
    draw_star(tod, -350, 100, 10)
    draw_square(tod, 150, -210, -290)
    draw_outer_roof(tod, -176, 40, 370)
    draw_square2(tod, -120, -90, 120)
    draw_square2(tod, -100, 10, 70)
    draw_square2(tod, 40, 10, 70)
    draw_window(tod, 45, 5, 60)
    draw_window(tod, -95, 5, 60)
    draw_square3(tod, 50, -90, 300)
    draw_square4(tod, -280, -55, 100)
    draw_square4(tod, -260, -55, 100)
    draw_tree(tod, -325, -100, 130)
    draw_tree(tod, -325, -70, 130)
    draw_tree(tod, -325, -40, 130)
    draw_tree(tod, -325, -10, 130)
    draw_circle(tod, 230, 200, 100)
    draw_circle(tod, 0, 0, 5)


def draw_bottom(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """The purpose of this function is to create the grass for my image.

    This will draw a rectangle.
    """ 
    colormode(255)
    a_turtle.pencolor(5, 112, 61)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(5, 112, 61)
    a_turtle.pendown()
    i: int = 0
    for i in range(2):
        a_turtle.forward(750)
        a_turtle.right(90)
        a_turtle.forward(200)
        a_turtle.right(90)
    a_turtle.end_fill()


def draw_drive(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """The driveway.""" 
    colormode(255)
    a_turtle.pencolor(154, 143, 143)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(154, 143, 143)
    a_turtle.pendown()
    i: int = 0
    for i in range(2):
        a_turtle.forward(400)
        a_turtle.right(90)
        a_turtle.forward(150)
        a_turtle.right(90)
    a_turtle.end_fill()


def draw_background(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Background sky."""
    colormode(255)
    a_turtle.pencolor(3, 8, 106)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(3, 8, 106)
    a_turtle.pendown()
    i: int = 0
    for i in range(2):
        a_turtle.forward(900)
        a_turtle.right(90)
        a_turtle.forward(500)
        a_turtle.right(90)
        a_turtle.forward(800)
        a_turtle.end_fill()


def draw_star(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Stars in the sky.""" 
    colormode(255)
    a_turtle.pencolor(255, 255, 255)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(255, 255, 255)
    a_turtle.pendown()
    i: int = 0
    while i < 5:
        a_turtle.forward(width)
        a_turtle.right(144)
        i = i + 1
    a_turtle.end_fill()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Main box of house.""" 
    colormode(255)
    a_turtle.pencolor(146, 84, 17)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(146, 84, 17)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_outer_roof(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Roof of my house.""" 
    colormode(255)
    a_turtle.pencolor(141, 12, 12)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(141, 12, 12)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()


def draw_square2(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Garage for house.""" 
    colormode(255)
    a_turtle.pencolor(64, 44, 6)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(64, 44, 6)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_window(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Yellow parts to window.""" 
    colormode(255)
    a_turtle.pencolor(255, 217, 7)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(255, 217, 7)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_square3(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Door for house.""" 
    colormode(255)
    a_turtle.pencolor(64, 44, 6)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(64, 44, 6)
    a_turtle.pendown()
    for _ in range(2):  
        a_turtle.forward(60)
        a_turtle.right(90)
        a_turtle.forward(120)
        a_turtle.right(90)
    a_turtle.end_fill()


def draw_square4(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Tree trunk.""" 
    colormode(255)
    a_turtle.pencolor(64, 44, 6)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(64, 44, 6)
    a_turtle.pendown()
    i: int = 0  
    while i < 2:
        a_turtle.forward(20)
        a_turtle.right(90)
        a_turtle.forward(110)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()

 
def draw_tree(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Leaves of the tree.""" 
    colormode(255)
    a_turtle.pencolor(93, 138, 12)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(93, 138, 12)
    a_turtle.pendown()
    for _ in range(3):
        a_turtle.forward(width)
        a_turtle.left(120)
    a_turtle.end_fill()


def draw_circle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Stars in the sky.""" 
    colormode(255)
    a_turtle.pencolor(255, 255, 255)
    a_turtle.begin_fill()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.fillcolor(255, 255, 255)
    a_turtle.pendown()
    r = 50
    a_turtle.circle(r)
    a_turtle.end_fill()
    done()


if __name__ == "__main__":
    main()