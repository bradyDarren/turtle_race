from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
screen.textinput("Turtle Race", "Guess which color turtle will win the race.")

timmy = Turtle()
tom = Turtle()
thomas = Turtle()
todd = Turtle()
tony = Turtle()
theo = Turtle()

turtles = [timmy,tom,thomas, todd, tony, theo]
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_cord = 0

for turtle in turtles:
    turtle.shape("turtle")
    turtle.color(random.choice(colors))
    turtle.goto(x=-240, y=y_cord)
    y_cord += 20

# timmy.goto(x=-240,y=0)

screen.exitonclick()
