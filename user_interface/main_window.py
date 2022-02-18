from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import user_interface.assets.ui_constants as uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_main_window()

    def _init_main_window(self):
        self.setWindowTitle(uic.APP_TITLE)
        self.setWindowIcon(QIcon(uic.APP_LOGO))
        self.setGeometry(50, 50, 750, 550)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
