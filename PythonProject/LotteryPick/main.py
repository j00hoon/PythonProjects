import tkinter
import random


FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
NUMBER_WIDTH = 100
NUMBER_HEIGHT = 100
RECTANGLE_X = 11
RECTANGLE_Y = 11
RECTANGLE_X1 = 50
RECTANGLE_Y1 = 50
LIST_NUMBERS = []
ODD_NUMBERS = list(range(1, 71, 2))
EVEN_NUMBERS = list(range(2, 71, 2))
MEGA_NUMBERS = list(range(1, 26))
RANGE_1 = range(36, 71)
RANGE_2 = range(1, 36)


# Select 3 odd numbers, and 2 even numbers range 1~70
def start_select_numbers():
    global LIST_NUMBERS

    result_label.config(text="Hmm...", foreground=RED)
    # LIST_NUMBERS = [random.randrange(1, 70, 2) for _ in range(0, 3)]
    # LIST_NUMBERS.extend([random.randrange(2, 70, 2) for num in range(0, 2)])
    LIST_NUMBERS = random.sample(ODD_NUMBERS, 3)
    LIST_NUMBERS.extend(random.sample(EVEN_NUMBERS, 2))

    condition_numbers_in_range()


# Check if 3 numbers in range 36~70 and 2 numbers in range 1~35
def condition_numbers_in_range():
    global LIST_NUMBERS
    range_1 = 0
    range_2 = 0

    for num in LIST_NUMBERS:
        if num in RANGE_1:
            range_1 += 1
        else:
            range_2 += 1

    if range_1 == 3 and range_2 == 2:
        condition_sum_numbers(True)
    else:
        return False


# Check sum of numbers whether in range 132~240
def condition_sum_numbers(condition):
    global LIST_NUMBERS
    sum = 0

    if condition:
        for num in LIST_NUMBERS:
            sum += num

    if sum in range(132, 141):
        check_final_numbers(True)
    else:
        check_final_numbers(False)


def check_final_numbers(condition):
    global LIST_NUMBERS
    if condition:
        LIST_NUMBERS.extend(random.sample(MEGA_NUMBERS, 1))
        number1.itemconfig(number1_text, text=LIST_NUMBERS[0])
        number2.itemconfig(number2_text, text=LIST_NUMBERS[1])
        number3.itemconfig(number3_text, text=LIST_NUMBERS[2])
        number4.itemconfig(number4_text, text=LIST_NUMBERS[3])
        number5.itemconfig(number5_text, text=LIST_NUMBERS[4])
        number6.itemconfig(number6_text, text=LIST_NUMBERS[5])
        result_label.config(text="Your number!", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)
        print(LIST_NUMBERS)
    LIST_NUMBERS = []
    start_select_numbers()


window = tkinter.Tk()
window.title("You want to be a billionare?!?!")
window.config(padx=10, pady=10, background=YELLOW)


number1 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number1.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number1_text = number1.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number1.grid(row=0, column=0)

number2 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number2.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number2_text = number2.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number2.grid(row=0, column=1)

number3 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number3.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number3_text = number3.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number3.grid(row=0, column=2)

number4 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number4.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number4_text = number4.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number4.grid(row=0, column=3)

number5 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number5.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number5_text = number5.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number5.grid(row=0, column=4)

number6 = tkinter.Canvas(width=NUMBER_WIDTH, height=NUMBER_HEIGHT, background=YELLOW, highlightthickness=0)
number6.create_rectangle(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_X1, RECTANGLE_Y1, fill="white")
number6_text = number6.create_text(RECTANGLE_X + 20, RECTANGLE_Y + 20, text="", font=(FONT_NAME, 20, "bold"))
number6.grid(row=2, column=2)

result_label = tkinter.Label(text="Hmm...", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=RED)
result_label.grid(row=3, column=2)


start_button = tkinter.Button(text="Start", command=start_select_numbers)
start_button.grid(row=3, column=0)


window.mainloop()

