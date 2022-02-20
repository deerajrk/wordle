import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from user_interface.main_window import MainWindow
from game_engine.game_manager import GameManager

class AppManager(QObject):
    def __init__(self):
        super().__init__()
        print("AppManager initiated")

    def start_gui(self):
        app = QApplication(sys.argv)
        self.main_window = MainWindow(self)
        self.main_window.show()
        self.start_game()
        sys.exit(app.exec_())

    def start_game(self):
        self.game_manager = GameManager(self)
        self.game_manager.start()
        self.connect_singal_slot()

    def connect_singal_slot(self):
        self.main_window.emit_single_key.connect(self.game_manager.register_single_key)
