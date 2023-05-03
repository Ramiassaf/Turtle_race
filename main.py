# Import necessary modules
from turtle import Turtle, Screen
import random

# Define the colors of the turtles
TURTLE_COLORS = ["red", "yellow", "blue", "orange", "green", "purple"]

# Create the screen and get the user's bet
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which Turtle will win the race? Enter a Color. ")

# Validate the user's bet
while user_bet not in TURTLE_COLORS:
    if user_bet == "":
        break
    user_bet = screen.textinput(title="Make your Bet", prompt="Invalid input. Which Turtle will win the race? Enter a Color. ")

# Create the turtles
turtles = []#append all the turtles object created from the turtle class
y = -150
for color in TURTLE_COLORS:
    new_turtle = Turtle("turtle")#giving the object a shape
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y)#here before the race start make all the turtles start from the same start point
    y += 50
    turtles.append(new_turtle)#filling the list with the turtles

# Start the race if a valid bet was placed
if user_bet:
    is_race_on = True

# Move the turtles and determine the winner
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've Won!, {winning_color} turtle is the winner")
            else:
                print(f"You Lose!, {winning_color} turtle is the winner")
            is_race_on = False

        movement = random.randint(0, 10)#to make a range of numbers
        turtle.forward(movement)#here it take a number from 0 to 10 and move forward by it 

# Exit the program when the user clicks on the screen
screen.exitonclick()
