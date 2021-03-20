from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        with open("data.txt", mode="r") as score_file:
            self.high_score = int(score_file.read())
        self.starting_score = 0
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.starting_score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, 15, 'normal'))

    def reset(self):
        if self.starting_score > self.high_score:
            self.high_score = self.starting_score
            with open("data.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")
        self.starting_score = 0
        self.show_score()

    def increase_score(self):
        self.starting_score = self.starting_score + 1
        self.show_score()
