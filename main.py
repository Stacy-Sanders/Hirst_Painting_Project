from turtle import Turtle, Screen, colormode
from random import choice

# 10 x 10 grid of dots, 20 in size, 50 paces apart
tommy = Turtle()
# tommy.shape("circle")

colormode(255)

color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12),
              (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177),
              (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26),
              (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202),
              (238, 64, 34), (71, 10, 28)]

# start_y = -300
# tommy.penup()
# tommy.setpos(-250, -300)
# tommy.stamp()
# mode()
# for j in range(10):
#     for i in range(10):
#         tommy.color(choice(color_list))
#         tommy.dot(20)  # tommy.stamp()
#         tommy.penup()
#         tommy.fd(50)
#         tommy.sety(start_y + 10)

# for i in range(10):
#     tommy.color(choice(color_list))
#     tommy.dot(20)
#     tommy.penup()
#     tommy.fd(50)
#     tommy.penup()
#
# tommy.setpos(-250, -270)
# for i in range(10):
#     tommy.color(choice(color_list))
#     tommy.dot(20)
#     tommy.penup()
#     tommy.fd(50)


def hirst_painting(turtle):
    turtle.speed("fastest")
    y = -350
    turtle.penup()
    for k in range(10):
        y += 50
        turtle.setpos(-250, y)
        for j in range(10):
            turtle.color(choice(color_list))
            turtle.dot(20)
            turtle.penup()
            turtle.fd(50)
            turtle.penup()
    turtle.color("white")


hirst_painting(tommy)


# tommy.dot(4, choice(color_list))

screen = Screen()
screen.exitonclick()