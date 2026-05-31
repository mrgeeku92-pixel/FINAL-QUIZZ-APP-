from PyQt5.QtWidgets import QButtonGroup, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pathlib import Path


class SelectionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("selectionScreen")
        
        layout = QVBoxLayout()

        # Theme Level layout (vertical)
        level_label = QLabel("Difficulty Level:")
        level_label.setAlignment(Qt.AlignCenter)
        
        level_layout = QVBoxLayout()
        level_layout.addWidget(level_label)
        level_group = QButtonGroup()
        self.level_easy_button = QPushButton("Easy")
        self.level_medium_button = QPushButton("Medium")
        self.level_hard_button = QPushButton("Hard")

        # Make them checkable and add to an exclusive button group
        for btn in (self.level_easy_button, self.level_medium_button, self.level_hard_button):
            btn.setCheckable(True)
            btn.setObjectName("levelButton")
            level_group.addButton(btn)

        level_group.setExclusive(True)
        self.level_group = level_group

        # Layout the level buttons horizontally under the label
        level_buttons_layout = QHBoxLayout()
        level_buttons_layout.addWidget(self.level_easy_button)
        level_buttons_layout.addWidget(self.level_medium_button)
        level_buttons_layout.addWidget(self.level_hard_button)

        # Default selection
        self.level_easy_button.setChecked(True)
        
        # Title label
        title_label = QLabel("Please select a quiz theme:")
        title_label.setAlignment(Qt.AlignCenter)
        
        # Theme button layout (horizontal)
        button_layout = QHBoxLayout()
        
        # Theme 1 Button
        self.theme1_button = QPushButton(icon=QIcon("Ressources/generalicon.png"), text="General Knowledge")
        self.theme1_button.setObjectName("themeButton")
        button_layout.addWidget(self.theme1_button)
        
        # Theme 2 Button
        self.theme2_button = QPushButton(icon=QIcon("Ressources/historyicon.png"), text="History")
        self.theme2_button.setObjectName("themeButton")
        button_layout.addWidget(self.theme2_button)
        
        # Theme 3 Button
        self.theme3_button = QPushButton(icon=QIcon("Ressources/scienceicon.png"), text="Science")
        self.theme3_button.setObjectName("themeButton")
        button_layout.addWidget(self.theme3_button)


        
        layout.addLayout(level_layout)
        layout.addLayout(level_buttons_layout)
        layout.addWidget(title_label)
        layout.addLayout(button_layout)
        layout.addStretch()
        
        self.setLayout(layout)


