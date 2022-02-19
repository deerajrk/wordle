from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
import user_interface.assets.ui_constants as uic
from user_interface.components.play_area.guess_area import GuessTile, TILE_TYPES


class HowToPlay(QDialog):
    def __init__(self):
        super().__init__()
        self._init_howto_play_box()
    
    def _init_howto_play_box(self):
        self.setWindowTitle("How to play WORDLE ?")
        self.setWindowIcon(QIcon(uic.APP_LOGO))
        self.dialog_layout = QVBoxLayout()
        self._set_explaination()
        self.setLayout(self.dialog_layout)

    def _set_explaination(self):
        self.dialog_layout.addWidget(self._get_text("Guess the <b>WORDLE</b> in six tries."))
        self.dialog_layout.addWidget(self._get_text("Each guess must be a valid five-letter word. Hit the enter button to submit."))
        self.dialog_layout.addWidget(self._get_text(" After each guess, the color of the tiles will change to show how close your guess was to the word."))
        self.dialog_layout.addWidget(self._get_hline())
        self.dialog_layout.addWidget(self._get_text("<b>Examples</b>"))
        self.dialog_layout.addWidget(self._add_word_combo("WEARY", "W", TILE_TYPES["POSITION"]))
        self.dialog_layout.addWidget(self._get_text("The letter <b>W</b> is in the word and in the correct spot."))
        self.dialog_layout.addWidget(self._add_word_combo("PILLS", "I", TILE_TYPES["CONTAIN"]))
        self.dialog_layout.addWidget(self._get_text("The letter <b>I</b> is in the word but in the wrong spot."))
        self.dialog_layout.addWidget(self._add_word_combo("VAGUE", "U", TILE_TYPES["WRONG"]))
        self.dialog_layout.addWidget(self._get_text("The letter <b>U</b> is not in the word in any spot."))
        self.dialog_layout.addWidget(self._get_hline())
        self.dialog_layout.addWidget(self._get_text("<b>A new WORDLE will be available with every new game!</b>"))

    @staticmethod
    def _get_text(text):
        title_label = QLabel(text)
        title_label.setStyleSheet("QLabel { color:black; font-size: 14px; }")
        return title_label

    @staticmethod
    def _get_hline():
        h_line = QFrame()
        h_line.setFixedHeight(3)
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        return h_line

    def _add_word_combo(self, word, lt, lt_typ):
        word_combo_widget = QWidget()
        word_combo_layout = QHBoxLayout()
        for i, letter in enumerate(word):
            typ = TILE_TYPES["EMPTY"]
            if letter == lt:
                typ = lt_typ
            word_combo_layout.addWidget(GuessTile(0, i, letter, typ))
        word_combo_widget.setLayout(word_combo_layout)
        word_combo_layout.addStretch(1)
        return word_combo_widget

    def display(self):
        self.exec()