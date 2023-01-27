import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_COLOR = "#FFFAF0"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = tkinter.Label(padx=20, text="Score : 0", background=THEME_COLOR, foreground=SCORE_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=270)
        self.question = self.canvas.create_text(
            150,
            100,
            width=280,
            text="hello~~~",
            font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=true_button_image, highlightthickness=0, background=THEME_COLOR, command=self.true_check_question)
        self.true_button.grid(row=2, column=0)

        false_button_image = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=false_button_image, highlightthickness=0, background=THEME_COLOR, command=self.false_check_question)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="End of questions!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(background="white")

    def true_check_question(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_check_question(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(background="green")
            self.score_label.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)



