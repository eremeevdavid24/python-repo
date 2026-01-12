import turtle

# for i in range(10):
#     turtle.forward(15)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()
#
# turtle.reset()
#
#
# for _ in range(4):
#     turtle.forward(125)
#     turtle.left(90)
#
#
# turtle.reset()

for _ in range(4):
    turtle.forward(200)
    turtle.left(90)

turtle.penup()
turtle.forward(25)
turtle.right(-90)
turtle.forward(25)
turtle.pendown()

for _ in range(4):
    turtle.forward(150)
    turtle.right(90)


turtle.exitonclick()