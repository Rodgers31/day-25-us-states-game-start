from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 7, "normal")
FONT2 = ("Courier", 10, "normal")


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

    # def already_chose(self, state):
    #     self.goto(0, 0)
    #     self.color("black")
    #     self.write(arg=f"Already chose {state}", align=ALIGNMENT, font=FONT2)
    #     time.sleep(1)
    #     self.clear()

