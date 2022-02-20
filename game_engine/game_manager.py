from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from pynput import keyboard
import user_interface.assets.ui_constants as uic
from game_engine.database_manager import DatabaseManager

class GameManager(QThread):
    update_user_input = pyqtSignal(str, int, int)
    update_backspace = pyqtSignal(int, int)

    def __init__(self, am):
        super().__init__()
        self.am = am
        self.current_word = None
        self.current_guessword =  None
        self.guess_x = 0
        self.guess_y = 0
        self.dbm = DatabaseManager()

    @pyqtSlot()
    def run(self):
        self.start_new_game()

    def start_new_game(self):
        # Clear guess area
        # Clear result area
        self.current_word = self.dbm.get_random_word()
        self.current_guessword = ""
        self.guess_x = 0
        self.guess_y = 0
        self._start_listen()

    def _process_character(self, ch):
        if len(ch) == 1 and self.guess_x < 5:
            self.update_user_input.emit(ch, self.guess_x, self.guess_y)
            self.guess_x += 1
            self.current_guessword += ch
        elif ch == "BACKSPACE" and self.guess_x > 0:
            self.guess_x -= 1
            self.update_backspace.emit(self.guess_x, self.guess_y)
            self.current_guessword = self.current_guessword[:-1]
        elif ch == "ENTER" and self.guess_x == 5:
            pass

    @pyqtSlot(str)
    def register_single_key(self, key):
        self._process_character(key)

    def _start_listen(self):
        listener = keyboard.Listener(on_press = self._on_press)
        listener.start()
        listener.join()

    def _on_press(self, key):
        try:
            k = key.char
        except:
            k = key.name
        if k.upper() in uic.KEYS_OF_INTEREST:
            self._process_character(k.upper())
            if self.guess_y >= 6 and self.guess_x >= 5:
                return False

    def verify_word(self, word):
        pass
