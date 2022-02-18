import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from user_interface.main_window import MainWindow

class AppManager(QObject):
    def __init__(self):
        super().__init__()
        print("AppManager initiated")

    def start_gui():
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())
