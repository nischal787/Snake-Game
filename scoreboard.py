from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.high_score =  int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("highscore.txt", mode="w") as new_highscore:
                    new_highscore.write(str(self.high_score))
            self.score = 0
            self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score =  {self.score} Highscore ={self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        
    def play_again(self):
        pass
