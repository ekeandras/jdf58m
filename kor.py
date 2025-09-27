import turtle


def kor():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.pensize(9)

    for _ in range(1):
        turtle.circle(200)


#App
ablak = turtle.Screen()
ablak.listen()
ablak.onkey(kor, "g")
ablak.onkey(turtle.bye, "a")
ablak.mainloop()
