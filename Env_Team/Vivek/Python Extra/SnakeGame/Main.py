from turtle import Turtle, Screen
from snake import Snake
import time

# Set up the initial screen
s1 = Screen()
s1.setup(width=600, height=600)
s1.bgcolor("black")
s1.title("My Snake Game")
s1.tracer(0)

sn1 = Snake()
s1.listen()
s1.onkey(sn1.up, "Up")
s1.onkey(sn1.down, "Down")
s1.onkey(sn1.right, "Right")
s1.onkey(sn1.left, "Left")

game_on = True
while game_on:
    s1.update()
    time.sleep(0.1)
    sn1.move()

s1.exitonclick()
