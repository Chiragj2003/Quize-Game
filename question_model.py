class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("True", "False")
print(new_q.text)
