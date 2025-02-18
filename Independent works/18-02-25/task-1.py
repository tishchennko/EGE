from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(2):
    rt(120)
    fd(7*m)

rt(300)

for i in range(2):
    rt(120)
    fd(7 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
