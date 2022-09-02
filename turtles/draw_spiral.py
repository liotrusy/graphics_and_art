import turtle
from random import randint

def draw_multicolor_square(a_turtle, number_of_sides, side_size):
    """A turtle draws a multicolor polygon of number_of_sides of side_size"""
    colors = ["red", "green", "blue", "purple", "hotpink"] # 5 colors option
    angle_change = 360 / number_of_sides

    for side in range(number_of_sides):
        a_turtle.color(colors[randint(0, len(colors)-1)]) # randint includes
        a_turtle.forward(side_size)
        a_turtle.left(angle_change)
    
    return 1

def draw_spiral(number_of_shapes, pen_size, number_of_sides, side_size, increase_fator, spin):
    """Draw a spiral"""
    window = turtle.Screen()
    window.bgcolor("black")

    pierre = turtle.Turtle()
    pierre.speed(10)
    pierre.pensize(pen_size)

    background_colors = ["black", "grey", "white", "yellow"]

    for spiral_point in range(number_of_shapes):
        draw_multicolor_square(pierre, number_of_sides, side_size)
        window.bgcolor(background_colors[randint(0, len(background_colors)-1)])
        side_size += increase_fator
        pierre.forward(increase_fator)
        pierre.right(spin)

    window.bgcolor("black")

    window.mainloop()

    return 1


draw_spiral(number_of_shapes=30, pen_size=3, number_of_sides=7, side_size=20, increase_fator=10, spin=10)
