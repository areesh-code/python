import turtle

screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()


pen.penup()
pen.goto(-200, 0)  
pen.pendown()
pen.color("blue")
for _ in range(3):
    pen.forward(100)  
    pen.left(120)  

pen.penup()
pen.goto(50, 50)  
pen.pendown()


pen.color("green")
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)


pen.hideturtle()


screen.exitonclick()