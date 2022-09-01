import turtle as t

def draw_star(length: int):
    angle = 72
    change = 180 - angle / 2

    pointer.right(angle)
    pointer.forward(length)

    for points in range(4):
        pointer.right(change)
        pointer.forward(length)
    
    pointer.right(angle)

    return 0

#
wn = t.Screen()
wn.bgcolor("black")
wn.title("Drawing a star")

#
pointer = t.Turtle()
pointer.color("red")
pointer.shape("classic")
pointer.pensize(3)
pointer.penup()
pointer.goto(0,200)
pointer.pendown()

draw_star(300)

wn.mainloop()





