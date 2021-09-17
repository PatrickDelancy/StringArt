import turtle

wn = turtle.Screen()

# un-comment this line to register the image for use in trinket
#wn.addshape("amongus.png")

drawSpeed = 0 #int(input("How fast do you want to render the artwork? "))

walls = [
[ 217 , 116 , 231 ,"lightgray"],
[ 140 , 21 , 166.7223925040845 ,""],
[ 117 , 125 , 222.09065168579855 ,""],
[ 235 , 86 , 278.0455931869225 ,""],
[ 140 , 21 , 175.8540799064706 ,""],
[ 76 , 80 , 234.6678810222037 ,""],
[ 187 , 21 , 205.95145529518106 ,""],
[ 205 , 122 , 122.62180253158897 ,"red"],
[ 52 , 162 , 242.47436854723162 ,""],
[ 99 , 122 , 201.29179696073857 ,""],
[ 107 , 187 , 193.88976226678415 ,""],
[ 148 , 128 , 184.92606050743768 ,""],
[ 168 , 171 , 130.38851126121142 ,""],
[ 33 , 133 , 258.53055976585495 ,""],
[ 78 , 97 , 259.3471081910807 ,""],
[ 14 , 77 , 268.82302289666063 ,""],
[ 81 , 53 , 271.1799603597051 ,""],
[ 7 , 23 , 105.71043940624662 ,""],
[ 92 , 37 , 114.04697147248885 ,""],
[ 6 , -32 , 284.24207192660174 ,""],
[ 216 , -70 , 268.741760658569 ,""],
[ 10 , -98 , 271.72559391499044 ,""],
[ 210 , -113 , 277.3077112569058 ,""],
[ 137 , -138 , 275.6269624436203 ,""],
[ 204 , -147 , 280.1869247883351 ,""],
[ 142 , -180 , 105.05353290591546 ,""],
[ 197 , -178 , 82.42055294038005 ,""],
[ 139 , -160 , 102.87800373463654 ,""],
[ 213 , -91 , 108.03896680274715 ,""],
[ 7 , -66 , 91.75209197368298 ,""],
[ 219 , -27 , 92.2633768498946 ,""],
[ 6 , -5 , 88.9143323415745 ,""],
[ 221 , 9 , 108.8986190003971 ,""],
[ 14 , -131 , 280.58893288125887 ,""],
[ 97 , -150 , 274.781597477521 ,""],
[ 22 , -181 , 101.22846949995 ,""],
[ 95 , -181 , 70.06409552092646 ,""],
[ 10 , -110 , 160.61494857855314 ,"maroon"],
[ -42 , -111 , 103.15141488033754 ,""],
[ 9 , -87 , 100.25761190299863 ,""],
[ -52 , -82 , 97.88182388564633 ,""],
[ 7 , -60 , 95.56980371785698 ,""],
[ -54 , -50 , 91.09331142134289 ,""],
[ 5 , -38 , 88.28257291968123 ,""],
[ -55 , -22 , 94.47193183791376 ,""],
[ 6 , 5 , 97.1277765271006 ,""],
[ -53 , 15 , 95.77076600856412 ,""],
[ 9 , 39 , 88.98133465162584 ,""],
[ -40 , 60 , 87.44242743467436 ,""],
[ 9 , 76 , 87.44242743467436 ,""],
]

# Control variables 
numberOfVisibleWalls = 2
move_increment = 2
keep_running = 1
line_index = 0
boundary_size = 500
xIdx = 0
yIdx = 1
angleIdx = 2
colorIdx = 3
turtleIdx = 4

def drawWall(idx):
  global walls
  global drawSpeed

  wall = walls[idx]
  
  if len(wall) <= turtleIdx:
    mason = turtle.Turtle()
    mason.hideturtle()
    mason.speed(drawSpeed)
    mason.pensize(4)
    wall.append(mason)
  else:
    mason = wall[turtleIdx]
  if (wall[colorIdx] != ""):
      mason.pencolor(wall[colorIdx])  
  mason.penup()
  mason.goto(wall[xIdx], wall[yIdx])
  mason.setheading(wall[angleIdx])
  
  mason.backward(25)
  mason.pendown()
  mason.forward(50)
  mason.backward(25)


def breakWall(idx):
  global walls
  
  wall = walls[idx]
  mason = wall[turtleIdx]
  
  # remove intact wall
  mason.clear()
  # TODO: draw broken wall
  mason.penup()
  mason.setheading(wall[angleIdx])
  # remove broken wall
  mason.clear()
    

def collideWithWall(idx):
  global walls
  
  breakWall(idx)
  if idx < len(walls) - numberOfVisibleWalls:
    drawWall(idx + numberOfVisibleWalls)

# method to draw the bounding box
def draw_boundaries():
  boundary_pen = turtle.Turtle()
  boundary_pen.speed(0)
  boundary_pen.pensize(5)
  boundary_pen.penup()
  # position to upper left corner
  boundary_pen.goto(-boundary_size/2, boundary_size/2)
  boundary_pen.pendown()
  sides_drawn = 0
  while (sides_drawn < 4):
    boundary_pen.forward(boundary_size)  
    boundary_pen.right(90)
    sides_drawn += 1
  boundary_pen.hideturtle()

# "bounce" the ball off the obstacle, based on angle of the obstacle
def change_heading(heading, angle_of_obstacle):
  return (2 * angle_of_obstacle - heading + 360) % 360

#  draw first numberOfVisibleWalls walls
wallsDrawn = 0
while (wallsDrawn <  numberOfVisibleWalls):
  wallsDrawn += 1
  drawWall(wallsDrawn)


# set initial game state : starting position, heading, initial color, etc.
wn = turtle.Screen()
wn.setup(boundary_size + 100,boundary_size + 100)
# wn.addshape("amongus.png")
drawSpeed = 0 #int(input("How fast do you want to render the artwork? "))

draw_boundaries()
traveller = turtle.Turtle(shape="circle")
traveller.penup()
traveller.speed(drawSpeed)
traveller.goto(walls[0][xIdx], walls[0][yIdx])
traveller.setheading(walls[0][angleIdx])
traveller.pencolor(walls[0][colorIdx])
traveller.pendown()
nextWallIndex = 1

# TODO: run game loop
while (nextWallIndex < len(walls)):
  traveller.forward(move_increment)
  # have we hit a side?  This is an error condition
  if (abs(traveller.xcor()) >= boundary_size/2 or abs(traveller.ycor()) >= boundary_size/2 ):
    print("Error.  We missed a wall")
    exit

  wall = walls[nextWallIndex]
  wallTurtle = wall[turtleIdx]  

  if (int(traveller.distance(wallTurtle.pos())) < 3):
    collideWithWall(nextWallIndex)
    traveller.setheading(change_heading(traveller.heading(), wall[angleIdx]))
    if (wall[colorIdx] > ""):
      traveller.pencolor(wall[colorIdx])
      traveller.color(wall[colorIdx])
    nextWallIndex += 1

# everything is drawn
traveller.hideturtle()

# This will draw the imposter on top of the string art
# imposter = turtle.Turtle()
# imposter.speed(0)
# imposter.setheading(90)
# imposter.goto(100, 0)
# imposter.shape("amongus.png")

wn.mainloop()
