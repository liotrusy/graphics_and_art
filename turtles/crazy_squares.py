from shapes import *

window = make_a_window("black")
jess = make_a_turtle(color="hotpink", shape="turtle", pen_size=3)
jess.speed(3)

size = 20
for square in range(20):
    
    draw_a_polygon(jess, 4, size)
    move_turtle(jess, -10, -10, 260)
    size += 20

stop_drawing(window)