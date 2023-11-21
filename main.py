from turtle import Turtle, Screen

player = Turtle()


def move_forwards():
    player.fd(10)


def move_backwards():
    player.bk()


def move_left():
    player.lt(10)


def move_right():
    player.rt(10)


def clear():
    player.clear()
    player.penup()
    player.home()
    player.pendown()


screen = Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
