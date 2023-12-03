from turtle import Turtle, Screen, clearscreen, home
#import random

screen = Screen()
screen.colormode(255)
screen.listen()

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")
timmy_the_turtle.speed(0)
#timmy_the_turtle.pensize(10)

#sqaure
#for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.right(90)


#dashed line
#timmy_the_turtle.up()
#timmy_the_turtle.setposition(-400,0)

#for _ in range(50):
#    timmy_the_turtle.up()
#    timmy_the_turtle.forward(5)
#    timmy_the_turtle.down()
#    timmy_the_turtle.forward(5)

#triangle sqaure pentagon
#for x in range(3,30):
#    timmy_the_turtle.color(random.randrange(256),random.randrange(256),random.randrange(256))
#    for _ in range(x):
 #       timmy_the_turtle.right(360/x)
 #       timmy_the_turtle.forward(100)

#random walk
#for x in range(1,50):
#    timmy_the_turtle.color(random.randrange(256),random.randrange(256),random.randrange(256))
#   timmy_the_turtle.right(random.randrange(361))
#    timmy_the_turtle.forward(30)

#spirograph
#for x in range(0,36):
#    timmy_the_turtle.color(random.randrange(256),random.randrange(256),random.randrange(256))
#    timmy_the_turtle.right(10)
#    timmy_the_turtle.circle(100)

#hirst painting
#move_x = 0
#move_y = 0
#for y in range(0,10):
#    for x in range(0,10):
#        timmy_the_turtle.up()
#        timmy_the_turtle.setx(-300 + move_x)
#        timmy_the_turtle.sety(-300 + move_y)
#        timmy_the_turtle.dot(20,random.randrange(256),random.randrange(256),random.randrange(256))
#        timmy_the_turtle.setheading(0)
#        timmy_the_turtle.forward(50)
#        move_x += 50
#    move_y += 50
#    move_x = 0
#timmy_the_turtle.hideturtle()

#etch-a-sketch
def move_forward():
    timmy_the_turtle.forward(10)

def move_backword():
        timmy_the_turtle.backward(10)

def move_right():
    timmy_the_turtle.right(10)

def move_left():
    timmy_the_turtle.left(10)

def clear_reset():
    clearscreen()
    home()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backword)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_reset)


screen.exitonclick()