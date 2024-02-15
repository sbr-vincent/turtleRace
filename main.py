from turtle import Turtle, Screen
import random

# Creating a turtle racing game
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-65, -40, -10, 10, 40, 65]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle  will win the race? Enter a color: ")
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle.forward(random.randint(0, 10))




screen.exitonclick()
