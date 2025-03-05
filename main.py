import turtle
import pandas
from write import Write
screen = turtle.Screen()
screen.title("U.s States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

write = Write()

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
print(answer_state)

states = pandas.read_csv("50_states.csv")
user_state = states[states["state"] == answer_state]
the_state = str(user_state.state)
the_x = user_state.x
the_y = user_state.y

if the_state:
    write.write_state(answer_state, the_x, the_y)
else:
    pass

screen.exitonclick()
