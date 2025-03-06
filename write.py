from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 7, "normal")


class Write(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()

    def write_state(self, state, st_x, st_y):
        self.goto(st_x, st_y)
        self.color("black")
        self.write(arg=f"{state}", align=ALIGNMENT, font=FONT)
        self.current_score += 1



