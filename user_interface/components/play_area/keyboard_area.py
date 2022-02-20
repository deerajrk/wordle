from turtle import clear
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLabel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QMouseEvent
import user_interface.assets.ui_constants as uic
from PyQt5.QtCore import pyqtSlot


class KeyboardArea(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self._init_keyboard_area()

    def _init_keyboard_area(self):
        self.keyboard_area_layout = QVBoxLayout()
        self._set_keyboards()
        self.setLayout(self.keyboard_area_layout)

    def _set_keyboards(self):
        self.row1 = self._set_row(uic.KEYBOARD_FIRST_ROW)
        self.row2 = self._set_row(uic.KEYBOARD_SECOND_ROW)
        self.row3 = self._set_row(uic.KEYBOARD_THIRD_ROW)
        self.keyboard_area_layout.addWidget(self.row1)
        self.keyboard_area_layout.addWidget(self.row2)
        self.keyboard_area_layout.addWidget(self.row3)

    def _set_row(self, key_list):
        row = QWidget()
        row_layout = QHBoxLayout()
        row_layout.addStretch(1)
        for key in key_list:
            single_key = Key(self.mw, key)
            row_layout.addWidget(single_key)
        row_layout.addStretch(1)
        row.setLayout(row_layout)
        return row

    @pyqtSlot()
    def clear_keyboard(self):
        def clear_keys(keys):
            for key in keys:
                if key is not None:
                    key.typ = 0
                    key.update_key_layout()
        row1_keys = (self.row1.layout().itemAt(i).widget() for i in range(self.row1.layout().count()))
        clear_keys(row1_keys)
        row2_keys = (self.row2.layout().itemAt(i).widget() for i in range(self.row2.layout().count()))
        clear_keys(row2_keys)
        row3_keys = (self.row3.layout().itemAt(i).widget() for i in range(self.row3.layout().count()))
        clear_keys(row3_keys)

    @pyqtSlot(list, int)
    def update_keyboard(self, wordsinfo, int):
        for w in wordsinfo:
            letter = w["letter"]
            typ = w["typ"]
            key = None
            if letter in uic.KEYBOARD_FIRST_ROW:
                i = uic.KEYBOARD_FIRST_ROW.index(letter)
                key = self.row1.layout().itemAt(i + 1).widget()
            elif letter in uic.KEYBOARD_SECOND_ROW:
                i = uic.KEYBOARD_SECOND_ROW.index(letter)
                key = self.row2.layout().itemAt(i + 1).widget()
            elif letter in uic.KEYBOARD_THIRD_ROW:
                i = uic.KEYBOARD_THIRD_ROW.index(letter)
                key = self.row3.layout().itemAt(i + 1).widget()
            if key is not None:
                if key.typ < typ:
                    key.typ = typ
                key.update_key_layout()


class Key(QFrame):
    def __init__(self, mw, value, typ = 0):
        super().__init__()
        self.mw = mw
        self.value = value
        self.typ = typ
        self._init_key()

    def _init_key(self):
        key_layout = QHBoxLayout()
        self.key_label = QLabel(self.value)
        key_layout.addStretch(1)
        key_layout.addWidget(self.key_label)
        key_layout.addStretch(1)
        self.key_label.setStyleSheet("QLabel { color:black; font-size: 18px; }")
        self.setLayout(key_layout)
        self.setFixedHeight(40)
        self.setMinimumWidth(35)
        self.update_key_layout()
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, QMouseEvent):
        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.mw.emit_key(self.value)

    def mouseReleaseEvent(self, QMouseEvent):
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)

    def update_key_layout(self):
        if self.typ == 0:
            self.setStyleSheet("QFrame { background-color: #D3D6DA; }")
            self.key_label.setStyleSheet("QLabel { color: black; }")
        elif self.typ == 1:
            self.setStyleSheet("QFrame { background-color: #787C7E; }")
            self.key_label.setStyleSheet("QLabel { color: white; }")
        elif self.typ == 2:
            self.setStyleSheet("QFrame { background-color: #C9B458; }")
            self.key_label.setStyleSheet("QLabel { color: white; }")
        elif self.typ == 3:
            self.setStyleSheet("QFrame { background-color: #6AAA64; }")
            self.key_label.setStyleSheet("QLabel { color: white; }")
        