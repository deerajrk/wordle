from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout, QLabel
from enum import Enum


class GuessArea(QWidget):
    def __init__(self):
        super().__init__()
        self._init_guess_area()

    def _init_guess_area(self):
        guess_area_layout = QGridLayout()
        positions = [(x, y) for x in range(6) for y in range(5)]
        for position in positions:
            guess_area_layout.addWidget(GuessTile(*position), *position)
        guess_widget = QWidget()
        guess_widget.setLayout(guess_area_layout)
        outer_layout = QHBoxLayout()
        outer_layout.addStretch(1)
        outer_layout.addWidget(guess_widget)
        outer_layout.addStretch(1)
        self.setLayout(outer_layout)


TILE_TYPES = {
    "EMPTY": 0,
    "WRONG": 1,
    "CONTAIN": 2,
    "POSITION": 3
}

class GuessTile(QFrame):
    def __init__(self, x, y, letter="", type = TILE_TYPES["EMPTY"]):
        super().__init__()
        self.x = x
        self.y = y
        self.letter = letter
        self.type = type
        self._init_guess_tile()

    def _init_guess_tile(self):
        self.setFixedHeight(40)
        self.setFixedWidth(40)
        self.tile_layout = QHBoxLayout()
        self.setLetter()
        self.setTileColor()

    def setLetter(self):
        self.tile_layout.addStretch(1)
        self.tile_layout.addWidget(self._get_text(self.letter))
        self.tile_layout.addStretch(1)
        self.setLayout(self.tile_layout)

    def _get_text(self, text):
        title_label = QLabel(text)
        if self.type == 0:
            text_color = "black"
        else:
            text_color = "white"
        title_label.setStyleSheet("QLabel { color:black; font-size: 14px;  color: " + text_color + "; }")
        return title_label

    def setTileColor(self):
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        
        if self.type == 0:
            self.setStyleSheet("QFrame { background-color: white; }")
        elif self.type == 1:
            self.setStyleSheet("QFrame { background-color: #787C7E; }")
        elif self.type == 2:
            self.setStyleSheet("QFrame { background-color: #C9B458; }")
        elif self.type == 3:
            self.setStyleSheet("QFrame { background-color: #6AAA64; }")
