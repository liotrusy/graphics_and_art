import turtle as t

input("Premi invio per ricevere il tuo messaggio...")

wn = t.Screen()
wn.title("Sorpresa per te!")
wn.bgcolor("black")

pumbi = t.Turtle()
pumbi.shape("turtle")
pumbi.color("red")
pumbi.pensize(4)

# start position
pumbi.penup()
pumbi.goto(-100,-30)
pumbi.pendown()

# draw letter T
pumbi.left(90)
pumbi.forward(50) # all hight 50
pumbi.right(90)
pumbi.forward(15)
pumbi.backward(30)
pumbi.forward(15)
pumbi.right(90)
pumbi.forward(50)
pumbi.left(90)

pumbi.penup()
pumbi.forward(30)
pumbi.pendown()

# draw letter I
pumbi.left(90)
pumbi.forward(50)
pumbi.backward(50)
pumbi.right(90)


pumbi.penup()
pumbi.forward(40)
pumbi.pendown()

# draw letter A
pumbi.left(90)
pumbi.forward(50)

pumbi.right(90)
pumbi.forward(30)

pumbi.right(90)
pumbi.forward(20)
pumbi.right(90)

pumbi.forward(30)
pumbi.backward(30)

pumbi.left(90)
pumbi.forward(30)
pumbi.left(90)

# 
pumbi.penup()
pumbi.forward(25)
pumbi.pendown()

# draw letter M
pumbi.left(90)
pumbi.forward(50)
pumbi.right(120)
pumbi.forward(20)
pumbi.left(60)
pumbi.forward(20)
pumbi.right(120)
pumbi.forward(50)
pumbi.left(90)

# 
pumbi.penup()
pumbi.forward(25)
pumbi.pendown()

# draw letter O
pumbi.left(90)
pumbi.forward(50)
pumbi.right(90)
pumbi.forward(30)
pumbi.right(90)
pumbi.forward(50)
pumbi.right(90)
pumbi.forward(30)
pumbi.right(180)

# 
pumbi.penup()
pumbi.forward(50)
pumbi.pendown()

# Draw exclamation point
pumbi.left(90)
pumbi.penup()
pumbi.forward(25)
pumbi.pendown()
pumbi.forward(35)
pumbi.right(180)
pumbi.forward(35)
pumbi.penup()
pumbi.forward(25)
pumbi.pendown()
pumbi.left(180)

wn.mainloop()