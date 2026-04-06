from src.quiz_data import quiz_data
from src.quiz import Quiz
import json
from pathlib import Path

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
    
    def load_quizzes(self):
        try : 
            path = Path("state.json")
            quiz_list = []
            with path.open("r",encoding='utf-8') as f:
                json_data = json.load(f)
            for i in json_data["quizzes"]:
                tmp = Quiz(i["id"],i["question"],i["choices"],i["answer"],i["hint"])
                quiz_list.append(tmp)
            self.quizzes = quiz_list
            self.best_score = json_data["best_score"]
            
        except : 
            self.quizzes = quiz_data()
            self.best_score = 0
            
    def show_quizzes(self):
        if len(self.quizzes) == 0:
            print("등록된 문제가 존재하지 않습니다.")

        else: 
            print(f"총 {len(self.quizzes)}문제")
            print("-------------------------")

            for i in self.quizzes :
                print(f" {i.id}번 문제") # 추후에 삭제할수도
                print(f" 문제 : {i.question}")
                print("-------------------------")
    
    def play_quiz(self):
        player_score = 0 
        
        for quiz in self.quizzes:
            while True:
                quiz.show_quiz()
                try:
                    user_answer = int(input().strip())
                    if user_answer <= 0 or user_answer >= 5 :
                        print("1~4 사이의 숫자를 입력 해주십시오.")
                        continue
                    if quiz.check_answer(user_answer):
                        player_score += 100
                        print("정답입니다. 점수가 100점 추가 되었습니다.")
                        break
                    else:
                        player_score -= 10
                        print("오답입니다. 점수가 10점 감소 되었습니다.")
                        print(f"정답은 {quiz.answer}번 입니다.")
                        break
                except :
                    print("올바른 숫자를 입력 해주십시오.")              
    
        if player_score > self.best_score :
            print(f"최고 기록입니다! 당신의 점수는 {player_score}점 입니다.")
            self.best_score = player_score
        else:
            print(f"당신의 점수는 {player_score}점 입니다. 다음에는 최고 점수를 노려보세요!")  
        self.save_data()    
            
    def save_data(self):
        save_quizzes = []
        quizzies_sort = sorted(self.quizzes, key = lambda x : x.id)
        for quiz in quizzies_sort:
            quiz_dict = {}
            quiz_dict["id"] = quiz.id
            quiz_dict["question"] = quiz.question
            quiz_dict["choices"] = quiz.choices
            quiz_dict["answer"] = quiz.answer
            quiz_dict["hint"] = quiz.hint
            save_quizzes.append(quiz_dict)
        save_dict = {}
        save_dict["quizzes"] = save_quizzes
        save_dict["best_score"] = self.best_score
        
        with open('state.json','w' , encoding = 'utf-8') as f :
            json.dump(save_dict,f,indent=4,ensure_ascii=False)


            
        
        