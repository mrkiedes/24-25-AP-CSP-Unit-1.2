import turtle as trtl

ex = trtl.Turtle()
ex.speed(0)
length = 200
shaded_lines = 100

# Makes a square
for sides in range(4):
    ex.forward(length)
    ex.right(90)

# Setting the color
ex.color("purple")

# Shade the box
for shading in range(shaded_lines):
    ex.penup()
    ex.goto(ex.xcor(), ex.ycor()-int((length/shaded_lines)))
    ex.pendown()
    ex.forward(length)
    ex.backward(length)


wn = trtl.Screen()
wn.mainloop()