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
            
    def add_quiz(self):
        print("퀴즈 추가 미구현")

    def run_menu(self):
        self.load_quizzes()
        while True:
            print("=============================")
            print("2주차 과제 퀴즈풀이")
            print("안내 : 코디세이 2주차 과제용 퀴즈입니다. 숫자를 선택해주세요.")
            print("=============================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            try: 
                print("원하는 메뉴 번호를 입력하세요.")
                tmp = int(input().strip())
                print("=============================")
                if tmp == 1:
                    self.play_quiz()
                elif tmp == 2:
                    self.add_quiz()
                elif tmp == 3:
                    self.show_quizzes()
                elif tmp == 4:
                    self.show_best_score()
                elif tmp == 5: 
                    print("프로그램을 종료합니다.")
                    self.save_data()
                    break
                else:
                    print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
            except KeyboardInterrupt:
                print("입력이 중단되었습니다. 프로그램을 종료합니다.")
                break
            except EOFError:
                print("입력을 받을 수 없습니다. 프로그램을 종료합니다.")
                break
            except:
                print("1~5사이의 숫자를 입력 해주세요.")

            print("=============================")
    
    def show_best_score(self):
        print(f"점수는 {self.best_score}점 입니다.")

            
        
        