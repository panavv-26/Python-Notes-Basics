import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["cyan", "magenta", "yellow", "white"]

for i in range(360):
    t.pencolor(colors[i % 4])
    t.circle(i, 90)
    t.left(90)
    t.circle(i, 90)
    t.left(18)

t.hideturtle()
turtle.done()
