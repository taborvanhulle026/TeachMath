class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def check_answer(self, user_answer):
        return self.answer == user_answer

# 示例测验
def create_quizzes():
    quiz1 = Quiz("What is the value of x in the equation 2x + 3 = 7?", "2")
    quiz2 = Quiz("What is the sum of the angles in a triangle?", "180")
    return [quiz1, quiz2]
