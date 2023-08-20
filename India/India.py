from turtle import*

#Ashok Chakra
pencolor("#000080")
dot(205)
pencolor("white")
dot(180)
pencolor("#000080")
dot(35)
penup()
right(8)
forward(90)
pendown()
left(90)
i = 1
while i < 25:
  circle(90,75,20)
  dot(10)
  i += 1
penup()
home()
pendown()
pensize(5)
j = 1
while j < 25:
  forward(90)
  back(90)
  right(15)
  j += 1

pensize(1)
penup()
right(90)
forward(115)
right(90)
pendown()

#Green Side
pencolor("#138808")
begin_fill()
fillcolor("#138808")
forward(512)
left(90)
forward(225)
left(90)
forward(1024)
left(90)
forward(225)
left(90)
forward(512)
end_fill()

penup()
right(90)
forward(230)
right(90)
pendown()

#Orange Colour
pencolor("#FF9933")
begin_fill()
fillcolor("#FF9933")
forward(512)
left(90)
forward(225)
left(90)
forward(1024)
left(90)
forward(225)
left(90)
forward(512)
end_fill()
hideturtle()
done()