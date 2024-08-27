import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(400,400)
hg=turtle.Turtle
hg.color("#68CF19")
numofsides = 6
angles = 360.0/numofsides
length = 70
for i in range(numofsides):
  hg.forward(length)
  hg.right(angles)
