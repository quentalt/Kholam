import turtle
import random

def draw_kolam_pattern(size, depth):
    if depth == 0:
        return

    for _ in range(4):
        turtle.forward(size)
        draw_kolam_pattern(size / 2, depth - 1)
        turtle.backward(size)
        turtle.right(90)

def draw_random_kolam():
    turtle.speed(100)
    turtle.pensize(2)

    # Définir les positions de départ de plusieurs motifs Kolam
    start_positions = [(-200, 200), (200, 200), (-200, -200), (200, -200), (0, 0)]

    for pos in start_positions:
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()

        size = random.randint(50, 100)
        depth = random.randint(3, 6)
        turtle.color(random.choice(["red", "blue", "green", "purple", "orange", "black", "brown", "pink", "yellow", "cyan"]))
        
        draw_kolam_pattern(size, depth)

    turtle.hideturtle()
    turtle.done()

draw_random_kolam()
