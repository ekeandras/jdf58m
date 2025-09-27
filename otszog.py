import turtle

# képernyő beállítás
turtle.setup(800, 600)
turtle.title("Turtle alakzat rajzolás")
turtle.speed(5)

# ötszög rajzolása
sides = 5           # oldalak száma (nem 3 és nem 4)
length = 100        # oldalak hossza
angle = 360 / sides

for _ in range(sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()