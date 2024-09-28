import turtle as t
import random
t.colormode(255)
timmmy_the_turtle = t.Turtle()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb_tuple = (r,g,b)
    return rgb_tuple

timmmy_the_turtle.pensize(10)
timmmy_the_turtle.speed(20)
angles = [90,180,270,360]
for _ in range(100):
    timmmy_the_turtle.setheading(random.choice(angles))
    timmmy_the_turtle.forward(20)
    timmmy_the_turtle.color(random_color())

screen = t.Screen()
screen.exitonclick()