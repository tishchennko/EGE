from turtle import *

m = 25
tracer(0)
lt(90)

for i in range(15):
    fd(4 * m)
    rt(60)



up()
goto(0, 0)
lt(90)
down()
fd(50 * m)
up()
goto(0, 0)
lt(90)
down()
fd(50 * m)




up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()