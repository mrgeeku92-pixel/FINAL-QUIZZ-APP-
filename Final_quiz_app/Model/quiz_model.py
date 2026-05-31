import json
from PyQt5.QtWidgets import QMessageBox

class QuizModel :
    def __init__(self, json_file="Ressources/questions_general.json", username=""):
        self.username = username
        # Default list of questions if no file is provided
        self.questions=self.load_questions(json_file)
        self.current_index=0
        self.score=0
        self.answered_questions=set()

        self.selected_theme = None
        self.selected_leaderboard_file = None
        self.leaderboard = []
        self.selected_level = 0
        
    def get_current_question(self):
        return self.questions[self.current_index]
        
    def check_answer(self, answer):
        if answer==self.get_current_question()["correct"]:
            # Score based on difficulty: Easy=5, Medium=10, Hard=15
            score_multipliers = {0: 5, 1: 10, 2: 15}
            self.score += score_multipliers.get(self.selected_level, 5)
            return True
        return False

    def load_questions(self, json_file, theme_name=None, leaderboard_file=None):
        with open(json_file,"r", encoding="utf-8") as file:
            data = json.load(file)
            self.questions = data
            if theme_name is not None:
                self.selected_theme = theme_name
            if leaderboard_file is not None:
                self.load_leaderboard(leaderboard_file)
            return data
    
    def load_leaderboard(self, json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            self.leaderboard = json.load(file)
            self.selected_leaderboard_file = json_file
            return self.leaderboard
    
    def save_leaderboard(self):
        if not self.selected_leaderboard_file:
            return
        with open(self.selected_leaderboard_file, "w", encoding="utf-8") as file:
            json.dump(self.leaderboard, file, indent=2, ensure_ascii=False)

    def current_leaderboard(self):
        # Ensure a leaderboard list is available for the selected theme
        if self.leaderboard is None:
            self.leaderboard = []
        
        if any (entry["username"] == self.username for entry in self.leaderboard):
            index = next(i for i, entry in enumerate(self.leaderboard) if entry["username"] == self.username)
            self.leaderboard[index]["score"] = max(self.leaderboard[index]["score"], self.score)
        else:
            self.leaderboard.append({"username": self.username, "score": self.score})
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x["score"], reverse=True)
        # Persist to the selected leaderboard file (if set)
        self.save_leaderboard()
        return self.leaderboard

    