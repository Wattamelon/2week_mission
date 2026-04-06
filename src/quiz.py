"""
퀴즈클래스를 정의 해두는 Py 파일입니다.
"""

class Quiz:
    def __init__(self , id, question, choices , answer , hint  ) :
        self.id = id
        self.question = question
        self.choices = choices
        self.answer = answer 
        self.hint = hint
    
    
    def show_quiz(self):
        print(f"문제 : {self.question}")
        q = self.choices
        print("---------------------")
        print("보기")
        for i in range(len(q)):
            print(f"{i+1}. {q[i]}")
                
    def check_answer(self, user_answer):
        return user_answer == self.answer   
    