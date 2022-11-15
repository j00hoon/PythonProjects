from question_model import Question
from data import question_data
import quiz_brain



def create_question_bank(question_list):

    for i in question_data["results"]:
        question_tmp = Question(i["question"], i["correct_answer"])
        question_list.append(question_tmp)

    return question_list


question_list = []
question_list = create_question_bank(question_list)

quiz_brain = quiz_brain.QuizBrain(question_list)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")