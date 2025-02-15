from turtle import *

tracer(0)
m = 15
lt(90)

up()
for i in range(10):
    rt(120)
    fd(10 * m)

down()
for i in range(7):
    fd(15 * m)
    rt(90)
for i in range(5):
    rt(60)
    fd(20 * m)
    rt(30)

up()
for x in range(-200, 200):
    for y in range(-200, 200):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
#55