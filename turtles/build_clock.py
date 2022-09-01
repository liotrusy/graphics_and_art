import turtle as t

def draw_clock(radius_blank, tick, spacing):

    dials = 12
    angle = 360 // dials
    for dial in range(dials):

        pointer.right(angle)
        pointer.forward(radius_blank)
        pointer.pendown()
        pointer.forward(tick)
        pointer.penup()
        pointer.forward(spacing)
        pointer.pendown()
        pointer.stamp()
        pointer.penup()
        pointer.backward(radius_blank + tick + spacing)        

    return 0

wn = t.Screen()
pointer = t.Turtle()
pointer.shape("turtle")
pointer.penup()

draw_clock(150, 30, 30)

wn.mainloop()

    

