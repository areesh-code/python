import turtle, random
sc= turtle.Screen().setup(400,600)
t= turtle.Turtle()
b= ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]
for i in range(50):
  c= random.choice(b)
  t.pencolor(c)
  t.forward(i*5)
  t.right(90)
turtle.done()
  

