import turtle
import pandas

screen = turtle.Screen()
screen.title("U.s States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
    # item() will look at the underlying data and grabs the first element
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

#     state to learn.csv
remainder = set(all_state) - set(guessed_state)
remaining = pandas.DataFrame(remainder)
remaining.to_csv("learn.csv")
