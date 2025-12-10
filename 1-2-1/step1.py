# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"

#-----initialize turtle-----
moewl = trtl.Turtle()
moewl.shape(spot_shape)
moewl.shapesize(spot_size)
moewl.fillcolor(spot_color)

#-----game functions--------
def spot_clicked(x, y):
    print("Hello world!")

#-----events----------------
moewl.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()