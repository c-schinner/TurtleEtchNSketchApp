from turtle import Turtle, Screen


t = Turtle()
screen = Screen()


def left():
    t.left(5)


def right():
    t.right(5)


def forward():
    t.forward(5)


def backward():
    t.back(5)


def c_clear():
    t.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=c_clear)
screen.exitonclick()
