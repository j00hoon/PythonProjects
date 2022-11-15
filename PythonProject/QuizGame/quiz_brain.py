class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_question(self):
        if len(self.questions_list) > self.question_number:
            return True
        return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = str(input(f"Q.{self.question_number}: {current_question.question}. (True/False)?: "))
        self.check_answer(answer, current_question.correct_answer)

    def check_answer(self, answer, q_answer):
        if answer.lower() == q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
