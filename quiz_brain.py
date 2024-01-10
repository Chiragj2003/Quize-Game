class QuizBrain:
    def __init__(self , q_list):
         self.question_number = 0
         self.score = 0
         self.question_list = q_list

    def still_has_question(self):
        return len(self.question_list) > self.question_number
 

    def next_question(self):
         current_question = self.question_list[self.question_number]
         self.question_number +=1
         user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False) :  ")
         self.check_answer(user_answer, current_question.answer)

    def check_answer(self , user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right ! ")
        else:
            print(f"the correct answer is : {correct_answer}")
            print(f"Your current score is : {self.score}/{self.question_number}")   
