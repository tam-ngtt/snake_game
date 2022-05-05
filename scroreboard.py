from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt") as data:
            self.write(f"Score: {self.score} High score: {data.read()}", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


