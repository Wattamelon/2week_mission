from src.quiz_data import quiz_data
from src.quiz import Quiz
import json
from pathlib import Path
from random import shuffle
import time 

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.play_logs = []
    
    def load_quizzes(self):
        try : 
            path = Path("state.json")
            quiz_list = []
            with path.open("r",encoding='utf-8') as f:
                json_data = json.load(f)
            for i in json_data["quizzes"]:
                tmp = Quiz(i["id"],i["question"],i["choices"],i["answer"],i["hint"])
                quiz_list.append(tmp)
            if len(quiz_list) < 5:
                self.quizzes = quiz_data()
            else:
                self.quizzes = quiz_list
            self.best_score = json_data["best_score"]
            if "play_logs" in json_data and json_data["play_logs"] :
                self.play_logs = json_data["play_logs"]
            else: 
                self.play_logs = []
            
        except : 
            self.quizzes = quiz_data()
            self.best_score = 0
            self.play_logs = []
            print("저장 파일을 불러오는 중 문제가 발생하여 기본 퀴즈로 복구했습니다.")
            self.save_data()
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
    
    def play_quiz(self,shuffled_quizzes):
        player_score = 0 
        use_hint = 2
        for quiz in shuffled_quizzes:
            while True:
                quiz.show_quiz()
                try:
                    user_answer = int(input().strip())
                    if user_answer <= 0 or user_answer > 5 :
                        print("1~5 사이의 숫자를 입력 해주십시오.")
                        continue
                    elif user_answer == 5 :
                        if use_hint == 0 :
                            print("더이상 사용 가능한 힌트가 없습니다.")
                            continue
                        else: 
                            print(quiz.hint)
                            use_hint -= 1
                            print(f"남은 힌트 수는 {use_hint}개 입니다.")
                            continue
                    elif quiz.check_answer(user_answer):
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
        #break_score = False
        if player_score > self.best_score :
            print(f"최고 기록입니다! 당신의 점수는 {player_score}점 입니다.")
            self.best_score = player_score
            #break_score = True
        else:
            print(f"당신의 점수는 {player_score}점 입니다. 다음에는 최고 점수를 노려보세요!")  
        self.play_logs.append({"playtime" : time.strftime('%Y.%m.%d - %H:%M:%S') , "num_solved" : len(shuffled_quizzes) , "score" : player_score})
        
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
        save_dict["play_logs"] = self.play_logs
        
        with open('state.json','w' , encoding = 'utf-8') as f :
            json.dump(save_dict,f,indent=4,ensure_ascii=False)
            
    def add_quiz(self):
        question_id = self.quizzes[-1].id + 1
        print("문제를 입력하세요.")
        question = self.check_empty("문제")
        print("보기1 입력.")
        c_1 = self.check_empty("보기1")
        print("보기2 입력.")
        c_2 = self.check_empty("보기2")
        print("보기3 입력.")
        c_3 = self.check_empty("보기3")
        print("보기4 입력.")
        c_4 = self.check_empty("보기4")
        print("정답을 입력하세요.")
        while True:
            answer = input().strip()
            if answer.isdigit():
                answer = int(answer)
            else:
                print("정답은 숫자만 입력됩니다.")
                continue
            if answer > 0 and answer < 5:
                break
            else:
                print("1~4 사이의 숫자를 입력하세요.")
                               
        print("힌트를 입력하세요.")
        hint = self.check_empty("힌트")     
        quiz = Quiz(question_id,question,[c_1,c_2,c_3,c_4],answer,hint)
        self.quizzes.append(quiz)  
        self.save_data()
        print("퀴즈 추가가 완료 되었습니다.")
        

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
            print("=============================")
            print("보너스 문제 존")
            print("6. 문제 수 정하기")
            print("7. 문제 삭제하기")
            try: 
                print("원하는 메뉴 번호를 입력하세요.")
                tmp = int(input().strip())
                print("=============================")
                if tmp == 1:
                    shuffled_quizzes = self.quizzes[:]
                    shuffle(shuffled_quizzes)
                    self.play_quiz(shuffled_quizzes)
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
                elif tmp == 6:
                    while True:
                        print("도전할 문제 수를 입력하세요.")
                        n = input().strip()
                        if not n.isdigit() :
                            print("정수를 입력 해주세요.")
                            continue
                        n = int(n)
                        if n > len(self.quizzes) or n <= 0:
                            print("도전할 문제 수가 올바르지 않습니다.")
                            continue
                        else:
                            self.play_n_quizzes(n)
                            break
                elif tmp == 7 :
                    self.delete_quiz()
                    
                else:
                    print("잘못된 입력입니다. 1~7 사이의 숫자를 입력해주세요.")
            except KeyboardInterrupt:
                self.save_data()
                print("입력이 중단되었습니다. 프로그램을 종료합니다.")
                break
            except EOFError:
                self.save_data()
                print("입력을 받을 수 없습니다. 프로그램을 종료합니다.")
                break
            except:
                print("1~7사이의 숫자를 입력 해주세요.")

            print("=============================")
    
    def show_best_score(self):
        print(f"점수는 {self.best_score}점 입니다.")

    def check_empty(self,kind):
        while True :
            text = input().strip()
            if text == "":
                print(f"{kind}를 다시 입력하세요. (공백 불가)")
            else:
                return text
    
    def shuffle_quizzes(self):
        
        shuffled_quizzes = self.quizzes[:]
        shuffle(shuffled_quizzes)
        return shuffled_quizzes
        
        
    def play_n_quizzes(self,n):
        shuffled_quizzes = self.shuffle_quizzes()
        self.play_quiz(shuffled_quizzes[:n])
        
            
    def delete_quiz(self):
        
        if len(self.quizzes) == 0 :
            print("퀴즈가 존재하지 않습니다.")
            return
            
        while True : 
            print("삭제할 문제의 번호를 입력하세요.")
            n = self.check_empty("문제 번호")
            if not n.isdigit():
                print("정수를 입력하세요.")
                continue
            else:
                n = int(n)
                break


        q_id_list = []
        for i in self.quizzes:
            q_id_list.append(i.id)
        if n not in q_id_list:
            print("선택하신 번호의 문제가 존재하지 않습니다.")
        else:
            for quiz in self.quizzes:
                if quiz.id == n:
                    self.quizzes.remove(quiz)
                    break
            print("선택하신 번호의 문제가 삭제 되었습니다.")
            self.save_data()
            