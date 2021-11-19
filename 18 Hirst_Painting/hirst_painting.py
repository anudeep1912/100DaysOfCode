import turtle as t
import random
import colorgram


def hirst_colors():
    colors = colorgram.extract("hirst_image.jpg", 20)
    color_list = []
    for color in colors:
        color_list.append(color.rgb)
    return color_list[1:]


def choose_colour():
    random_colour = random.choice(hirst_colors())
    return random_colour


"""Note: extracting color list from image every loop for a hundred dots is making the code very slow. 
So using the Color list from an already generated file from image file."""
color_list1 = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
               (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
               (13, 99, 71),
               (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
               (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
               (176, 192, 209)]


tim = t.Turtle()
tim.speed(10)
t.delay(0)
t.colormode(255)
tim.penup()
tim.hideturtle()


rows = 50
tim.setheading(225)
tim.forward((rows/2)*25)
tim.setheading(0)
number_of_dots = rows*rows
for dot_number in range(1, number_of_dots + 1):
    tim.dot(10, random.choice(color_list1))
    tim.forward(20)
    if dot_number % rows == 0:
        tim.setheading(90)
        tim.forward(20)
        tim.setheading(180)
        tim.forward(20*rows)
        tim.setheading(0)


s = t.Screen()
s.screensize(rows*(rows+1), rows*(rows+1))
s.exitonclick()