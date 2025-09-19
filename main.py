from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Score()


screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_on = True
while game_on == True:
    screen.update()
    time.sleep(.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(ball.heading(), ball.ycor())

    if ball.xcor() < -330 or ball.xcor() > 330:
        if ball.distance(l_paddle) < 40 or ball.distance(r_paddle) < 40:
            ball.bounce(ball.heading(), ball.ycor())

    if ball.xcor() > 395:
        scoreboard.r_point()
        ball.reset()
    elif ball.xcor() < -395:
        scoreboard.l_point()
        ball.reset()

screen.exitonclick()