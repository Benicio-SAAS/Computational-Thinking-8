import turtle

t = turtle.Turtle()
t.penup()
t.goto (-100, -100)
t.color ("purple")
t.pendown()

for i in range(67):
    t.left(67)
    t.forward(67)
turtle.exitonclick()