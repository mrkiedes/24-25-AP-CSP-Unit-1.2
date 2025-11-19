# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

pixel_size = 20
distance = 3
# TODO: move turtles across and down screen, stopping for collisions
for step in range(20):
    print(step)
	# For each vertical turtle
    for vt in vert_turtles:
        # For each horizontal turtle
        for ht in horiz_turtles:
            # Move each forward
            ht.forward(distance)
            vt.forward(distance)

            # Speed
            distance += 1

            # Check the speed
            if distance > 10:
                distance = 3

            # if they collide
            if abs(ht.xcor() - vt.xcor()) < pixel_size:
                if abs(ht.ycor() - vt.ycor()) < pixel_size:
                    # Turn it gray and change the shape
                    ht_color = ht.fillcolor()
                    vt_color = vt.fillcolor()
                    ht_shape = ht.shape()
                    vt_shape = vt.shape()

                    ht.fillcolor("gray")
                    vt.fillcolor("gray")

                    ht.shape("classic")
                    vt.shape("classic")

                    ht.back(10)
                    vt.back(20)

                    vt.shape(vt_shape)
                    ht.shape(ht_shape)
                    ht.fillcolor(ht_color)
                    vt.fillcolor(vt_color)

                    '''
                    # Remove the turtle from the list
                    horiz_turtles.remove(ht)
                    vert_turtles.remove(vt)
                    '''
for turtle in horiz_turtles:
    turtle.fillcolor("violet")
for turtle in vert_turtles:
    turtle.fillcolor("violet")

wn = trtl.Screen()
wn.mainloop()