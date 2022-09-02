import turtle

def make_a_window(background_color):
    """Creates background_color window with turtle module"""
    window = turtle.Screen()
    window.bgcolor(background_color)

def make_a_turtle(color, shape, pen_size):
    """Create turtle with shape, color and pen_size"""
    pierre = turtle.Turtle()
    pierre.shape(shape)
    pierre.color(color)
    pierre.pensize(pen_size)

def draw_a_polygon(a_turtle, number_of_sides, side_length):
    """A turtle draws a polygon with number_of_sides sides of side_length"""
    # Turtle moves only counterclockwise
    angle_change = 360 / number_of_sides
    for side in range(number_of_sides):
        a_turtle.forward(side_length)
        a_turtle.left(angle_change)

def move_turtle(a_turtle, x_movement, y_movement, angle_change):
    """Move turtle of x_movement and y_movement, in direction angle_change"""
    # direction is always counter clockwise!
    a_turtle.penup()
    a_turtle.forward(x_movement)
    a_turtle.left(angle_change)
    a_turtle.forward(y_change)


