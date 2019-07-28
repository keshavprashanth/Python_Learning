import turtle

#bgcolor = input("Enter the background color for the window")

window = turtle.Screen()
#window.bgcolor(bgcolor)   # set the window background color
window.bgcolor("red")
#tess_color = input("Enter the color for turtle")
tess = turtle.Turtle()
#tess.color(tess_color)             # make tess blue
tess.color("blue")

tess.pensize(3)                # set the width of her pen
tess.forward(180)
tess.left(90)
tess.forward(180)


tess1 = tess.clone()
tess1.left(120)
tess1.forward(500)

window.exitonclick()           # wait for a user click on the canvas
