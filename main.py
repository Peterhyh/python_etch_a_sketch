from turtle import Turtle, Screen

player = Turtle()


def move_forwards():
    player.fd(10)


screen = Screen()
screen.onkey(move_forwards, "space")
screen.exitonclick()
