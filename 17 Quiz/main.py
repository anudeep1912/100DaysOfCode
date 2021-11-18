from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_ans = question['answer']
    question_bank.append(Question(question_text, question_ans))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.ask_question_and_check_answer()

print("You have completed the Quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")