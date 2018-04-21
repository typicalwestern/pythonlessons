import turtle
import tortilla01

tortilla01.init()
turtle.penup()
turtle.backward(200)
turtle.pendown()

for k in range(10, 60, 10):
    tortilla01.david_star(k)
    turtle.penup()
    turtle. forward(k*4)
    turtle.pendown()
