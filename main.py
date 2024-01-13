import turtle

tim = turtle.Turtle()


def fwd():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def back():
    tim.back(10)


def clean():
    tim.home()
    tim.clear()


def pen_up():
    tim.penup()


def pen_down():
    tim.pendown()


screen = turtle.Screen()
screen.listen()
screen.onkey(key='w', fun=fwd)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=back)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clean)
screen.onkey(key='space', fun=pen_up)
screen.onkey(key='m', fun=pen_down)
screen.mainloop()
