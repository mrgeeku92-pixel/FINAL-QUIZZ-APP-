#main.py

import sys
# Main class for the PyQt5 application
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
# Import the main application window
from View.quiz_view import QuizView
from View.start_view import StartView
from View.result_view import ResultView
from View.selection_view import SelectionView
from Controller.quiz_controller import QuizController
from Model.quiz_model import QuizModel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.quiz_view = QuizView()
        self.start_view = StartView()
        self.selection_view = SelectionView()
        self.result_view = ResultView()
        self.setFixedSize(800,600)
        #add widgets to the stack
        self.stack.addWidget(self.start_view)
        self.stack.addWidget(self.selection_view)
        self.stack.addWidget(self.quiz_view)
        self.stack.addWidget(self.result_view)
        # Create a vertical layout to contain the QStackedWidget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.stack)
        self.setLayout (layout)



app = QApplication(sys.argv) # Creates the application
app.setWindowIcon(QIcon("Ressources/quizicon.png"))
with open("Ressources/style.qss") as f:
    app.setStyleSheet(f.read())
#setup app
model = QuizModel()
window = MainWindow() # Creates the window
controller = QuizController(model, window)
#launch the app
window.show() # Displays the window
sys.exit(app.exec_()) # Starts the application loop and exits cleanly