from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout


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


class GuessTile(QFrame):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self._init_guess_tile()

    def _init_guess_tile(self):
        self.setFixedHeight(40)
        self.setFixedWidth(40)
        self.setFrameStyle(QFrame.Box | QFrame.Plain)