import turtle

t = turtle.Turtle()

t.goto(-50, -50)
t.speed(10)
turtle.Screen().bgcolor("black")
color = ["Red","Orange","Violet"]
for i in range (600):
    t.color ( color[ i % 3])
    t.forward(83 + i)
    t.left(84)

turtle.exitonclick()