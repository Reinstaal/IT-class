import turtle

turtle.Screen()
turtle.width(3)
turtle.bgcolor('white')
turtle.up()
turtle.goto(-200, 200)
turtle.down()
turtle.speed(0)


for i in range(4):
    for j in range(4):
        turtle.color('black')
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(40)
            turtle.right(90)
        turtle.forward(40)
        turtle.end_fill()
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(40)
            turtle.right(90)
        turtle.forward(40)
        turtle.color('grey')
        turtle.end_fill()
    turtle.color('black')
    turtle.backward(320)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)

    for j in range(4):
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(40)
            turtle.right(90)
        turtle.forward(40)
        turtle.color('grey')
        turtle.end_fill()
        turtle.color('black')
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(40)
            turtle.right(90)
        turtle.forward(40)
        turtle.end_fill()
    turtle.color('black')
    turtle.backward(320)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
turtle.done()