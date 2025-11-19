import turtle as trtl

wn = trtl.Screen()
wn.colormode(255)
ex = trtl.Turtle()
ex.speed(0)
length = 200
shaded_lines = 20


# Makes a square
for sides in range(4):
    ex.forward(length)
    ex.right(90)

# Setting the color
r = 91
g = 11
b = 247
ex.pencolor(r,g,b)

# Shade the box
for shading in range(shaded_lines):
    ex.penup()
    ex.goto(ex.xcor(), ex.ycor()-int((length/shaded_lines)))
    ex.pendown()
    ex.forward(length)
    ex.backward(length)
    if g < 245:
        g += 10
    else:
        g = 11
    ex.pencolor(r,g,b)



wn.mainloop()