
from question_model import Question
from quiz_brain import QuizBrain

#select file for question data: note, you may have to change the keys in the for loop below accordingly:
from music_data import question_data

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"Quiz is over. Final score: {quiz.user_score}/{quiz.question_number}")