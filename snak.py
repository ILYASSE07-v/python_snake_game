import turtle as t
import random
import time

#functions
def up():
	if head.direction != "down":
		head.direction = "up"
		
def right():
	if head.direction != "left":
		head.direction = "right"
		
def left():
	if head.direction != "right":
		head.direction = "left"
		
def down():
	if head.direction != "up":
		head.direction = "down"
		
def move():
	if head.direction == "up":
		head.sety(head.ycor() + 20)
	if head.direction == "left":
		head.setx(head.xcor() - 20)
	if head.direction == "right":
		head.setx(head.xcor() + 20)
	if head.direction == "down":
		head.sety(head.ycor() - 20)

#variables
seg = []
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
head.penup()
head.goto(0,0)
head.direction = "Stop"

#food 
food = t.Turtle()
food.shape(random.choice(["square", "circle", "triangle"]))
food.color(random.choice(["red", "green", "blue", "black", "purple"]))
food.penup()
food.goto(0,100)

#score
s = t.Turtle()
s.ht()
s.penup()
s.goto(0,250)
s.write("Score : 0 High Score : 0", align="center", font= ("candara", 24, "bold"))

#key binding
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(down, "Down")	

#main loop
while run:
	try:
		screen.update()
		
		#wall collision
		
		if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "Stop"
			for segment in seg:
				segment.goto(1000,1000)
			seg.clear()
			delay = 0.1
			score = 0
			s.clear()
			s.write(f"Score : {score} High Score : {h_score}", align="center", font= ("candara", 24, "bold"))
		
		#food collision
		
		if head.distance(food) < 20:
			food.goto(random.randint(-270,270), random.randint(-270,270))
			new_seg = t.Turtle()
			new_seg.shape("square")
			new_seg.color("orange")
			new_seg.penup()
			seg.append(new_seg)
			delay -= 0.001
			score += 10
			if score > h_score:
				h_score = score
			s.clear()
			s.write(f"Score : {score} High Score : {h_score}", align="center", font= ("candara", 24, "bold"))
		
		#body movment
		
		for i in range(len(seg) - 1, 0, -1):
			x = seg[i - 1].xcor()
			y = seg[i - 1].ycor()
			seg[i].goto(x,y)
		if seg:
			seg[0].goto(head.xcor(), head.ycor())
		move()
		
		#body collision
		
		for segment in seg:
			if segment.distance(head) < 20:
				
				time.sleep(1)
				head.goto(0,0)
				head.direction = "Stop"
				for segment in seg:
					segment.goto(1000,1000)
				seg.clear()
				delay = 0.1
				score = 0
				s.clear()
				s.write(f"Score : {score} High Score : {h_score}", align="center", font= ("candara", 24, "bold"))
		
		#speed control
		
		time.sleep(delay)
	except t.Terminator:
		run = False
