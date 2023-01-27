import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
RED = "#e7305b"
GREEN = "#9bdeac"
random_card = []
COUNT = 3
timer = None


# read data from csv
# check if "words_to_learn.csv" file exists or not
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    # convert data into dictionary
    word_dict = original_data.to_dict(orient="records")
else:
    # convert data into dictionary
    word_dict = data.to_dict(orient="records")


# save word to 'words_to_learn.csv'
def save_word_csv():
    global random_card

    save_word_dict = {
        "French" : [random_card["French"]],
        "English" : [random_card["English"]]
    }

    # check whether "words_to_learn.csv" file exists or not
    # if no, create the csv file
    # if yes, read "French" list and "English" list
    # then append the new value into these lists
    # finally, create a new dictionary, and then write into the csv file
    try:
        df = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        df = pandas.DataFrame(save_word_dict)
        df.to_csv("./data/words_to_learn.csv", index=False)
    else:
        french_list = df.French.to_list()
        english_list = df.English.to_list()
        french_list.append(random_card["French"])
        english_list.append(random_card["English"])
        new_word_dict = {
            "French": french_list,
            "English": english_list
        }
        new_df = pandas.DataFrame(new_word_dict)
        new_df.to_csv("./data/words_to_learn.csv", index=False)


def delete_from_csv():
    global random_card

    # convert into list
    # french_list = word_from_csv.French.to_list()
    # english_list = word_from_csv.English.to_list()
    # french_list.remove(random_card["French"])
    # english_list.remove(random_card["English"])

    # # convert list to dictionary
    # new_word_dict = {
    #     "French" : french_list,
    #     "English" : english_list
    # }

    word_dict.remove(random_card)
    print(len(word_dict))
    # save a new dictionary into "french_words.csv"
    df = pandas.DataFrame(word_dict)
    df.to_csv("./data/french_words.csv", index=False)
    save_word_csv()


def next_word():
    global random_card, COUNT
    # data frame
    #word_frame = pandas.DataFrame(word_dict)

    # check if COUNT is 0
    # if so, call reset()
    if COUNT == 0:
        delete_from_csv()
        reset()
    canvas.itemconfig(title, text="French")
    random_card = random.choice(word_dict)
    canvas.itemconfig(word, text=random_card["French"])
    count_method()


# reset everything
def reset():
    global COUNT
    COUNT = 3
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text="French", font=(FONT_NAME, 40, "italic"), fill=RED)
    canvas.itemconfig(word, text="", font=(FONT_NAME, 60, "bold"), fill=GREEN)


# count 3 seconds or something kk
# after 3 seconds, then call english_word() to show english meaning
def count_method():
    global COUNT
    if COUNT > 0:
        global timer
        COUNT -= 1
        timer = window.after(500, count_method)
    else:
        english_word()


# show english meaning
def english_word():
    global random_card, COUNT

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", font=(FONT_NAME, 40, "italic"), fill="white")
    canvas.itemconfig(word, text=random_card["English"], font=(FONT_NAME, 60, "bold"), fill="white")


# cancel 3 seconds count
def delay_cancel():
    window.after_cancel(timer)


window = tkinter.Tk()
window.title("Flash card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 265, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill=RED)
word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill=GREEN)

wrong_button_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, background=BACKGROUND_COLOR, command=delay_cancel)
wrong_button.grid(row=1, column=0)

right_button_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, background=BACKGROUND_COLOR, command=next_word)
right_button.grid(row=1, column=1)

next_word()
window.mainloop()



