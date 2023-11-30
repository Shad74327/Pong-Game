from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.points_paddle_1 = 0
        self.points_paddle_2 = 0
        self.update_score()

    def update_score(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.points_paddle_2, align="center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.points_paddle_1, align="center", font=("Courier", 80, "normal"))

    def player_1_points(self):
        self.points_paddle_1 += 1
        self.update_score()

    def player_2_points(self):
        self.points_paddle_2 += 1
        self.update_score()
