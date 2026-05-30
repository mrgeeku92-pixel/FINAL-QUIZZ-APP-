import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QPushButton,QButtonGroup
from PyQt5.QtCore import Qt 

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightblue;")
        
        main_layout = QVBoxLayout()
        self.question_label = QLabel("What is the capital of France?", self)
        self.question_label.setAlignment(Qt.AlignCenter) 
        main_layout.addWidget(self.question_label)
        
        self.setLayout(main_layout)
        
        answer_layout = QVBoxLayout()
        main_layout.addLayout(answer_layout)
        self.paris_button=QRadioButton("Paris",self)
        self.amsterdam_button=QRadioButton("Amsterdam",self)
        self.alger_button=QRadioButton("Alger",self)
        self.brasil_button=QRadioButton("Brasil",self)
        answer_layout.addWidget(self.paris_button)
        answer_layout.addWidget(self.amsterdam_button)
        answer_layout.addWidget(self.alger_button)
        answer_layout.addWidget(self.brasil_button)
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.paris_button)
        self.button_group.addButton(self.amsterdam_button)
        self.button_group.addButton(self.alger_button)
        self.button_group.addButton(self.brasil_button)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        self.previous=QPushButton("Previous",self)
        self.next=QPushButton("Next",self)
        button_layout.addWidget(self.previous)
        button_layout.addWidget(self.next)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizView()
    window.show()
    sys.exit(app.exec_())




