from turtle import Turtle

ALIGNMENT = "center"
BOARDALIGN = "left"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-295, 180)
        self.color("black")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align=BOARDALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()
