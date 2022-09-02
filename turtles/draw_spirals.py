import shapes as s
from random import randint

def draw_spiral(a_turtle, length, length_increase, angle, number_of_legs):
    """a_turtle draws a spiral starting from lenght, and chaing angle"""
    colors = ["green", "red", "blue", "purple"]

    for leg in range(number_of_legs):
        color = colors[randint(0, len(colors)-1)]
        a_turtle.color(color)
        a_turtle.forward(length)
        a_turtle.right(angle)
        length += length_increase


window = s.make_a_window("black")
jess = s.make_a_turtle("green", "turtle", 3)
draw_spiral(a_turtle=jess, length=10, length_increase=5, angle=91, number_of_legs=90)
s.stop_drawing(window)