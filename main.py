import turtle
import pandas
from write import Write
screen = turtle.Screen()
screen.title("U.s States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

write = Write()
data = pandas.read_csv("50_states.csv")
all_states = data.state

chosen_states = []
while write.current_score <= 50:

    answer_state = screen.textinput(title=f"{write.current_score}/50 States correct",
                                    prompt="What's another state's name?").title()

    for state in all_states:
        if answer_state == state and answer_state not in chosen_states:
            user_state = data[data["state"] == state].to_dict()
            # if answer_state not in chosen_states:
            for state_num in user_state["state"]:
                state = user_state["state"][state_num]
                state_x = user_state["x"][state_num]
                state_y = user_state["y"][state_num]
                write.write_state(state, state_x, state_y)
                chosen_states.append(state)
            # else:
            #     write.already_chose(state)
        else:
            pass

screen.exitonclick()
