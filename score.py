from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(
            f"Score: 0 Highscore: {self.high_score}",
            align="center",
            font=FONT,
        )

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(
            f"Score: {self.score} Highscore: {self.high_score}",
            align="center",
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_score()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=FONT)
