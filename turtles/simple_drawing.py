import turtle as t

background_color = input("Please enter the background color: ")
alex_color = input("Please enter Alex's color: ")

wn = t.Screen()
wn.bgcolor(background_color)
wn.title("Hello, Alex!")

alex = t.Turtle() # new type imported by module turtle
alex.shape("turtle")
alex.color(alex_color)
alex.pensize(3)

tess = t.Turtle()
tess.shape("turtle")
tess.color("pink")
tess.pensize(5)

alex.forward(50) # dictates the movement
alex.left(90) # dictates the turn
alex.forward(50)
alex.right(90)
alex.forward(50)

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.right(60)
tess.forward(80)

wn.mainloop()