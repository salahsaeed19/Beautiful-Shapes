import turtle as t
import colorsys

t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
hue = 0.0
t.hideturtle()

for i in range(1000):
	color = colorsys.hsv_to_rgb(hue, 1, 1)
	t.pencolor(color)
	t.fd(i)
	t.rt(98.5)
	t.circle(50)
	hue += 0.005

t.exitonclick()
