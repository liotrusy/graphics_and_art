from shapes import *
from random import randint

window = make_a_window("black")
jess = make_a_turtle(color="hotpink", shape="turtle", pen_size=3)
jess.speed(3)

size = 50
colors = ["hotpink", "blue", "green", "yellow", "purple"]

for dimension in range(5):
    shape_color = colors[randint(0, len(colors)-1)]
    jess.color(shape_color)

    for square in range(12):
        draw_a_polygon(jess, 4, size)
        move_turtle(jess, 0, 0, 30)
    size += 20

    

stop_drawing(window)