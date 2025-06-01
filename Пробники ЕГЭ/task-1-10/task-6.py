from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(2):
    fd(6 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
bk(3 * m)
lt(90)
fd(5 * m)
rt(90)
up()
fd(8 * m)
down()
for i in range(4):
    fd(8 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(4, 'red')
update()
done()

