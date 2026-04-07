import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[0 + i])
    new_turtle.penup()
    new_turtle.goto(-230, -125 + (i * 50))
    turtles.append(new_turtle)
user_bet = screen.textinput(title="Make a bet!", prompt="Which colour turtle will win?")
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor().capitalize()
            if user_bet.capitalize()==winning_color:
                print(f"You won the bet! {winning_color} turtle won the race!")
            else:
                print(f"You lost the bet! {winning_color} turtle won the race!")
            is_race_on = False
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
