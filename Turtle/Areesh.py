import turtle
import random
screen = turtle.Screen()
screen.setup(400, 600)
t = turtle.Turtle()
t.speed("fastest") 
b= ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]
for i in range(50):
  color = random.choice(b)
  t.pencolor(color)
  t.forward(i*5)
  t.right(90)
turtle.done()



