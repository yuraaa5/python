def seven(n):
    for i in range(n):
        forward(50)
        left(360/n)
    
    left(51.5)

    for j in range(n):
        forward(112)
        left(360/n*3)

def nine(n):
    for j in range(n):
        forward(50)
        left(40)

    left(60)

    for k in range(n):
        forward(143)
        left(160)

from turtle import *
seven(7)
#nine(9)
done()
