# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

#variables
#has all starting values for all variables
x1 = -200
y1 = 100
x2 = -200
y2 = 50
x3 = -200
y3 = 0
x4 = -200
y4 = -50

#setup
#backround and my sprites
set_background("castle")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("baseball",x2,y2)
t3 = create_sprite("soccerball",x3,y3)
t4 = create_sprite("waterbottle",x4,y4)

#racing
#shows how much the variables change by and how many times it has to repeat
#sprite three is the fastest because it has a high odd of going faster then everything else
for i in range(30):
	x1 += random.randint(7,18)
	x2 +=(7)
	x3 += random.randint(0,25)
	x4 +=(8)
	t1.goto(x1, y1)
	t2.goto(x2,y2)
	t3.goto(x3,y3)
	t4.goto(x4,y4)
	time.sleep(0.1)

#winner
#text for player 1 and 2 winnign
#text for player 3 and 4 winning
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("Basketball won") 
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("baseball won")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
	print("soccerball won")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
	print("waterbottle won")

turtle.exitonclick()