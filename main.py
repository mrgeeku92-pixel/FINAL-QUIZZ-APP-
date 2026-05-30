import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from quizz_view import QuizView
from quizz_model import QuizModel
from quizz_controller import QuizController

app = QApplication(sys.argv)
model = QuizModel()
view = QuizView()
controller = QuizController(model,view)
view.show()
sys.exit(app.exec_())