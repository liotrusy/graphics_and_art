from shapes import *

window = make_a_window("green")
jess = make_a_turtle(color="hotpink", shape="turtle", pen_size=3)

for shape in range(5):
    draw_a_polygon(jess, 4, 20)
    move_turtle(jess, 40, 0, 0)

stop_drawing(window)