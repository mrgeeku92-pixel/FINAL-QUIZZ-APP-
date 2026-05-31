from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem


START_PAGE=0
SELECTION_PAGE=1
QUIZ_PAGE=2
RESULT_PAGE=3

    
class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.quiz_view.next_button.clicked.connect(self.next_question)
        self.view.start_view.start_button.clicked.connect(self.start_quiz)
        self.view.result_view.restart_button.clicked.connect(self.restart)
        self.view.selection_view.theme1_button.clicked.connect(lambda: self.select_theme("Ressources/questions_general.json", "General Knowledge", "Ressources/leaderboard_general.json"))
        self.view.selection_view.theme2_button.clicked.connect(lambda: self.select_theme("Ressources/questions_history.json", "History", "Ressources/leaderboard_history.json"))
        self.view.selection_view.theme3_button.clicked.connect(lambda: self.select_theme("Ressources/questions_science.json", "Science", "Ressources/leaderboard_science.json"))
        
    def update_view(self):
        current_question = self.model.get_current_question()
        current_text_question = current_question["question"]
        total = len(self.model.questions)
        numero = self.model.current_index + 1
        question_text = f"Question {numero}/{total}: {current_text_question}"
        question_type = "multiple" if isinstance(current_question.get("correct"), list) else "single"
        self.view.quiz_view.update_question(question_text, current_question["answers"], question_type)
        self.view.quiz_view.progress_bar.setValue(self.model.current_index + 1)
        self.view.quiz_view.update_score(f"{self.model.score}")
    
    def next_question(self):
        current_question = self.model.get_current_question()
        question_type = "multiple" if isinstance(current_question.get("correct"), list) else "single"
        answer = self.view.quiz_view.get_selected_answers(question_type)
        is_correct = self.model.check_answer(answer)


        if not answer:
            QMessageBox.warning(self.view, "Error", "Warning: You must choose an answer!")
            return

        if is_correct:
            QMessageBox.information(self.view, "Result", "Good job!")
        else:
            QMessageBox.information(self.view, "Result", "Nice try, unfortunately that's incorrect!")


        if self.model.current_index not in self.model.answered_questions:
            self.model.answered_questions.add(self.model.current_index)
            if self.model.current_index + 1 < len(self.model.questions):
                self.model.current_index += 1
                self.update_view()
            else:
                self.show_result()
                self.model.current_leaderboard()
                self.show_leaderboard()

    def start_quiz(self):
        name = self.view.start_view.name_input.text()
        if name == "":
            QMessageBox.warning(self.view, "error", "Please enter a name")
            return 
        self.model.username = name
        self.view.quiz_view.update_welcome(self.model.username)
        self.view.stack.setCurrentIndex(SELECTION_PAGE)
        
    def restart(self):
        self.model.current_index=0
        self.model.score=0
        self.model.answered_questions=set()
        self.model.selected_theme = None
        self.update_view()
        self.view.stack.setCurrentIndex(SELECTION_PAGE)

    def select_theme(self, json_file, theme_name, leaderboard_file):
        """Load the selected theme and its leaderboard"""
        all_questions = self.model.load_questions(json_file, theme_name, leaderboard_file)
        self.model.selected_level = self.get_selected_level()

        # Extract only questions from the selected difficulty level
        self.model.questions = all_questions[self.model.selected_level]
        self.model.current_index = 0
        self.model.score = 0
        self.model.answered_questions = set()
        self.view.quiz_view.progress_bar.setMaximum(len(self.model.questions))
        self.update_view()
        self.view.quiz_view.update_welcome(self.model.username)
        self.view.stack.setCurrentIndex(QUIZ_PAGE)
    
    def get_selected_level(self):
        """Return the currently selected level as a string: 'Easy', 'Medium', or 'Hard'."""
        btn = self.view.selection_view.level_group.checkedButton()
        mapping = {"easy":0, "medium":1, "hard":2}
        return mapping.get(btn.text().lower()) if btn is not None else None

    def show_result(self):
        name = self.model.username
        score = self.model.score
        total = len(self.model.questions) * 5
    
        self.view.result_view.result_label.setText(
            f"{name}, your score is: {score} / {total}"
        )
    
        self.view.stack.setCurrentIndex(RESULT_PAGE)
    
    def show_leaderboard(self):
        table = self.view.result_view.table
        table.setColumnCount(2)
        table.setRowCount(len(self.model.leaderboard))
        table.setHorizontalHeaderLabels(["Username", "Score"])
        for i, entry in enumerate(self.model.leaderboard):
            table.setItem(i, 0, QTableWidgetItem(entry["username"]))
            table.setItem(i, 1, QTableWidgetItem(str(entry["score"])))
        table.resizeColumnsToContents()

