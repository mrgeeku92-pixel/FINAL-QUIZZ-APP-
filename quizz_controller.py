from PyQt5.QtWidgets import QMessageBox
class QuizController:
    def __init__(self, model, view):
        self.model = model 
        self.view = view
        self.view.next.clicked.connect(self.next_question)
    
    
    def next_question(self):
        selected_button = self.view.button_group.checkedButton()

        if selected_button is None:
            QMessageBox.warning(self.view, "Selection Required", "Please select an answer!")
            return

        answer = selected_button.text()
        is_correct = self.model.check_answer(answer)

        if is_correct:
            QMessageBox.information(self.view, "Result", "Good job!")
        else:
            QMessageBox.information(self.view, "Result", "Nice try!")

        self.model.current_index += 1

        if self.model.current_index < len(self.model.questions):
            new_q = self.model.questions[self.model.current_index]
            
            self.view.question_label.setText(new_q["question"])
            
            self.view.paris_button.setText(new_q["answers"][0])
            self.view.amsterdam_button.setText(new_q["answers"][1])
            self.view.alger_button.setText(new_q["answers"][2])
            self.view.brasil_button.setText(new_q["answers"][3])
            
            self.view.button_group.setExclusive(False)
            selected_button.setChecked(False)
            self.view.button_group.setExclusive(True)
        else:
            QMessageBox.information(self.view, "Quiz Finished", f"Final Score: {self.model.score}")