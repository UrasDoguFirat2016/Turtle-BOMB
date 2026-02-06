import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(10)
t.penup()
t.goto(0, -100)
t.pendown()
t.hideturtle()

def draw_a_bomb():
    t.color("black")
    for i in range(100, 0, -1):
        t.circle(i)
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.left(90)
    t.color("red")
    t.forward(30)
    t.left(-25)
    t.color("orange")
    t.forward(30)
    t.left(-25)
    t.color("yellow")
    t.forward(30)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("white")
    t.write("BOOM!", align="center", font=("Arial", 24, "bold"))

draw_a_bomb()
turtle.mainloop()
