from email import header
from urllib.request import HTTPDigestAuthHandler
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import user_interface.assets.ui_constants as uic


class Header(QWidget):
    def __init__(self):
        super().__init__()
        self._init_header()

    def _init_header(self):
        self.setMinimumHeight(75)
        self.setMaximumHeight(75)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self._get_image(uic.APP_LOGO))
        header_layout.addStretch(1)
        header_layout.addWidget(self._get_title())
        header_layout.addStretch(1)
        self.setLayout(header_layout)

    def _get_image(self, img_src):
        logo_label = QLabel(self)
        logo_pixmap = QPixmap(img_src)
        logo_label.setPixmap(logo_pixmap.scaled(70, 70))
        return logo_label

    @staticmethod
    def _get_title():
        title_label = QLabel(uic.APP_HEADING)
        title_label.setStyleSheet("QLabel { color:black; font-size: 40px; }")
        return title_label