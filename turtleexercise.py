import turtle
import random
#turtle.hideturtle()
"""
#60
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
"""
"""
#61
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
"""
"""
#62
angle = 360
turtle.right(90)
turtle.penup()
turtle.forward(250)
turtle.left(90)
turtle.pendown()
while (angle >= 0):
    turtle.forward(5)
    turtle.left(1)
    angle = angle - 1
"""
"""
turtle.color("black","red")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.color("black","green")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
turtle.right(90)
turtle.forward(100)

turtle.color("black","blue")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
"""
turtle.shape("turtle")
while(1 == 1):
    n1 = random.randint(1,100) #forword
    n2 = random.randint(1,360) #angle
    n3 = random.randint(1,2)   #left or right
    n4 = random.randint(1,4)   #lift pen
    n5 = random.randint(1,10)  #pen thickness
    n6 = random.randint(1,100) #turtle size
    turtle.pensize(n5)
    turtle.turtlesize(n6)
    if(n4 < 4):
        turtle.pendown()
    elif(n4 == 4):
        turtle.penup()
    turtle.forward(n1)
    if(n3 == 1):
        turtle.right(n2)
    elif(n3 == 2):
        turtle.left(n2)
turtle.exitonclick()