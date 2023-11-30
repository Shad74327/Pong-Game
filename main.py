from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""Setting up the screen"""
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

"""Taking inputs from user"""
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    """Ball bouncing off the wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """Ball hit the paddles"""
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """Player 1 missed the ball"""
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.player_2_points()

    """Player 2 missed the ball"""
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.player_1_points()

screen.exitonclick()
