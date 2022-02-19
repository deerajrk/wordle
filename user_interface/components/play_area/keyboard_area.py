from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLabel
import user_interface.assets.ui_constants as uic 


class KeyboardArea(QWidget):
    def __init__(self):
        super().__init__()
        self._init_keyboard_area()

    def _init_keyboard_area(self):
        self.keyboard_area_layout = QVBoxLayout()
        self._set_keyboards()
        self.setLayout(self.keyboard_area_layout)

    def _set_keyboards(self):
        row1 = self._set_row(uic.KEYBOARD_FIRST_ROW)
        row2 = self._set_row(uic.KEYBOARD_SECOND_ROW)
        row3 = self._set_row(uic.KEYBOARD_THIRD_ROW)
        self.keyboard_area_layout.addWidget(row1)
        self.keyboard_area_layout.addWidget(row2)
        self.keyboard_area_layout.addWidget(row3)

    def _set_row(self, key_list):
        row = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addStretch(1)
        for key in key_list:
            single_key = Key(key)
            row_layout.addWidget(single_key)
        row_layout.addStretch(1)
        row.setLayout(row_layout)
        return row


class Key(QFrame):
    def __init__(self, value, type = None):
        super().__init__()
        self.value = value
        self.type = type
        self._init_key()

    def _init_key(self):
        key_layout = QHBoxLayout()
        key_label = QLabel(self.value)
        key_layout.addStretch(1)
        key_layout.addWidget(key_label)
        key_layout.addStretch(1)
        key_label.setStyleSheet("QLabel { color:black; font-size: 18px; }")
        self.setLayout(key_layout)
        self.setFixedHeight(40)
        self.setMinimumWidth(35)
        self.setStyleSheet("QFrame { background-color: #D3D6DA; }")
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)