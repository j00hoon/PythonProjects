import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count_down():
    global reps, checkmarks

    window.after_cancel(timer)
    reps = 0
    checkmarks = ""

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")




# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_count_down():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down_time = LONG_BREAK_MIN * 60
        timer_label.config(text="Long break", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=PINK)
    elif reps % 2 == 1:
        count_down_time = SHORT_BREAK_MIN * 60
        timer_label.config(text="Short break", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=RED)
    else:
        count_down_time = WORK_MIN * 60
        timer_label.config(text="Work", font = (FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)
    count_down(count_down_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global checkmarks
    count_min = math.floor(count / 60)
    count_sec = format(count % 60, '02d')
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        start_count_down()
        if reps % 2 == 1:
            checkmarks += "✓"
            check_mark.config(text=checkmarks, font=35, foreground=GREEN, background=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
# window.minsize(height=500, width=500)
window.config(padx=100, pady=50, background=YELLOW)

tomato_image = tkinter.PhotoImage(file='./tomato.png')
canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 133, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN, background=YELLOW)
timer_label.grid(row=0, column=1)

# start_button = tkinter.Button(text="Start", highlightthickness=0, command=lambda:count_down(count_down_time))
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_count_down)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_count_down)
reset_button.grid(row=2, column=2)

check_mark = tkinter.Label(text="", font=35, foreground=GREEN, background=YELLOW)
check_mark.grid(row=3, column=1)



window.mainloop()