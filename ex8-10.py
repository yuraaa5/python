def draw_tree():
    penup()
    goto(-20, -155)
    pendown()
    fillcolor('brown')
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

    penup()
    goto(-110, -115)
    pendown()
    fillcolor('green')
    begin_fill()
    for j in range(3):
        forward(220)
        left(120)
    end_fill()

    penup()
    goto (-90,-30)
    pendown()
    fillcolor('green')
    begin_fill()
    for k in range(3):
        forward(180)
        left(120)
    end_fill()

    penup()
    goto (-70,45)
    pendown()
    fillcolor('green')
    begin_fill()
    for k in range(3):
        forward(140)
        left(120)
    end_fill()

def draw_star():
    penup()
    goto(-33,165)
    pendown()
    fillcolor('yellow')
    begin_fill()
    for p in range(10):
        forward(25)
        if p % 2 == 0:
            left(72)
        else:
            right(144)
    end_fill()

from turtle import *
draw_tree()
draw_star()
done()