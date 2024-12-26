from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput("Turtle Race", "Guess which color turtle will win the race.")


"""creation of 6 turtle objects."""
turtles = [Turtle(shape="turtle") for _ in range(6)]
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

start_x = -240
upper_y_cord = 0
lower_y_cord = 0

"""Designates a color to all turtle objects and places them in a starting position."""
for i, turtle in enumerate(turtles):
    turtle.penup()
    rand_color = colors.pop(random.randint(0,len(colors)-1))
    turtle.color(rand_color)
    if i %  2 == 0:
        turtle.goto(x=start_x, y=upper_y_cord)
        upper_y_cord += 30
    else:
        lower_y_cord -= 30 
        turtle.goto(x=start_x, y=lower_y_cord)

game_on = True

while game_on: 
    for turtle in turtles: 
        if turtle.xcor() >= 220:
            game_on = False 
            wining_color = turtle.pencolor()
            if user_input != wining_color:
                print(f"SORRY!!! You guessed incorrectly. The correct color was {wining_color}.")
            else: 
                print(f"YOU WIN!! You guessed the correct color.")
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
