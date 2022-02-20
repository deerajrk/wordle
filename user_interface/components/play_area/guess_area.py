from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot
from time import sleep


class GuessArea(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self._init_guess_area()

    def _init_guess_area(self):
        self.guess_area_layout = QGridLayout()
        positions = [(x, y) for x in range(6) for y in range(5)]
        for position in positions:
            self.guess_area_layout.addWidget(GuessTile(*position), *position)
        guess_widget = QWidget()
        guess_widget.setLayout(self.guess_area_layout)
        outer_layout = QHBoxLayout()
        outer_layout.addStretch(1)
        outer_layout.addWidget(guess_widget)
        outer_layout.addStretch(1)
        self.setLayout(outer_layout)

    @pyqtSlot(str, int, int)
    def update_user_input(self, ch, x, y):
        guess_tile = self.guess_area_layout.itemAt(x + y * 5).widget()
        guess_tile.update_letter(ch)

    @pyqtSlot(int, int)
    def update_backspace(self, x, y):
        guess_tile = self.guess_area_layout.itemAt(x + y * 5).widget()
        guess_tile.update_letter("")

    @pyqtSlot(list, int)
    def update_guess_word(self, word_info, y):
        for info in word_info:
            tile = self.guess_area_layout.itemAt(y * 5 + info["x"]).widget()
            tile.type = info["typ"]
            tile.update_frame_style()

    @pyqtSlot()
    def clear_guess_area(self):
        tiles = (self.guess_area_layout.itemAt(i).widget() for i in range(self.guess_area_layout.count())) 
        for tile in tiles:
            tile.update_letter("")
            tile.type = TILE_TYPES["EMPTY"]
            tile.update_frame_style()


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

    def update_letter(self, letter):
        self.letter = letter
        self.title_label.setText(self.letter)

    def update_frame_style(self):
        if self.type == 0:
            self.setStyleSheet("QFrame { background-color: white; }")
            self.title_label.setStyleSheet("QLabel { color: black; }")
        elif self.type == 1:
            self.setStyleSheet("QFrame { background-color: #787C7E; }")
            self.title_label.setStyleSheet("QLabel { color: white; }")
        elif self.type == 2:
            self.setStyleSheet("QFrame { background-color: #C9B458; }")
            self.title_label.setStyleSheet("QLabel { color: white; }")
        elif self.type == 3:
            self.setStyleSheet("QFrame { background-color: #6AAA64; }")
            self.title_label.setStyleSheet("QLabel { color: white; }")

    def _get_text(self, text):
        self.title_label = QLabel(text)
        if self.type == 0:
            text_color = "black"
        else:
            text_color = "white"
        self.title_label.setStyleSheet("QLabel { color:black; font-size: 14px;  color: " + text_color + "; }")
        return self.title_label

    def setTileColor(self):
        self.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.update_frame_style()
