import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from user_interface.main_window import MainWindow
from game_engine.game_manager import GameManager

class AppManager(QObject):
    def __init__(self):
        super().__init__()
        print("AppManager initiated")

    def start_app(self):
        app = QApplication(sys.argv)
        self.main_window = MainWindow(self)
        self.main_window.show()
        self.game_manager = GameManager(self)
        self.connect_singal_slot()
        self.start_game()
        sys.exit(app.exec_())

    def start_game(self):
        self.game_manager.start()

    def start_new_game(self):
        self.game_manager.start_new_game()

    def connect_singal_slot(self):
        self.main_window.emit_single_key.connect(self.game_manager.register_single_key)
        self.game_manager.update_user_input.connect(self.main_window.guess_area.update_user_input)
        self.game_manager.update_backspace.connect(self.main_window.guess_area.update_backspace)
        self.game_manager.update_guess_word.connect(self.main_window.guess_area.update_guess_word)
        self.game_manager.update_guess_word.connect(self.main_window.keyboard_area.update_keyboard)
        self.game_manager.update_result.connect(self.main_window.result_area.update_result_info)
        self.main_window.start_new_game.connect(self.start_new_game)
        self.game_manager.newgame_start.connect(self.main_window.guess_area.clear_guess_area)
        self.game_manager.newgame_start.connect(self.main_window.keyboard_area.clear_keyboard)
