from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(4):
    fd(16 * m)
    lt(90)
    fd(20 * m)
    lt(90)
up()
fd(4 * m)
lt(90)
fd(8 * m)
rt(180)
down()

for i in range(3):
    fd(35 * m)
    lt(90)
    fd(6 * m)
    lt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(7, 'white')

done()
update()

