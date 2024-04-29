"""polygon.py
C West
This program will draw a polygon and prompt the user for the number of sides and colors."""
# docs.python.org/3/library/turtle.html

import turtle
#from turtle import turtle

turtle.pencolor("blue") # pen color

polygon_sides = int(input ("Let\'s draw a polygon.  How many sides does this polygon have? Choose a number between 3 and 10.  "))
polygon_fill = str(input ("Next choose a fill color by typing blue, red, yellow, green, purple.  ")) # fill color

turtle.fillcolor(polygon_fill) # indicates the user color choice
turtle.begin_fill() # this is where the fill color starts

if polygon_sides > 2 and polygon_sides < 11:
    polygon_angle = ((polygon_sides-2) * 180) / polygon_sides    # instructors formula
    #print ("polygon angle =  ", polygon_angle)
    polygon_calc = (180 - polygon_angle)
    #print("polygon_calc", polygon_calc)
    turtle.shape("turtle") # shape of the pointer can be arrow circle classic square triangle and turtle
    for val in range(polygon_sides):
#        pass
        turtle.forward(100) # moves the line forward 100 places
##        turtle.left(polygon_angle)
        turtle.left(polygon_calc)
        print(val)
    turtle.end_fill()

else:
    print ("Incorrect entry, end of program.")

turtle.home() # sends the turtle pointer home if it is off screen

turtle.exitonclick() # exits from the turtle screen

z = input("end, CWest")
