from turtle import *

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window1
penup()
goto(20, 135)
pendown()

color("cyan")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
end_fill()
forward(25)
color("brown")
left(90)
forward(50)
penup()
goto(20, 160)
pendown()
right(90)
forward(50)

#window2
penup()
goto(120, 135)
pendown()

color("cyan")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
end_fill()

color("brown")
penup()
goto(145, 135)
pendown()
left(90)
forward(50)
penup()
goto(120, 160)
pendown()
right(90)
forward(50)



exitonclick()