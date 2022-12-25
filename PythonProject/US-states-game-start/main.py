import turtle
import pandas
from tkinter import messagebox


def game_over(guessed_states):
    data_frame = pandas.DataFrame(guessed_states)
    data_frame.to_csv("./missing_states.csv")


screen = turtle.Screen()
screen.title("U.S. states game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_state_original = data.state.to_list()
all_states = []
guessed_states = []
for x in all_state_original:
    all_states.append(x.lower())

guessed_states = all_states.copy()
answer_cnt = 0

game_is_on = True
while game_is_on:
    answer_from_user = screen.textinput(title=f"{answer_cnt}/50   Guess the state!", prompt="Your answer is").lower()

    # if len(data[data['state'].str.lower() == answer_from_user.lower()]) == 0:
    if answer_from_user not in all_states:
        if answer_from_user == 'exit':
            game_is_on = False
            game_over(guessed_states)
            break
        options = messagebox.askyesno("Wrong answer", "Continue?", icon="warning")
        if not options:
            game_is_on = False
            game_over(guessed_states)
    # elif len(data[data['state'].str.lower() == answer_from_user.lower()]) == 1:
    elif answer_from_user in all_states:
        guessed_states.remove(answer_from_user)
        answer_cnt += 1
        x_cor = data[data.state.str.lower() == answer_from_user].x.item()
        y_cor = data[data.state.str.lower() == answer_from_user].y.item()
        # x_cor = data[answer_from_user]['x'].item()
        # y_cor = data[answer_from_user]['y'].item()
        state_data = data[data.state.str.lower() == answer_from_user]
        tmp_turtle = turtle.Turtle()
        tmp_turtle.penup()
        tmp_turtle.hideturtle()
        tmp_turtle.setpos(x_cor, y_cor)
        tmp_turtle.write(data[data.state.str.lower() == answer_from_user].state.item())
    elif answer_cnt == 50:
        messagebox.showinfo("Congratulations!")
        game_is_on = False


screen.exitonclick()