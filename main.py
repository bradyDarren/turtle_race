from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.textinput("Turtle Race", "Guess which color turtle will win the race.")


"""creation of 6 turtle objects."""
timmy = Turtle()
tom = Turtle()
thomas = Turtle()
todd = Turtle()
tony = Turtle()
theo = Turtle()

turtles = [timmy,tom,thomas, todd, tony, theo]
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

upper_y_cord = 0
lower_y_cord = 0



"""Designates a color to all turtle objects and places them in a starting position."""
for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    rand_color = random.choice(colors)
    turtle.color(rand_color)
    colors.remove(rand_color)
    if turtles.index(turtle) %  2 == 0:
        turtle.goto(x=-240, y=upper_y_cord)
        upper_y_cord += 30
    else:
        lower_y_cord -= 30 
        turtle.goto(x=-240, y=lower_y_cord)

for turtle in turtles:
    turtle.speed("slowest")
    if turtle.xcor() != 250:
        turtle.forward(random.choice(range(random.choice(range(5,20,5)))))
        

# for _ in range(30):
#     timmy.speed("slowest")
#     timmy.forward(random.choice(range(5,20,5)))
#     print(timmy.position())

screen.exitonclick()
