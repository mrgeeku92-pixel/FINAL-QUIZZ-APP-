from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QRadioButton, QCheckBox, QButtonGroup, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.question_label = QLabel("")
        
        #-----Background---"
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Ressources/quizview.jpg")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()
        
        self.question_label.setObjectName("questionLabel")
        
        welcome_layout= QHBoxLayout()
        self.welcome_label = QLabel("")
        self.welcome_label.setObjectName("scoreLabel")

        header_layout = QHBoxLayout()
        self.score_label1 = QLabel("Score:")
        self.score_label2 = QLabel("0")
        
        self.score_label1.setObjectName("scoreLabel")
        self.score_label2.setObjectName("scoreLabel")
        
        welcome_layout.addWidget(self.welcome_label)
        header_layout.addWidget(self.question_label)
        header_layout.addStretch() # pousse le score à droite
        header_layout.addWidget(self.score_label1)
        header_layout.addWidget(self.score_label2)
        
        #-------answer layout-------
        self.answer_layout = QVBoxLayout()
        self.button_group = QButtonGroup()
        self.radio_buttons = []
        self.check_boxes = []
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")
        self.answer_layout.addWidget(self.progress_bar)

        for _ in range(4):
            rb = QRadioButton("")
            cb = QCheckBox("")
            self.button_group.addButton(rb)
            self.radio_buttons.append(rb)
            self.check_boxes.append(cb)
            self.answer_layout.addWidget(rb)
            self.answer_layout.addWidget(cb)
        
        #------Layout navigation---------
        self.navigation_layout=QHBoxLayout()
        self.next_button=QPushButton("Suivant")
        self.navigation_layout.addWidget(self.next_button)
        self.navigation_layout.setSpacing(30)

        #-----main-layout------
        main_layout = QVBoxLayout()
        main_layout.addLayout(welcome_layout)
        main_layout.addLayout(header_layout)
        main_layout.addLayout(self.answer_layout)
        main_layout.addLayout(self.navigation_layout)
        main_layout.setAlignment(Qt.AlignCenter) #2
        self.setLayout(main_layout)
        #--------style--------

        self.answer_layout.setSpacing(20)
        self.navigation_layout.setSpacing(30)
        
    def update_question(self, question, answers, question_type="single"):
        self.question_label.setText(question)

        if question_type == "multiple":
            for rb, cb in zip(self.radio_buttons, self.check_boxes):
                rb.hide()
                cb.show()
                cb.setChecked(False)

            for index, text in enumerate(answers):
                self.check_boxes[index].setText(text)
                self.check_boxes[index].show()

            for index in range(len(answers), len(self.check_boxes)):
                self.check_boxes[index].hide()
        else:
            for rb, cb in zip(self.radio_buttons, self.check_boxes):
                cb.hide()
                rb.show()
                rb.setChecked(False)

            for index, text in enumerate(answers):
                self.radio_buttons[index].setText(text)
                self.radio_buttons[index].show()

            for index in range(len(answers), len(self.radio_buttons)):
                self.radio_buttons[index].hide()

    def get_selected_answers(self, question_type="single"):
        if question_type == "multiple":
            return [cb.text() for cb in self.check_boxes if cb.isChecked()]

        selected_button = self.button_group.checkedButton()
        return selected_button.text() if selected_button else None

    def update_score(self, score):
        self.score_label2.setText(score)

    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)
        
    def update_welcome(self, name):
        self.welcome_label.setText(f"Hello {name}")
