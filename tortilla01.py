import turtle


def init():
    turtle.clear()
    turtle.setpos(0, 0)
    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.color('blue', 'red')
    turtle.speed(100)


def regular_polygone(N, edge):
    for i in range(N):
        turtle.forward(edge)
        turtle.right(360 / N)


def many_polygones():
    init()
    for x in range(3, 17):
        regular_polygone(x, 50)


def david_star(edge):
    for i in range(6):
        turtle.begin_fill()
        for k in range(3):
            turtle.forward(edge)
            turtle.left(120)
        turtle.end_fill()
        turtle.forward(edge)
        turtle.right(360 / 6)


if __name__ == '__main__':
    init()
    david_star(100)
