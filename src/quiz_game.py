from src.quiz_data import quiz_data
from src.quiz import Quiz
import json
from pathlib import Path

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
    
    def load_quiz(self):
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
