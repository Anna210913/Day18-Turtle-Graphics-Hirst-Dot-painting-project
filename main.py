#import colorgram
#
#rgb_colours = []
#colours = colorgram.extract('image.jpg',20)
#for colour in colours:
#    r = colour.rgb.r
#    g = colour.rgb.g
#    b = colour.rgb.b
#    new_colour =(r, g, b)
#    rgb_colours.append(new_colour)
#
#print(rgb_colours)
import random
import turtle as turtle_module


turtle_module.colormode(255)
wayne = turtle_module.Turtle()
wayne.speed("fastest")
wayne.penup()
wayne.hideturtle()

colour_list = [(215, 151, 110), (30, 104, 179), (163, 81, 44), (180, 12, 33), (116, 170, 208), (216, 131, 160), (238, 222, 101), (158, 58, 97), (223, 65, 98), (223, 80, 52), (73, 24, 11), (18, 51, 149), (126, 183, 141), (169, 149, 31), (16, 170, 206), (47, 185, 138)]

wayne.setheading(225)
wayne.forward(325)
wayne.setheading(0)

num_of_dots =100


for dot_count in range(1, num_of_dots+1):
    wayne.dot(20, random.choice(colour_list))
    wayne.forward(50)

    if dot_count % 10 ==0:
        wayne.setheading(90)
        wayne.forward(50)
        wayne.setheading(180)
        wayne.forward(500)
        wayne.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()