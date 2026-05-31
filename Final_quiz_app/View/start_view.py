from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pathlib import Path


class StartView(QWidget):

    def __init__(self):

        super().__init__()
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(500)
        self.name_input.setPlaceholderText("Enter your name...")
        
        self.setObjectName("startScreen")
        
        #------- Background Image ---------
        project_root = Path(__file__).resolve().parent.parent
        image_path = project_root / "Ressources" / "startScreen.jpeg"
        pixmap = QPixmap(str(image_path))

        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.lower()
        self.bg_label.show()
                
        self.layout = QVBoxLayout()
        self.title = QLabel("Welcome to the Quiz")
        self.start_button = QPushButton("Start")

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.start_button)
        self.layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.layout)
        
    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)