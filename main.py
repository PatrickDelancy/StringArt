import turtle

wn = turtle.Screen()
wn.setup(500, 400)

# un-comment this line to register the image for use in trinket
#wn.addshape("amongus.png")

drawSpeed = 0 #int(input("How fast do you want to render the artwork? "))

# TODO: determine angle for each wall to get proper bounce (perpendicular to center of angle)
walls = [
    [ 217 , 116 , 0 ,"lightgray"],
    [ 140 , 21 , 0 ,""],
    [ 117 , 125 , 0 ,""],
    [ 235 , 86 , 0 ,""],
    [ 103 , 30 , 0 ,""],
    [ 180 , 127 , 0 ,""],
    [ 218 , 28 , 0 ,""],
    [ 76 , 80 , 0 ,""],
    [ 187 , 21 , 0 ,""],
    [ 205 , 122 , 0 ,"red"],
    [ 52 , 162 , 0 ,""],
    [ 99 , 122 , 0 ,""],
    [ 107 , 187 , 0 ,""],
    [ 148 , 128 , 0 ,""],
    [ 168 , 171 , 0 ,""],
    [ 33 , 133 , 0 ,""],
    [ 78 , 97 , 0 ,""],
    [ 14 , 77 , 0 ,""],
    [ 81 , 53 , 0 ,""],
    [ 7 , 23 , 0 ,""],
    [ 92 , 37 , 0 ,""],
    [ 6 , -32 , 0 ,""],
    [ 216 , -70 , 0 ,""],
    [ 10 , -98 , 0 ,""],
    [ 210 , -113 , 0 ,""],
    [ 137 , -138 , 0 ,""],
    [ 204 , -147 , 0 ,""],
    [ 142 , -180 , 0 ,""],
    [ 197 , -178 , 0 ,""],
    [ 139 , -160 , 0 ,""],
    [ 213 , -91 , 0 ,""],
    [ 7 , -66 , 0 ,""],
    [ 219 , -27 , 0 ,""],
    [ 6 , -5 , 0 ,""],
    [ 221 , 9 , 0 ,""],
    [ 14 , -131 , 0 ,""],
    [ 97 , -150 , 0 ,""],
    [ 22 , -181 , 0 ,""],
    [ 95 , -181 , 0 ,""],
    [ 10 , -110 , 0 ,"maroon"],
    [ -42 , -111 , 0 ,""],
    [ 9 , -87 , 0 ,""],
    [ -52 , -82 , 0 ,""],
    [ 7 , -60 , 0 ,""],
    [ -54 , -50 , 0 ,""],
    [ 5 , -38 , 0 ,""],
    [ -55 , -22 , 0 ,""],
    [ 6 , 5 , 0 ,""],
    [ -53 , 15 , 0 ,""],
    [ 9 , 39 , 0 ,""],
    [ -40 , 60 , 0 ,""],
    [ 9 , 76 , 0 ,""]
  ]

numberOfVisibleWalls = 2

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
  mason = wall.pop(1)
  
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


def drawGrid():
  grid = turtle.Turtle()
  grid.speed(0)
  
  x = -200
  while x < 200:
    if x == 0:
      grid.color("blue")
      
    grid.penup()
    grid.goto(x,-200)
    grid.pendown()
    grid.goto(x,200)
    x += 10

# TODO: draw first numberOfVisibleWalls walls

# TODO: set initial game state : starting position, heading, initial color, etc.

# TODO: run game loop


# ---- this code just draws lines between the points so I can make get the picture correct.
needle = turtle.Turtle()
needle.penup()
needle.speed(drawSpeed)

wallIdx = 0
while wallIdx < len(walls):
  wall = walls[wallIdx]

  # I have been using this code block to make calculated adjustments to the coordinates, then copy/pasting the output
  # to correct the array above. Things like correct positioning on canvas
  # x = wall[xIdx] + 100
  # y = wall[yIdx] - 200
  # print("[",x,",",y,",",wall[angleIdx],",\""+wall[colorIdx]+"\"],")
  # needle.goto(x, y)
  
  needle.goto(wall[xIdx], wall[yIdx])
  
  if wall[colorIdx] != "":
    needle.pencolor(wall[colorIdx])
  
  needle.pendown()
  wallIdx += 1

# This will draw the imposter on top of the string art
# imposter = turtle.Turtle()
# imposter.speed(0)
# imposter.setheading(90)
# imposter.goto(100, 0)
# imposter.shape("amongus.png")

wn.mainloop()