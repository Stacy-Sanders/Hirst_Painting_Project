from turtle import Turtle, Screen, colormode
from random import choice

# 10 x 10 grid of dots, 20 in size, 50 paces apart
tommy = Turtle()
tommy.hideturtle()
tommy.speed("fastest")
# tommy.shape("circle")

colormode(255)

color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12),
              (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177),
              (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26),
              (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202),
              (238, 64, 34), (71, 10, 28)]


def hirst_painting(turtle, rows, columns):
    y = -225
    turtle.penup()
    for k in range(rows):
        turtle.setpos(-225, y)
        for j in range(columns):
            turtle.dot(20, choice(color_list))
            turtle.penup()
            turtle.fd(50)
            turtle.penup()
        y += 50


hirst_painting(tommy, 10, 10)


# tommy.dot(4, choice(color_list))

screen = Screen()
screen.exitonclick()