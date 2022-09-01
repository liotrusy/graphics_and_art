import turtle as t

def draw_shape(number_of_sides:int, length: int):
    turn = 360 / number_of_sides
    for side in range(number_of_sides):
        pointer.forward(length)
        pointer.left(turn)
    return 0

number_of_sides = int(input("Please type the number of sides: "))
length = int(input("Please type the length of each side: "))


wn = t.Screen()
wn.bgcolor("black")
wn.title("A simple square")

pointer = t.Turtle()
pointer.color("red")
pointer.shape("turtle")
pointer.pensize(5)


draw_shape(number_of_sides, length)
wn.mainloop()



    