import turtle

window = turtle.Screen()
alex = turtle.Turtle()
alex.color('red', 'yellow')
alex.begin_fill()
while True:
    alex.forward(200)
    alex.left(170)
    if abs(alex.pos()) < 1:
        break
alex.end_fill()

window.exitonclick()