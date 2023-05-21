from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    quiz.still_has_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")