from mimetypes import guess_type
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from pynput import keyboard
import user_interface.assets.ui_constants as uic
from game_engine.database_manager import DatabaseManager
from user_interface.components.play_area.guess_area import TILE_TYPES

class GameManager(QThread):
    update_user_input = pyqtSignal(str, int, int)
    update_backspace = pyqtSignal(int, int)
    update_guess_word = pyqtSignal(list, int)
    update_result = pyqtSignal(str, str)
    newgame_start = pyqtSignal()

    def __init__(self, am):
        super().__init__()
        self.am = am
        self.current_word = None
        self.current_guessword =  None
        self.guess_x = 0
        self.guess_y = 0
        self.game_over = False
        self.dbm = DatabaseManager()

    @pyqtSlot()
    def run(self):
        self.start_new_game(True)

    def start_new_game(self, init_run = False):
        self.current_word = self.dbm.get_random_word()
        print(self.current_word)
        self.current_guessword = ""
        self.guess_x = 0
        self.guess_y = 0
        self.game_over = False
        self.newgame_start.emit()
        self.update_result.emit(f"Lets guess the word! You have {6 - self.guess_y} tries.", "black")
        if init_run:
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
            if self.dbm.validate_word(self.current_guessword):
                self._compare_guess_word()
                self.guess_x = 0
                self.guess_y += 1
                if self.current_word == self.current_guessword:
                    self.update_result.emit(f"Congrats! You won. Yes the word was: '{self.current_word}'", "green")
                    self.game_over = True
                else:
                    self.update_result.emit(f"Lets guess the word! You have {6 - self.guess_y} tries.", "black")
                self.current_guessword = ""
                if self.guess_y >= 6:
                    self.game_over = True
                    self.update_result.emit(f"Sorry you lost. The word was '{self.current_word}'", "red")
            else:
                self.update_result.emit(f"The word you entered '{self.current_guessword}' is not in the database!", "red")
                pass

    def _game_over(self):
        pass

    def _compare_guess_word(self):
        guess_result = []
        for i, cl in enumerate(self.current_word):
            cgl = self.current_guessword[i]
            if cgl == cl:
                guess_result.append({
                    "letter": cgl,
                    "typ": TILE_TYPES["POSITION"],
                    "x": i
                })
            elif cgl in self.current_word:
                guess_result.append({
                    "letter": cgl,
                    "typ": TILE_TYPES["CONTAIN"],
                    "x": i
                })
            else: 
                 guess_result.append({
                     "letter": cgl,
                    "typ": TILE_TYPES["WRONG"],
                    "x": i
                })
        self.update_guess_word.emit(guess_result, self.guess_y)

    @pyqtSlot(str)
    def register_single_key(self, key):
        if not self.game_over:
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

        if not isinstance(k, str):
            k = ""
        if k.upper() in uic.KEYS_OF_INTEREST and not self.game_over:
            self._process_character(k.upper())
