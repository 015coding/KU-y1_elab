from turtlelab4 import turtle , check

def draw_square(size):
    for i in range (4):
        turtle.forward(size)
        turtle.left(90)
    

def draw_triangle(size):
    for i in range (3):
        turtle.forward(size)
        turtle.left(120)
        
turtle.left(30)
draw_square(120)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
draw_triangle(120)
