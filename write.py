from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 13, "normal")
class Write(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()

    def write_state(self, state, st_x, st_y):
        print("IN Write")
        print(st_x)
        print(st_y)
        # self.goto(st_x, st_y)
        # self.color("white")
        # self.write(arg=f"{state}")



