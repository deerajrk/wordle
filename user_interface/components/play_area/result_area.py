from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot


class ResultArea(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self._init_result_area()

    def _init_result_area(self):
        result_area_layout = QHBoxLayout() 
        result_area_layout.addStretch(1)
        result_area_layout.addWidget(self._get_info_widget())
        result_area_layout.addStretch(1)
        self.setLayout(result_area_layout)

    def _get_info_widget(self):
        self.info_label = QLabel()
        self.info_label.setStyleSheet("QLabel { color:black; font-size: 14px; }")
        return self.info_label

    @pyqtSlot(str, str)
    def update_result_info(self, message, color):
        self.info_label.setText(message)
        self.info_label.setStyleSheet("QLabel { color: " + color + "; }")