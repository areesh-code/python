import turtle
import random


screen = turtle.Screen()
screen.setup(width=400, height=600)


t = turtle.Turtle()
t.speed("fastest")  


colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]


for i in range(50):
    color = random.choice(colors)  
    t.pencolor(color)             
    t.forward(i * 5)               
    t.right(90)                   


turtle.done()
