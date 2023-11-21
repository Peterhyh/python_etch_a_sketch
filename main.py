from turtle import Turtle, Screen

player = Turtle()


def move_forwards():
    player.fd(10)


def move_backwards():
    player.bk()


def move_left():
    player.lt()


def move_right():
    player.rt()


screen = Screen()
screen.onkey(move_forwards, "space")
screen.exitonclick()
