import random
from turtle import Turtle, Screen

timothy = Turtle()
screen = Screen()
screen.colormode(255)

timothy.shape("turtle")
timothy.color("DarkSeaGreen4")
timothy.hideturtle()
timothy.penup()
timothy.speed("fastest")

# Damien Hirst Spot Painting
def generate_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

current_position = [-200.0, -200.0]
timothy.goto(current_position[0], current_position[1])

for _ in range(10):
    for _ in range(10):
        timothy.dot(20, generate_random_color())
        timothy.forward(50)
    current_position[1] += 50
    timothy.goto(current_position[0], current_position[1])

screen.exitonclick()
