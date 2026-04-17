import turtle as t
import random
import time

#variables
delay = 0.1
score = 0
h_score = 0
run = True

# setting up the screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")
screen.title("snake game")
screen.tracer(0)

#the head
head = t.Turtle()
head.color("white")
head.shape("square")
head.up()
head.goto(0,0)
head.direction = "Stop"

#food 
food = t.Turtle()
food.shape(random.choice(["square", "circle", "triangle"]))
food.color(random.choice(["red", "green", "blue", "black", "purple"]))
food.up()
food.goto(0,100)

#score
s = t.Turtle()
s.ht()
s.up()
s.goto(0,250)
s.write("Score : 0 High Score : 0", align="center", font= ("candara", 24, "bold"))
screen.update()
t.done()
