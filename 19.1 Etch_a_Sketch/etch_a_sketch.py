from turtle import Turtle, Screen

ted = Turtle()
s = Screen()
s.delay(0)


def move_forward():
    ted.forward(10)


def move_back():
    ted.backward(10)


def rotate_clockwise():
    ted.right(10)


def rotate_anticlockwise():
    ted.left(10)


def clear():
    s.reset()


def circle():
    ted.circle(50)


def clock_circle():
    ted.right(1)
    ted.forward(1)


ted.fillcolor('red')
s.listen()
s.onkeypress(key="Up", fun=move_forward)
s.onkeypress(key="Down", fun=move_back)
s.onkeypress(key="Right", fun=rotate_clockwise)
s.onkeypress(key="Left", fun=rotate_anticlockwise)
s.onkeypress(key="c", fun=clear)
s.onkeypress(key="space", fun=circle)
s.onkeypress(key='a', fun=clock_circle)
s.exitonclick()
